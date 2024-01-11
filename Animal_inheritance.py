class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("\n","The name is:",self.name,"\n","The age is :",self.age )
class Mammal(Animal):
    def __init__(self,fur_color):
        self.fur_color=fur_color
    def giveBirth(self):
        print("\n","Fur color is :",self.fur_color)
class Bird(Animal):
    def __init__(self,feather_color):
        self.feather_color=feather_color
    def fly(self):
        print("\n","The feather color is :",self.feather_color)
class Fish(Animal):
    def __init__(self,weight):
        self.weight=weight
    def swim(self):
        print("\n","The sur name is :",self.weight)
p1=Mammal("dog",5,"black")
p1.display()
p1.giveBirth()
p2=Bird("parrot",2,"green")
p1.display()
p2.fly()
p3=Fish("catfish",1,"37")
p1.display()
p3.swim()