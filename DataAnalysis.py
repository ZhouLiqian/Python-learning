# 日期和时间
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.minute)
print(dt.date())
print(dt.time())

# 三元表达式
x = 5
value = 'Non-negative' if x >= 0 else 'Negative'
print(value)