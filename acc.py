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
	
	type = "checking"
	

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):

        self.balance = self.balance - amount - self.fee


# add dirs and files for another account


jack_checking = Checking("jack.txt", 1)
print(checking.balance)
jack_checking.transfer(int(input('How much?   ')))
jack_checking.commit()
print(jack_checking.balance)

john_checking = Checking("john.txt", 1)
print(checking.balance)
john_checking.transfer(int(input('How much?   ')))
john_checking.commit()
print(john_checking.balance)
