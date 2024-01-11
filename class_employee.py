class Employee:
    def __init__(self,name,code,salary):
        self.name=name
        self.code=code
        self.salary=salary

    def display(self):
        print("Employee name :",self.name,", Code :",self.code,", Salary :",self.salary)

p1=Employee("Sona",1234,30000)
p1.display()