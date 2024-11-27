def binary_search(arr, target):
    """
    二分查找函数

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

# 示例用法
if __name__ == "__main__":
    # 创建一个已排序的数组
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_value = 7  # 要查找的目标值

    # 调用二分查找函数
    result_index = binary_search(sorted_array, target_value)

    # 输出结果
    if result_index != -1:
        print(f"目标值 {target_value} 在索引 {result_index} 处找到。")
    else:
        print(f"目标值 {target_value} 未找到。")