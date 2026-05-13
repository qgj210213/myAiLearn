# Python 常用 list / map / 相关内置函数 详解速查表

本文件为教学速查表（面向 Python 3.x），放在当前路径：
`AI_PRJ_LEARN/learndemo/WeekOne/py_base/list_map_methods.md`。
内容包含常用 `list` 方法与 `map` / `filter` / `zip` / `enumerate` / `reduce` 等函数的说明、可复制的多行示例以及示例输出与注意事项。

> 说明：本文示例均以 Python 3.x 为准；`map` 在 Python 3 返回惰性 `map` 对象，需用 `list()` 或显式迭代来消费结果。

---

## 目录

- 列表方法（总览表）
- 列表方法详例（每个方法 2~3 行示例）
- 内置函数与常用组合（总览表）
- `map` 专节：行为、多参数与惰性示例
- 使用建议与注意事项
- 在 Jupyter / PowerShell 中运行示例说明

---

## 列表方法（总览表）

| 方法 | 说明 | 简短示例 |
|---|---:|---|
| `append(x)` | 在列表尾部添加单个元素 | `lst.append(4)` |
| `extend(iterable)` | 在列表尾部一次性扩展多个元素 | `lst.extend([4,5])` |
| `insert(i, x)` | 在索引 `i` 前插入元素 `x` | `lst.insert(1, 99)` |
| `pop([i])` | 移除并返回索引 `i` 的元素（默认最后一个） | `lst.pop()` |
| `remove(x)` | 删除第一个值为 `x` 的元素 | `lst.remove(2)` |
| `clear()` | 清空列表 | `lst.clear()` |
| `index(x[, start[, end]])` | 返回第一次出现 `x` 的索引 | `lst.index(3)` |
| `count(x)` | 统计值 `x` 出现次数 | `lst.count(2)` |
| `sort(key=None, reverse=False)` | 原地排序 | `lst.sort()` |
| `reverse()` | 原地反转顺序 | `lst.reverse()` |
| `copy()` | 返回浅拷贝 | `lst2 = lst.copy()` |

> 注：表格为总览，下面会给出详细多行示例（包含边界情况与常见陷阱）。

---

## 列表方法详例

### 1) append / extend / insert
```python
lst = [1, 2, 3]
# append 添加单个元素
lst.append(4)
print(lst)  # 输出: [1, 2, 3, 4]

# extend 添加可迭代对象的所有元素
lst.extend([5, 6])
print(lst)  # 输出: [1, 2, 3, 4, 5, 6]

# insert 在位置 1 前插入 99
lst.insert(1, 99)
print(lst)  # 输出: [1, 99, 2, 3, 4, 5, 6]
```

注意：`append([5,6])` 会把整个列表作为单个元素追加，结果变成嵌套列表。

### 2) pop / remove
```python
lst = [10, 20, 30, 40]
val = lst.pop()  # 弹出最后一个
print(val, lst)  # 输出: 40 [10, 20, 30]
val = lst.pop(0) # 弹出索引 0
print(val, lst)  # 输出: 10 [20, 30]

# remove 删除第一个匹配项
lst = [1,2,3,2]
lst.remove(2)
print(lst)  # 输出: [1,3,2]
# remove 未找到会抛 ValueError
# lst.remove(999) -> ValueError: list.remove(x): x not in list
```

### 3) clear / index / count / copy
```python
lst = [1,2,3,2]
print(lst.count(2))  # 输出: 2
print(lst.index(3))  # 输出: 2
copy = lst.copy()
copy.append(999)
print(lst, copy)     # 原列表不受影响
lst.clear()
print(lst)  # 输出: []
```

### 4) sort / reverse
```python
lst = [3, 1, 4, 2]
lst.sort()
print(lst)  # 输出: [1,2,3,4]
# 带 key
words = ['apple', 'Banana', 'cherry']
words.sort(key=str.lower)
print(words)  # 输出: ['apple','Banana','cherry']
# reverse 原地反转
lst.reverse()
print(lst)  # 输出: [4,3,2,1]
```

### 分片赋值（slice assignment）
分片赋值是列表的强大功能，可以用来替换、插入或删除连续的一段元素。语法为 `lst[start:stop:step] = iterable`。注意：左右两边不是一一对应的限制，右侧可以是任意可迭代对象（长度可不同），但当使用步长（`step`）时，右侧长度必须与左侧选定的元素数量相同。

```python
# 基本替换：用新的子序列替换一段
lst = [0,1,2,3,4,5]
lst[2:4] = ['a','b']
print(lst)  # 输出: [0,1,'a','b',4,5]

# 插入（start==stop）
lst = [0,1,2]
lst[1:1] = ['x','y']
print(lst)  # 输出: [0,'x','y',1,2]

# 删除（赋空列表）
lst = [0,1,2,3]
lst[1:3] = []
print(lst)  # 输出: [0,3]

# 步长分片：替换时右侧长度必须与左侧被选中的元素数量一致
lst = [0,1,2,3,4,5]
lst[::2] = ['a','b','c']  # 选中索引 0,2,4 共 3 个位置
print(lst)  # 输出: ['a',1,'b',3,'c',5]

# 如果步长分片两边长度不匹配会抛出 ValueError
# lst = [0,1,2,3]
# lst[::2] = ['only','two','items']  # ValueError

# 注意：对元组不能进行分片赋值（元组不可变，会抛 TypeError）
tpl = (1,2,3)
# tpl[1:2] = [9]  # TypeError: 'tuple' object does not support item assignment
```

