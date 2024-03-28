# Time: 2022/6/14
# Created by Qian
# Purpose: List


from sqlalchemy import true
# 创建列表
empty_list=[]
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
another_empty_list=list()

# 将其他数据类型转换为列表
cat=list('cat')
a_tuple=('ready','fire','aim')
a_tuple=list(a_tuple)
birthday='1/6/1952'
birthday=birthday.split('/')

# 获取元素
marxes1=['Groucho','Chico','Harpo']
marxes1=marxes1[0]

# 列表的列表
small_birds=['hunmingbird','finch']
extinct_birds=['dodo','passenger pigeon','Norwegian Blue']
carol_birds=[3,'French hens',2,'turtledoves']
all_birds=[small_birds,extinct_birds,'macaw',carol_birds]

# 修改元素
marxes2=['Groucho','Chico','Harpo']
marxes2[2]='Wanda'

# 使用切片提取元素
marxes3=['Groucho','Chico','Harpo','Wanda']
marxes3=marxes3[0:4]
marxe3=marxes3[::3]
marx3=marxes3[::-1]

# 添加元素至尾部
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
marxes2=['Groucho','Chico','Harpo']
mar2=marxes2.pop()
mar1=marxes2.pop(1)

# 查询元素位置
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

# 列表转换为字符串
change = ','.join(coun)
switch = '*'.join(list)

# 排序
# 1:保存为副本，不影响原列表
sorted_coun=sorted(coun)
# 2:对原列表执行排序操作
coun.sort()
list.sort(reverse=True)

# 获取长度
length=len(list)

# 复制
a=[1,2,3]
b=a.copy()
c=a
d=a[:]

print(b,c,d)
print(None)