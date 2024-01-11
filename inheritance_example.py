class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Welcome to inheritance")

class Dog(Animal):
    def speak(self):
        print("says woof!!!!!!!",self.name)

class Cat(Animal):
    def speak(self):
        print("says meow!!!!!!!!",self.name)

d=Dog("puppy")
d.speak()

d=Cat("dommy")
d.speak()