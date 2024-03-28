### define class
from re import S


class Person():
    pass
someone = Person()

class Person():
    """
    Create an instance object from the class definition.
    """
    def __init__(self):
        pass

class Person():
    def __init__(self,name):
        self.name = name
"""
1. View the Person class definition;
2. Create a new object;
3. Call the object's method and new object -> self and new parameters -> name;
4. The value of name -> new object;
5. Return new object;
6. Make hunter = new object;
"""
hunter = Person('Elmer Fudd')
# print('The mighty hunter:', hunter.name)

### inherit
class Car():
    pass
class Yugo(Car):
    pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

### Override method
class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

class Person():
    def __init__(self,name):
        self.name = name
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor," + name
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ",Esquire"
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)

# add new method
class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
# give_me_a_yugo.need_a_push()

# super: call father method to subclass
class Person():
    def __init__(self, name):
        self.name = name
"""
1. super(): get father definition.
2. _init_() in subclass calls Person._init_() method.
3. "self.email" distinguishes between EmailPerson and Person. 
"""
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
bob = EmailPerson('Bob Frapples','bob@frapples.com')
# print(bob.name)
# print(bob.email)

### self
class Car():
    def exclaim(self):
        print("I'm a Car!")
"""
1. Find the class 'Car' to which object 'car' belongs.
2. Make self = car and exclaim -> car.
"""
car = Car()
# car.exclaim()
# Car.exclaim(car)

### Use properties(属性) to get and set properties
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
# fowl = Duck('Howard')
# # fowl.name = 'Daffy'
# # print(fowl.name)
# print(fowl.hidden_name)

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
# fowl = Duck('Howard')
# fowl.name = 'Daffy'
# print(fowl.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
# print(c.radius)
# print(c.diameter)

# protect private attribute by adjusting name
"""
1. 设置属性，保护特性；
2. 代码重整，外部无法访问；
3. 类内修改特性，属性不变；
"""
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the getter')
        self.__name = input_name
fowl = Duck('Howard')
# fowl.name = 'Donald'
# print(fowl.name)
print(fowl._Duck__name)

# type of method


