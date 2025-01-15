# Python语法

## 数组

### 1.  符号

|      | 含义     | case     |
| ---- | -------- | -------- |
| //   | 向下取整 | 5//2=2   |
| %    | 取余     | 5%2=1    |
| x**y | x的y次方 | 4**0.5=2 |

### 2. 交换两个元素

```python
left,right = right,left

# 下标嵌套，必须修复，否则死循环！！！
# 例如 交换nums[i]  nums[nums[i]-1]
# 1. 记录正确下标
a,b=nums[i],nums[nums[i]-1]
# 2. 不嵌套再交换
nums[i]=b
nums[a-1]=a
```

### 4. 取值范围  ==左闭右开==

`nums[0:n]` 取值范围是0~n-1，差值就是包含的元素个数。

### 5. 数组翻转

```python
# ===================原地翻转=================
# 方案一
nums = [1, 2, 3, 4, 5]
nums.reverse()  
# 方案二  双指针 双闭区间
left,right=0,n-1
while left<right:
   nums[left],nums[right]=nums[right],nums[left]
   left+=1
   right-=1
# ===================返回新对象================= 
nums[::-1] 
# 切片语法为 start:end:step，其中：
	# start：切片的起始位置（默认是开头）。
	# end：切片的结束位置（默认是末尾）。
	# step：步长，表示切片时的移动步伐，可以为正数或负数。
```

### 6. lambda表达式

```python
lambda 参数1,参数2: 操作并返回

add = lambda x, y: x + y
print(add(3, 5))  # 输出 8
```

### 7. sort排序

- 共同参数

  - key: 可选，按照元素本身进行排序
  - reverse：可选，默认False从小到大，True从大到小

- sort()  原地排序。默认从小到大。

  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  numbers.sort()
  print(numbers)  # 输出 [1, 1, 2, 3, 4, 5, 6, 9]
  
  # 示例
  intervals = [[3, 5], [1, 4], [2, 6]]
  intervals.sort(key=lambda x: x[0])  # 按照元素的第一个值排序
  ```

- sorted 返回新对象，默认从小到大。

  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  sorted_numbers = sorted(numbers)
  print(sorted_numbers)  # 输出 [1, 1, 2, 3, 4, 5, 6, 9]
  ```

### 8. 获取指定元素下标

```python
index = nums.index(value) #元素重复时，只返回第一个下标
```

## 集合

- set   用于==去重==和==判断元素是否存在==

  ```python
  my_set = set() # 创建集合
  my_set.add(4) # 新增
  my_set.remove(3) # 删除指定元素
  ```

- Counter  ==统计元素频率==，底层是字典Dict

  ```python
  from collections import Counter
  counter = Counter([1,2,2,2]) # 创建  {2:3,1:1}
  counter['a']=xxx  # 更新Value
  counter.pop(key)  # 删除key
  ```

## 栈 先进后出

```python
stack = [] # list模拟栈，创建一个空栈
stack.append(1) # 入栈
top_element = stack.pop() # 出栈
```

## 队列 先进先出

```python
from collections import deque
dq = deque() # 创建一个双端队列
dq.append(value)  # 队尾添加元素
head = dq.popleft() # 队头移出元素
```

