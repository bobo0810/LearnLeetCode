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