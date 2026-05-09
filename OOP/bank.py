class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_balance= 100
        self.max_withdraw=5000000
    def getBalance(self):
        print(f"Your current balance : {self.balance}")    
    def deposit(self,amount):
        self.balance +=amount
        print(f"After deposit you current balance is: {self.balance} ")    
    def withdraw(self,amount):
        if  amount > self.max_withdraw:
            print(f"can't withdraw more than {self.max_withdraw} ")
        elif amount > self.balance:
            print(f" you balance: {self.balance} , Can't withdraw more than you balance") 
        elif  amount < self.min_balance:
            print(f"You can't withdraw min {self.min_balance}")  
        else:
            self.balance -=amount
            print(f"After withdraw {amount} you current balance is : {self.balance}")       


brace=bank(20000)
brace.deposit(300)
brace.withdraw(50)
brace.withdraw(1000000000)
brace.withdraw(2000)
brace.getBalance()
