# Time: 2022/6/20
# Created by Qian
# Purpose: Dictionary


from numpy import empty
import py
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

print(signals)