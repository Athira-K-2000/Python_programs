class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def display(self,id):
        self.id=id
        print("Name :",self.name,"Age :",self.age,"id :",self.id)

p1=Employee("Athira",23)
p1.display(1234)