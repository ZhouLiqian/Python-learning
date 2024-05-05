# Time: 2022/6/14
# Created by Qian
# Purpose: Set/Dict/List/Tuple

from numpy import empty
from sqlalchemy import true
# import py

"""
- 集合：
    - 创建集合
    - 类型转换
    - 求取交集
"""
# 创建集合
empty_set=set()
even_numbers={0,2,4,6,8}
odd_numbers={1,3,5,7,9}

# 类型转换
letters1=set('letters')
letters2=set(['Dasher','Dancer','Prancer','Mason-Dixon'])
letters3=set(('Ummagumma','Echoes','Atom Heart Mother'))
letters4=set({'apple':'red','orange':'orange','cherry':'red'})

drinks={
    'martini':{'vodka','vermouth'},
    'black russian':{'vodka','kahlua'},
    'white russian':{'cream','kahlua','vodka'},
    'manhattan':{'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
}
# # 测试存在
# for name,contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)

# 求取交集
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
# print(drinks)


"""
- 字典(可变类型):
    - 创建字典
    - 双值子序列转换为字典
    - 添加/修改元素
    - 合并字典
    - 删除元素
    - 获取元素
    - 获取键、值
    - 赋值/复制
"""
# 创建字典
empty_dict={}
bierce={
    "day":"A period of twenty-four hours,mostly misspent",
    "positive":"Mistaken at the top of one's voice",
    "misfortune":"The kind of fortune that never misses",
}

# 双值子序列转换为字典
lol=[['a','b'],['c','d'],['e','f']]
lol=dict(lol)
lot=[('a','b'),('c','d'),('e','f')]
lot=dict(lot)
tol=(['a','b'],['c','d'],['e','f'])
tol=dict(tol)
los=['ab','cd','ef']
los=dict(los)
tos=('ab','cd','ef')
tos=dict(tos)

# 添加/修改元素
pythons={
    'Chapman':'Graham',
    'Cleese':'John',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
}
pythons['Gilliam']='Terry'

# 合并字典
others={'Marx':'Groucho','Howard':'Moe'}
pythons.update(others)

# 删除元素
del pythons['Marx']
del pythons['Howard']
pythons.clear()
pythons={}

# # 判断是否存在
# pythons={
#     'Chapman':'Graham',
#     'Cleese':'John',
#     'Idle':'Eric',
#     'Jones':'Terry',
#     'Palin':'Michael',
# }
# if 'Chapman' in pythons:
#     print('True')
# else:
#     print('False')

# 获取元素
pythons={
    'Chapman':'Graham',
    'Cleese':'John',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
}
pyth=pythons['Cleese']
pyth=pythons.get('Cleese')
pyth=pythons.get('Marx','Not a Python')
pyth=pythons.get('Marx')

# 获取键、值
signals={'green':'go','yellow':'go faster','red':'smile for the camera'}
sig=signals.keys()
sig=list(sig)
val=signals.values()
val=list(val)
item=signals.items()
item=list(item)

# 赋值/复制
signals={'green':'go','yellow':'go faster','red':'smile for the camera'}
save_signals=signals
signals['blue']='confuse everyone'
signals={'green':'go','yellow':'go faster','red':'smile for the camera'}
original_signals=signals.copy()
signals['blue']='confuse everyone'
# print(signals)


"""
- 列表(可变类型)：
    - 创建列表
    - 类型转换
    - 获取元素
    - 列表列表
    - 修改元素
    - 列表切片
    - 添加元素
    - 合并列表
    - 插入元素
    - 删除元素
    - 查询元素
    - 记录次数
    - 转字符串
    - 列表排序
    - 获取长度
    - 列表复制
"""
# 创建列表
empty_list=[]
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
another_empty_list=list()

# 类型转换
cat=list('cat')
a_tuple=('ready','fire','aim')
a_tuple=list(a_tuple)
birthday='1/6/1952'
birthday=birthday.split('/')

# 获取元素
marxes1=['Groucho','Chico','Harpo']
marxes1=marxes1[0]

# 列表列表
small_birds=['hunmingbird','finch']
extinct_birds=['dodo','passenger pigeon','Norwegian Blue']
carol_birds=[3,'French hens',2,'turtledoves']
all_birds=[small_birds,extinct_birds,'macaw',carol_birds]

# 修改元素
marxes2=['Groucho','Chico','Harpo']
marxes2[2]='Wanda'

# 列表切片
marxes3 = ['Groucho','Chico','Harpo','Wanda']
marxes3 = marxes3[0:4]
marxe3 = marxes3[::3]
marx3 = marxes3[::-1]

# 添加元素
marxes3.append('Zeppo')

# 合并列表
mar3=['Groucho','Chico','Harpo','Wanda']
others=['Gummo','Karl']
mar3.extend(others)
mar4=['Groucho','Chico','Harpo','Wanda']
mar4+=others
mar5=['Groucho','Chico','Harpo','Wanda']
mar5.append(others)

# 插入元素
mar6=['Groucho','Chico','Harpo','Wanda']
mar6.insert(3,'Gummo')
mar6.insert(10,'Karl')

# 删除元素
del mar6[-1]
del mar6[2]
mar6.remove('Gummo')
marxes2 = ['Groucho','Chico','Harpo']
mar2 = marxes2.pop()
mar1 = marxes2.pop(1)

# 查询元素
list=['Groucho','Chico','Harpo','Zeppo']
position=list.index('Zeppo')

# # 判断是否存在
# if 'Har' in list:
#     print("True")
# else:
#     print("False")

# 记录次数
coun=['Groucho','Chico','Harpo','Zeppo','Groucho','Groucho']
record=coun.count('Groucho')

# 转字符串
change = ','.join(coun)
switch = '*'.join(list)
# print(change)
# print(switch)

# 列表排序
# 1:保存为副本，不影响原列表
sorted_coun=sorted(coun)
# 2:对原列表执行排序操作
coun.sort()
list.sort(reverse=True)

# 获取长度
length=len(list)

# 列表复制
a=[1,2,3]
b=a.copy()
c=a
d=a[:]

# print(b,c,d)
# print(None)


"""
- 元组(不可变类型):
    - 创建元组
    - 元组解包
    - 元素交换
"""
# 创建元组
empty_tuple = ()
one_marx ='Groucho',
marx_tuple1 = 'Groucho', 'Chico', 'Harpo'
marx_tuple2 = 'Groucho', 'Chico', 'Harpo',
marx_tuple3 = ('Groucho', 'Chico', 'Harpo')

# 元组解包
a, b, c = marx_tuple1

# 元素交换
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password

# print(password,icecream)