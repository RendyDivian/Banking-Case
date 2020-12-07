class Bank:
    number_of_customers = 0

    def __init__(self, bank_name, customers):
        self.bank_name = bank_name
        self.customers = customers

    def add_customer(self, first_name, last_name, number_of_customers=0):
        self.customers.append(Customer(first_name, last_name))
        number_of_customers += 1

    def get_number_of_customers(self):
        return self.number_of_customers

    def get_customers(self, index):
        return self.customers[index]


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Account()

    def get_fname(self):
        return self.first_name

    def get_lname(self):
        return self.last_name

    def get_acc(self):
        return self.account

    def set_acc(self, acc):
        self.account = acc


class Account:
    #class variable
    noOfAccounts = 0

    def __init__(self, balance=0):
        self.balance = balance  #instance variable

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False


class Account:

    def menu():
        print('\n''Hello Customer!')
        print('What would you like to do?''\n''1. Balance''\n''2. Deposit''\n''3. Withdraw''\n''4. Quit')
        pick = input('Please pick a service(1,2,3,4): ')
        if pick == '1':
            Account.getBalance()
        if pick == '2':
            Account.deposit()
        if pick == '3':
            Account.withdraw()
        if pick == '4':
            current_user.pop(0)
            Bank().addCustomer()

