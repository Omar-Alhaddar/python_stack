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

guido.make_deposit(50)
guido.make_deposit(50)
guido.make_deposit(50)
guido.make_withdrawal(50)
guido.display_user_balance()

lana.make_deposit(50)
lana.make_deposit(50)
lana.make_withdrawal(20)
lana.make_withdrawal(20)
lana.display_user_balance()

omar.make_deposit(500)
omar.make_withdrawal(50)
omar.make_withdrawal(50)
omar.make_withdrawal(50)
omar.display_user_balance()

guido.transfer_money(omar, 30)
guido.display_user_balance()
omar.display_user_balance()