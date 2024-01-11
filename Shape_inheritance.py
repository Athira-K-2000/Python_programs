class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        print("Area of circle =",3.14*self.radius**2)
    def perimeter(self):
        print("Perimeter of circle =",2*3.14*self.radius)

class Square(Shape):
    def area(self,side):
        self.side=side
        print("Area of square =",self.side**2)
    def perimeter(self):
        print("Perimeter of square =",4*self.side)

class Triangle(Shape):
    def area(self,base,height):
        self.base=base
        self.height=height
        print("Area of triangle =",.5*self.base*self.height)
    def perimeter(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        print("perimeter of triangle",self.side1+self.side2+self.side3)

a=Circle()
a.area(5)