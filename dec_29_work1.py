class Animal:
    def __init__(self, name):
        self.name = name

    def makeSound(self):
        print("Generic animal sound")

class Dog(Animal):
    def makeSound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def makeSound(self):
        print("Meow! Meow!")

myDog = Dog("Buddy")
myCat = Cat("Whiskers")

def animalSound(animal):
    animal.makeSound()


animalSound(myDog)  
animalSound(myCat)  
