class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds!")

    def displayBalance(self):
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate / 100  

    def deposit(self, amount):
        super().deposit(amount)
        self.calculateInterest()

    def calculateInterest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest earned: ${interest_earned:.2f}. New balance: ${self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            super().withdraw(amount)
        else:
            print("Overdraft limit exceeded!")


savingsAccount = SavingsAccount("ABC123", "Athira", 1000, 2)
currentAccount = CurrentAccount("DEF456", "Anu", 2000, 500)

savingsAccount.deposit(500)
savingsAccount.calculateInterest()
savingsAccount.withdraw(200)
savingsAccount.displayBalance()

currentAccount.withdraw(1500)
currentAccount.displayBalance()