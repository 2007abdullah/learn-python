class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.get_balance() * 0.05
        self.deposit(interest)
        print("Interest added")


acc = SavingsAccount("Ali", 1000)

acc.deposit(500)
acc.withdraw(200)
acc.add_interest()
print("Final Balance:", acc.get_balance())