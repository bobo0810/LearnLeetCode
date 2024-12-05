# Python语法

## 数字

```
//向下取整     %取余
```



## 数组

### 1. 交换两个元素

```python
# 
left,right = right,left

# 涉及到嵌套，必须普通写法
temp=nums[nums[i] - 1]
nums[nums[i] - 1]=nums[i]
nums[i]=temp
```

### 2. 取值范围

[0:n]取值范围是0~n-1，左闭右开

### 3. 数组翻转

```python
# ===================原地翻转=================
start,end=0,n-1 # 双闭区间
while start<end:
   nums[start],nums[end]=nums[end],nums[start]
   start+=1
   end-=1
# ===================返回新对象================= 
nums[::-1]  
# 切片语法为 start:end:step，其中：
	# start：切片的起始位置（默认是开头）。
	# end：切片的结束位置（默认是末尾）。
	# step：步长，表示切片时的移动步伐，可以为正数或负数。
```

### 4. lambda表达式

```python
lambda 参数1,参数2: 操作并返回

add = lambda x, y: x + y
print(add(3, 5))  # 输出 8

```

```python
# 子数组按照指定key排序
intervals = [[3, 5], [1, 4], [2, 6]]
sorted_intervals = sorted(intervals, key=lambda x: x[0])
print(sorted_intervals)
```

### 5. sort排序

- sort()  原地排序，无返回值。默认从小到大。

  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  numbers.sort()
  print(numbers)  # 输出 [1, 1, 2, 3, 4, 5, 6, 9]
  ```

- sorted 返回新对象，默认从小到大。

  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  sorted_numbers = sorted(numbers)
  print(sorted_numbers)  # 输出 [1, 1, 2, 3, 4, 5, 6, 9]
  ```

- 共同参数

  - key: 可选，按照元素本身进行排序
  - reverse：可选，默认False从小到大，True从大到小

## 集合

- Set  add添加元素，remove移除元素
- Counter    本质是dict，字符及出现次数，默认为0。 删除key是aaa.pop(key)



## 字符串

### 1. 字符列表转为字符串

```python
chars = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(chars)   # 拼接成"Python"
```

## 堆

import  heapq，默认最小堆。堆顶始终是堆中最小的值

- 弹出最小元素：heapq.heappop(heap_x)  
- 压入元素：heapq.heappush(heap, item)



## 栈

List模拟栈，队尾追加append    队尾弹出pop



## 队列

双端队列deque

- 队头移出  deque.popleft()
- 队尾移出 deque.pop()
- 队尾添加元素  deque.append()
