"""4) Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That Class Contains one class variable as ROI which is initialize to 10.5
Inside init method initialize all name and amount variable by accepting the values from user.
There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
And Display () method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects"""

class BankAccount:

    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print(f"Name: {self.name}, Amount: {self.amount}")

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        return self.amount * (BankAccount.ROI / 100)


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)


account1.display()
account1.deposit(500)
account1.withdraw(200)
print(f"Interest for {account1.name}: {account1.calculate_interest()}")

account2.display()
account2.deposit(1000)
account2.withdraw(500)
print(f"Interest for {account2.name}: {account2.calculate_interest()}")
