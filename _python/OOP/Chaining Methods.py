class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self	

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self	
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self

    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
lana = User("lana theo", "lana@th")
omar = User("omar Alhaddar", "omar@gmail.com")

guido.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(50).display_user_balance()

lana.make_deposit(50).make_deposit(50).make_withdrawal(20).make_withdrawal(20).display_user_balance()

omar.make_deposit(500).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

guido.transfer_money(omar, 30).display_user_balance()
omar.display_user_balance()