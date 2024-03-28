##### if/else
from turtle import position


furry=True
small=True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human.Or a hairless bear.")

##### if/elif/else
color="puce"
if color=="red":
    print("It's a tomato.")
elif color=="green":
    print("It's a green pepper.")
elif color=="bee purple":
    print("I don't know what it is,but only bees can seee it.")
else:
    print("I've never heard of the color.",color)

##### empty=false
some_list=[]
if some_list:
    print("There's something in here.")
else:
    print("Hey,it's empty!")

##### while/break
# count=1
# while count<=5:
#     print(count)
#     count=count+1

##### while True:
#     stuff=input("String to capitalize [type q to quit]:")
#     if stuff=="q":
#         break
#     print(stuff.capitalize())

##### continue/while/break
# while True:
#     value=input("Integer,please [q to quit]:")
#     # 跳出循环
#     if value=='q':
#         break
#     number=int(value)
#     # 继续循环
#     if number % 2==0:
#         continue
#     print(number,"squared is",number*number)

##### while/else
numbers=[1,2,3,5]
position=0
while position<len(numbers):
    number=numbers[position]
    if number % 2==0:
        print("Found even number",number)
        break
    position+=1
# 未调用break执行的检查
else:
    print("No even number found")

##### for/break/continue/else
# rabbits=['Flopsy','Mopsy','Cottontail','Peter']
# current=0
# while current<len(rabbits):
#     print(rabbits[current])
#     current+=1
# for rabbit in rabbits:
#     print(rabbit)
# accusation={'room':'ballroom','weapon':'lead pipe','person':'Col.Mustard'}
# for card in accusation:
#     print(card)
# for value in accusation.values():
#     print(value)
# for item in accusation.items():
#     if item == ('person', 'Col.Mustard'):
#         break
#     print(item)
# cheeses=[]
# for cheese in cheeses:
#     print('This shop has some lovely',cheeses)
#     break
# # 循环未正常结束，进入else
# else:
#     print('This is not much of a cheese shop,is it?')
cheeses=['cheese1']
found_one=False
for cheese in cheeses:
    found_one=True
    print('This shop has some lovely.',cheese)
    break
if not found_one:
    print('This is not much of a cheese shop,is it?')

#####zip()
days=['Monday','Tuesday','Wednesday']
fruits=['banana','orange','peach']
drinks=['coffee','tea','beer']
desserts=['tiramisu','ice cream','pie']
# for zipped in zip(days,fruits,drinks,desserts):
#     print(zipped)
for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,":drink",drink,"- eat",fruit,"- enjoy",dessert)
english='Monday','Tuesday','Wednesday'
french='Lundi','Mardi','Mercredi'
# list
conlis=list(zip(english,french))
print(conlis)
# dictionary
con=dict(zip(english,french))
print(con)

##### range()
for x in range(0,3,1):
    print(x)
lirang=list(range(0,3))
print(lirang)