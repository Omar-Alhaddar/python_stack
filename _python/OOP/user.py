class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount	

    def make_withdrawal(self, amount):
    	self.account_balance -= amount	
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
    def transfer_money(self,other_user,amount):
        other_user.account_balance += amount
        self.account_balance -= amount


guido = User("Guido van Rossum", "guido@python.com")
lana = User("lana theo", "lana@th")
omar = User("omar Alhaddar", "omar@gmail.com")

# guido.make_deposit(50)
# lana.make_deposit(50)
# lana.make_deposit(50)
# omar.make_deposit(50)

# print(guido.account_balance)

# print(lana.name)
# lana.make_withdrawal(10)
# lana.make_withdrawal(10)
# print(lana.account_balance)

# guido.display_user_balance()
# print(guido.account_balance)
# print(lana.account_balance)


# omar.make_deposit(50)
# omar.make_withdrawal(10)
# omar.make_withdrawal(10)
# omar.make_withdrawal(10)
# print(omar.account_balance)

# guido.transfer_money(lana, 30)
# print(guido.account_balance)
# print(lana.account_balance)