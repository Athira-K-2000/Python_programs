class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        pass
class Manager(Employee):
    def __init__(self,name,salary,num_suborinates):
        self.name=name
        self.salary=salary
        self.num_subordinates=num_suborinates
    def display(self):
        print("\n",". The name is :",self.name,"\n",". Salary is:",self.salary,"\n",". num_subordinates is :",self.num_subordinates)
class Developer(Employee):
    def __init__(self,name,salary,prog_lang):
        self.name=name
        self.salary=salary
        self.prog_lang=prog_lang
    def display(self):
        print("\n",". The name is :",self.name,"\n",". Salary is:",self.salary,"\n",". list of programming language is :",self.prog_lang)
p1=Manager("Rohini",45000,10)
p1.display()
p2=Developer("Arun",35000,7)
p2.display()