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

# 示例用法
if __name__ == "__main__":
    # 创建一个待排序的数组
    array = [3, 6, 8, 10, 1, 2, 1]
    print("Original Array:", array)

    # 调用快速排序   数组原地操作
    quicksort(array, 0, len(array) - 1)
    print("Sorted Array:", array)