class BankAccount:
    def __init__(self,account_number,balence):
        self.account_number=account_number
        self.balence=balence
    def display(self):
        print("\n",".Account number is:",self.account_number,"\n",".Balence is :",self.balence)
        def deposit(self):
            print("Depositer")
        def withdraw(self):
            print("withdrawer")
class SavingsAccount(BankAccount):
    def __init__(self,interest_rate):
        self.interest_rate=interest_rate
    def display(self):
        print("\n",".Interet rate is:",self.interest_rate)
class CheckingAccount(BankAccount):
    def __init__(self,limit):
        self.limit=limit
    def display(self):
        print("\n",".The limit on overdraft is :",self.limit)    

p1=BankAccount("xxxxxxx7894",50000)
p1.display()
p2=SavingsAccount("12%")
p2.display()
p3=CheckingAccount("8%")
p3.display()