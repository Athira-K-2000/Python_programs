from abc import ABC,abstractmethod

#define abstrct class
class Shape(ABC):
    #abstract methods
    def area(self):
        print("Area of the shape")

    def perimeter(self):
        print("Perimeter of the shape")


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
    
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    def area(self):
        return self.side_length*self.side_length
    def perimeter(self):
        return 4*self.side_length
    

#object creation
c=Circle(5)
s=Square(6)

print("Circle area =",c.area())
print("Circle perimeter =",c.perimeter())
print("Square area =",s.area())
print("Square perimeter =",s.perimeter())