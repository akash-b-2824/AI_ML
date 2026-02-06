class bankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit successful. New balance:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds.for ",amount,"Current balance:",self.balance,"Withdrawal failed.")
        else:
            self.balance-=amount
            print("Withdrawal successful. New balance:",self.balance)
    def balence(self):
        print("Current balance:",self.balance)

def baba():
    print("Hello, I am Baba!")