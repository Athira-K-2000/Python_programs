class Person:
    def __init__(self):
        print("Welcome")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("my name is :",self.name,", my age is :",self.age)

#object creation
p1=Person()
#function calling using object
p1.display("Athira",23)
    


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        
        print("my name is :",self.name,", my age is :",self.age)

#object creation
p1=Person("Athira",23)
#function calling using object
p1.display()


class Person:
    #def __init__(self):
     #   print("Welcome")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("my name is :",self.name,", my age is :",self.age)

#object creation
p1=Person()
#function calling using object
p1.display("Athira",23)