import threading

class BankAccount(object):
    lock = threading.Lock()

    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        if self.is_open:
            return 0
        else:
            raise ValueError('BankAccount is closed')

    def open(self):
        if self.is_open == True:
            raise ValueError("Already opened")
        self.balance = 0
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('BankAccount is closed')
        if amount < 0:
            raise ValueError('Amount is negative')
        with BankAccount.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('BankAccount is closed')
        if amount < 0:
            raise ValueError('Amount is negative')
        with BankAccount.lock:
            if self.balance - amount < 0:
                raise ValueError('Balance is negative')
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError("Already closed")
        self.is_open = False