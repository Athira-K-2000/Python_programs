class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def start(self):
        print("Welcome")

    def stop(self):
        pass
    
class Car(Vehicle):
    def display(self,num_doors):
        self.num_doors=num_doors
        print("Make :",self.make,"\nModel :",self.model,"\nDoors :",self.num_doors)

class Motorcycle(Vehicle):
    def display(self,two_wheels):
        self.two_wheels=two_wheels
        print("Make :",self.make,"\nModel :",self.model,"\nWheels :",self.two_wheels)


c=Car("Lamborgini","Urus")
c.display(4)
m=Motorcycle("Triumph","Bobber")
m.display(2)
