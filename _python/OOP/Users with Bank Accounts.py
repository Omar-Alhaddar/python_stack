class User:		
    def __init__(self, name, ):
        self.name = name
        self.account
    
    def make_deposit(self, amount):
        self.account.balance += amount	

    def make_withdrawal(self, amount):
    	self.account.balance -= amount	
    
    def display_user_balance(self):
        print(self.name)
        print(self.account.balance)
    def transfer_money(self,other_user,amount):
        other_user.account.balance += amount
        self.account.balance -= amount


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

