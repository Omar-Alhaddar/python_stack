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

omar = BankAccount()
bara = BankAccount(balance=1000000)

omar.deposit(500).deposit(500).deposit(500).withdraw(200).yield_interest().display_account_info()
bara.deposit(5000).deposit(50000).withdraw(600).withdraw(600).withdraw(600).withdraw(600).yield_interest().display_account_info()