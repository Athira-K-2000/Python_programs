class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        print("Area of circle =",3.14*self.radius**2)

class Rectangle(Shape):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("Area of Rectangle =",2*self.length*self.breadth)

a=Circle()
a.area(5)
b=Rectangle()
b.area(5,8)