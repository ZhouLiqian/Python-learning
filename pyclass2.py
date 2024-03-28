"""
circle module: contains the Circle class.
"""
from curses.textpad import rectangle


class Circle:
    """
    Circle class
    """
    all_circles = []
    pi = 3.14159
    def __init__(self,r = 1) :
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self) :
        """
        determine the area of the Circle.
        """
        return self.__class__.pi * self.radius * self.radius

    @classmethod
    def total_area(cls) :
        """
        Class method to total the areas of all Circles.
        """
        total = 0
        for c in cls.all_circles :
            total = total + c.area()
        return total

class Shape :
    def __init__(self,x = 0,y = 0) :
        self.x = x
        self.y = y
    def move(self,delta_x,delta_y) :
        self.x = self.x + delta_x
        self.y = self.y + delta_y
class Square(Shape) :
    def __init__(self,side = 1,x = 0,y = 0) :
        super().__init__(x,y)
        self.side = side
class Circle(Shape) :
    def __init__(self,r = 1,x = 0,y = 0) :
        super().__init__(x,y)
        self.radius = r


# instance(1)
class Rectangle:
    def __init__(self,long,width) :
        self.long = long
        self.width = width
    def area(self) :
        return self.long * self.width 

# instance(2)
"""
circle module: contains the Circle class.
"""
class Circle:
    """
    Circle class
    """
    all_circles = []
    pi = 3.14159
    def __init__(self,r) :
        self.radius = r
        self.__class__.all_circles.append(self)
    def circumference(self) :
        """
        determine the circumference of the Circle.
        """
        return self.__class__.pi * 2 * self.radius

    @classmethod
    def total_circumference(cls) :
        """
        Class method to total the areas of all Circles.
        """
        total = 0
        for c in cls.all_circles :
            total = total + c.circumference()
        return total

# instance(3)
class Rectangle:
    def __init__(self) :
        self.long = 10
        """
        __width is a private variable.
        """
        self.__width = 5
    def area(self) :
        return self.__long * self.__width 


