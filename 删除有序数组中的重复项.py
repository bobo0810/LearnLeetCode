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

# 示例使用
array = [1, 1, 2, 3, 3]
new_length = remove_duplicates(array)

# 输出结果
print("新的数组长度:", new_length)
print("去重后的数组:", array[:new_length])  # 输出去重后的有效元素部分