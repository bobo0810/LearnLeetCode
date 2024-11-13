# LearnAlgorithm
刷刷算法题


## 翻转链表
保存->翻转->前后移
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