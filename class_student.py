class Student:
    def __init__(self,name,number,address):
        self.name=name
        self.number=number
        self.address=address

    def display(self):
        print("Student name :",self.name,", Phone number :",self.number,", Address :",self.address)

p1=Student("Athira",9946949353,"Valanchery")
p1.display()