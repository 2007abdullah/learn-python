class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
            self.balance+=amount
            print("Amount deposited:",amount)
            print("New balance:",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Amount withdrawn:",amount)
            print("New balance:",self.balance)


user1= bankaccount("Abdullah",1000)
user1.deposit(500)
user1.withdraw(200) 
