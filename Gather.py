# Time: 2022/6/20
# Created by Qian
# Purpose: Gather

# 创建集合
empty_set=set()
even_numbers={0,2,4,6,8}
odd_numbers={1,3,5,7,9}

# 其它类型转换为集合
letters1=set('letters')
letters2=set(['Dasher','Dancer','Prancer','Mason-Dixon'])
letters3=set(('Ummagumma','Echoes','Atom Heart Mother'))
letters4=set({'apple':'red','orange':'orange','cherry':'red'})

# 测试是否存在
drinks={
    'martini':{'vodka','vermouth'},
    'black russian':{'vodka','kahlua'},
    'white russian':{'cream','kahlua','vodka'},
    'manhattan':{'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
}
# for name,contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)

# 合并及运算符
for name,contents in drinks.items():
    if contents & {'vermouth','orange juice'}:
        print(name)

# print(drinks)
