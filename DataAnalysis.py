# 日期和时间
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
# print(dt.day)
# print(dt.minute)
# print(dt.date())
# print(dt.time())

# 三元表达式
x = 5
value = 'Non-negative' if x >= 0 else 'Negative'
# print(value)

# 元组 - 数量统计
a = (2, 2, 2, 3, 4, 2)
valu = a.count(2)
# print(valu)

# 列表 - 插入元素/删除元素
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list.insert(1, 'red')
# print(b_list)
b = b_list.pop(2)
# print(b)

# 列表 - 组合元素
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
# print(x)

# 列表 - 二分搜索
import bisect
c = [1, 2, 2, 2, 3, 4, 7]
c1 = bisect.bisect(c, 2)
# print(c1)
c2 = bisect.bisect(c, 5)
# print(c2)
bisect.insort(c, 6)
# print(c)

# 列表 - 跟踪索引
some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
# print(enumerate(some_list))
# print(mapping)

# 匿名函数
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
result = apply_to_list(ints, lambda x: x * 2)
# print(result)

# 异常处理
def attempt_float(x):
    try:
        return float(x)
    except:
        return x
print(attempt_float('1.2345'))
print(attempt_float('something'))