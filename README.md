# LearnAlgorithm
高频题型

## 翻转链表
思路：保存->翻转->前后移
```python
def reverse_linked_list(head):
    """
    :param head: 链表的头节点
    :return: 翻转后的链表头节点
    """
    prev = None  # 上一个节点，初始化为 None
    current = head  # 当前节点，初始化为链表的头节点

    # 遍历链表，直到当前节点为空   
    while current:
        next_node = current.next  # 保存下一个节点
        current.next = prev  # 将当前节点的next指针指向上一个节点（翻转指针）
        prev = current  # 移动 prev 到当前节点
        current = next_node  # 移动到下一个节点

    return prev  # 返回新的头节点（翻转后的链表头）
```

## 快速排序QuickSort

时间复杂度O(nlogn)

```python
def quicksort(arr, low, high):
    """
    带有指定范围的快速排序函数

    :param arr: 待排序的数组
    :param low: 排序的起始索引
    :param high: 排序的结束索引
    """
    if low < high:
        # 获取基准元素的索引
        pivot_index = partition(arr, low, high)

        # 递归排序基准左侧和右侧部分
        quicksort(arr, low, pivot_index - 1)  # 排序左侧
        quicksort(arr, pivot_index + 1, high)  # 排序右侧

def partition(arr, low, high):
    """
    分区函数，选择一个基准元素并将数组分为两部分

    :param arr: 待排序的数组
    :param low: 排序的起始索引
    :param high: 排序的结束索引
    :return: 基准元素的最终位置
    
    总结
    选择基准: 选择数组的最后一个元素作为基准。
    分区过程: 遍历数组，将小于基准的元素移动到左侧。
    放置基准: 将基准元素放到它的正确位置。
    返回值: 返回基准元素的新索引，以便快速排序的递归调用使用。
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # 小于基准的元素的最后一个索引

    # 遍历数组并进行分区
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1  # 增加小于基准的元素的索引
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素

    # 将基准元素放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 返回基准元素的位置
```

## 二分查找
时间复杂度O(logn)

定范围、循环比左右,只返回中间或-1

```python
def binary_search(arr, target):
    """
    :param arr: 已排序的数组
    :param target: 需要查找的目标值
    :return: 目标值的索引，如果不存在则返回 -1
    """
    low = 0  # 查找范围的起始索引
    high = len(arr) - 1  # 查找范围的结束索引

    while low <= high:  # 当查找范围有效时
        mid = (low + high) // 2  # 计算中间索引

        # 检查中间元素是否是目标值
        if arr[mid] == target:
            return mid  # 找到目标值，返回索引
        elif arr[mid] < target:
            low = mid + 1  # 目标值在右侧，更新起始索引
        else:
            high = mid - 1  # 目标值在左侧，更新结束索引

    return -1  # 如果未找到目标值，返回 -1
```

## 删除有序数组中的重复项
思路：快慢指针
```python
def remove_duplicates(array):
    # 检查数组是否为空，如果为空，返回 0
    if not array:
        return 0
    
    # 初始化两个指针
    slow = 1  # 指向新数组的下一个可写位置
    fast = 1  # 用于遍历原数组

    # 遍历原数组，直到 fast 指针到达数组末尾
    while fast < len(array):
        # 比较当前元素和前一个元素
        if array[fast] != array[fast - 1]:
            # 如果不同，说明找到了一个新的元素
            array[slow] = array[fast]  # 将新元素写入到 slow 指向的位置
            slow += 1  # 移动 slow 指针，准备写入下一个新元素
        # 不管是否写入，fast 都要向前移动
        fast += 1
    
    # 返回新数组的长度，即有效元素的数量
    return slow
```

## 无重复字符的最长子串
思路：滑动窗口
```python
def lengthOfLongestSubstring(strs):
    # 如果输入字符串为空，直接返回 0
    if not strs:
        return 0
    
    # 初始化最长子串的长度为 0
    ans = 0
    # 左指针，表示当前子串的起始位置
    left = 0
    # 用于存储当前窗口中的字符，确保它们是唯一的
    window = set()

    # 遍历字符串中的每个字符，右指针表示当前字符的索引
    for right, c in enumerate(strs):
        # 如果当前字符已经在窗口中，说明出现了重复字符
        while c in window:
            # 移除左指针指向的字符，缩小窗口
            window.remove(strs[left])
            # 移动左指针向右，继续缩小窗口
            left += 1
        
        # 将当前字符添加到窗口中
        window.add(c)
        # 计算当前无重复字符的子串长度，并更新最长长度
        ans = max(ans, right - left + 1)

    # 返回找到的无重复字符的最长子串的长度
    return ans
```

## 合并两个有序链表
时间复杂度为 O(m + n)
```python
def merge_two_lists(l1, l2):
    # 创建一个虚拟头节点，方便处理合并操作
    dummy = ListNode(0)
    current = dummy  # 用于遍历和构建合并链表的指针

    # 遍历两个链表，直到其中一个链表为空
    while l1 and l2:
        # 比较两个链表的当前节点的值
        if l1.val < l2.val:
            # 如果 l1 的值更小，将 l1 的节点添加到合并链表中
            current.next = l1
            l1 = l1.next  # 移动 l1 指针到下一个节点
        else:
            # 如果 l2 的值更小或相等，将 l2 的节点添加到合并链表中
            current.next = l2
            l2 = l2.next  # 移动 l2 指针到下一个节点
        
        # 移动 current 指针到合并链表的下一个位置
        current = current.next

    # 处理剩余的节点
    # 只需将 l1 或 l2 中剩余的节点连到合并链表的末尾
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    # 返回合并后的链表，去掉虚拟头节点
    return dummy.next
```