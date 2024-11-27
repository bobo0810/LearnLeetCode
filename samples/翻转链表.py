class ListNode:
    def __init__(self, value=0, next=None):
        """
        链表节点类

        :param value: 节点的值
        :param next: 指向下一个节点的指针
        """
        self.value = value  # 存储节点的值
        self.next = next    # 存储指向下一个节点的指针

def reverse_linked_list(head):
    """
    翻转链表的函数

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

def print_linked_list(head):
    """
    打印链表的值

    :param head: 链表的头节点
    """
    current = head  # 从头节点开始遍历
    while current:
        print(current.value, end=" -> ")  # 打印当前节点的值
        current = current.next  # 移动到下一个节点
    print("None")  # 打印链表结束符

# 示范用法
if __name__ == "__main__":
    # 创建一个链表 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1)  # 创建头节点
    head.next = ListNode(2)  # 创建第二个节点
    head.next.next = ListNode(3)  # 创建第三个节点
    head.next.next.next = ListNode(4)  # 创建第四个节点

    print("Original Linked List:")
    print_linked_list(head)  # 打印原始链表

    # 翻转链表
    reversed_head = reverse_linked_list(head)  # 调用翻转函数

    print("Reversed Linked List:")
    print_linked_list(reversed_head)  # 打印翻转后的链表