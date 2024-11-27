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

# 示例使用
input_string = "abcabcbb"
result = lengthOfLongestSubstring(input_string)

# 输出结果
print("无重复字符的最长子串长度:", result)