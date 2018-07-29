class Account:

    def __init__(self, filepath):
        # set the filepath arg to a variable to be used elsewhere
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())


    def withdraw(self, amount):
        ''' balance - amount = new_balance '''
        self.balance = self.balance - amount


    def deposit(self, amount):
        self.balance = slef.balance + amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


account = Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()