---

## 内置函数与常用组合（总览表）

| 函数 | 说明 | 简短示例 |
|---|---:|---|
| `map(func, *iterables)` | 将 `func` 应用于每个可迭代的对应元素（Python3 返回惰性迭代器） | `map(lambda x: x*2, [1,2,3])` |
| `filter(func, iterable)` | 过滤出使 `func(x)` 为真的元素（返回迭代器） | `filter(lambda x: x%2==0, nums)` |
| `zip(*iterables)` | 并行聚合多个可迭代的元素，长度以最短为准（返回迭代器） | `zip([1,2],[3,4])` |
| `enumerate(iterable, start=0)` | 同时返回索引与元素 | `enumerate(['a','b'])` |
| `sorted(iterable, key=None, reverse=False)` | 返回排序后的新列表（不改变原序列） | `sorted([3,1,2])` |
| `reversed(seq)` | 返回反向迭代器（不改变原序列） | `list(reversed([1,2,3]))` |
| `list(iterator)` | 将迭代器强制求值为列表 | `list(map(...))` |
| `functools.reduce(func, seq)` | 将序列累积折叠为单一值（需要 import functools.reduce） | `reduce(lambda x,y:x+y,[1,2,3])` |

下面给出多行示例与常见注意点。

---

## `map` 专节：行为与详例

### 基本用法（单个可迭代）
```python
numbers = [1, 2, 3, 4, 5]
# Python3 中 map 返回惰性 map 对象
m = map(lambda x: x**2, numbers)
print(m)            # 输出: <map object at 0x...>
print(list(m))      # 输出: [1, 4, 9, 16, 25]
# 注意：map 对象被消费后为空
print(list(m))      # 输出: []
```

### 多可迭代参数（并行）
```python
a = [1,2,3]
b = [10,20,30]
res = list(map(lambda x,y: x+y, a, b))
print(res)  # 输出: [11,22,33]

# 当长度不一致时，map 截断到最短
c = [1,2]
res = list(map(lambda x,y: x+y, a, c))
print(res)  # 输出: [2,4]  # 第三个元素被丢弃
```

若希望以最长为准并用指定填充值填补，可以使用 `itertools.zip_longest` + 列表/生成器：
```python
from itertools import zip_longest
# 为了示例自包含，这里重新定义 a 和 c
a = [1,2,3]
c = [1,2]
res = [ ( (x or 0) + (y or 0) ) for x,y in zip_longest(a, c, fillvalue=0) ]
print(res)  # 输出: [2,4,3]
```

### 惰性与副作用
```python
def f(x):
    print('calling', x)
    return x*x
m = map(f, [1,2,3])
# 此时不会打印 'calling'
print('before list')
print(list(m))
# 打印会在 list() 消费时发生
```

### 与列表推导的对比
```python
# 等价形式（结果立即生成列表）
nums = [1,2,3]
print([x*x for x in nums])         # 列表推导，立即求值
print(list(map(lambda x: x*x, nums))) # map + list，效果相同
```

---

## 其他内置函数详例：filter / zip / enumerate / reduce

### filter
```python
nums = [1,2,3,4,5]
print(list(filter(lambda x: x%2==0, nums)))  # 输出: [2,4]
```

### zip
```python
a = [1,2,3]
b = ['a','b','c']
print(list(zip(a,b)))  # 输出: [(1,'a'), (2,'b'), (3,'c')]
# 长度不等时按最短截断
print(list(zip([1,2], [10,20,30])))  # 输出: [(1,10),(2,20)]
```

### enumerate
```python
for idx, val in enumerate(['x','y'], start=1):
    print(idx, val)
# 输出:
# 1 x
# 2 y
```

### reduce
```python
from functools import reduce
nums = [1,2,3,4]
print(reduce(lambda x,y: x*y, nums))  # 输出: 24
```

---

## 使用建议与注意事项

- `map`、`filter`、`zip` 在 Python3 中都返回惰性迭代器，适合处理大数据流但要注意若需要多次遍历要先转换为列表或其他结构。
- 若函数有副作用（如写日志、修改外部状态），副作用只在迭代时发生（惰性延后）。
- `map` 并行处理多个可迭代时会按照最短的可迭代器截断；如需最长行为请配合 `itertools.zip_longest`。
- `sorted()` 不改变原序列，会返回新列表；若需原地排序使用 `list.sort()`。
- 集合 `set` 无序，若需要稳定显示请 `sorted(set_obj)`。
- 当追求高性能批量数值计算时，优先考虑 NumPy（向量化）而非 `map`/列表推导。

---

## 在 Jupyter / PowerShell 中运行示例

- 在 Jupyter Notebook 中，可以把示例代码直接复制到 cell 并运行。示例输出写在注释中作为参考。
- 在 Windows PowerShell 中运行单行脚本示例，请把多行写入 `.py` 文件后用 `python yourfile.py` 执行。

示例：在 PowerShell 中创建并运行临时文件

```powershell
# 在 PowerShell 中（单行示例）
python - <<'PY'
print(list(map(lambda x: x*2, [1,2,3])))
PY
```

---

如果你希望我把这些示例也写成一个独立的可执行示例脚本（例如 `list_map_examples.py`）并在工作区生成，我可以接着创建。
