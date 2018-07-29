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
        self.balance = self.balance + amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):

        self.balance = self.balance - amount - self.fee


# add dirs and files for another account


checking = Checking("balance.txt", 1)
print(checking.balance)
checking.transfer(int(input('How much?   ')))
checking.commit()
print(checking.balance)
