from threading import Lock
lock = Lock() 

class BankAccount(object):
    
   
    def __init__(self):
        self.active = False
        self.balance = 0

    def get_balance(self):
        while not self.active:
            raise ValueError("Account is not active. Cannot obtain balance.")
        return self.balance

    def open(self):
        if self.active:
            raise ValueError("Account is already open.")
        self.active = True

    def deposit(self, amount):
        if not self.active:
            raise ValueError("Cannot deposit into closed account.")
        if amount < 0:
            raise ValueError("Deposit amount is negative.")
        
        lock.acquire()
        self.balance += amount
        lock.release()   

    def withdraw(self, amount):
        if not self.active:
            raise ValueError("Cannot withdraw from closed account.")
        if amount < 0:
            raise ValueError("Withdraw amount is negative.")
        if amount > self.balance:
            raise ValueError("This bank does not allow overdrafting.")
        
        lock.acquire()
        self.balance -= amount
        lock.release()

    def close(self):
        if not self.active:
            raise ValueError("Account is already closed.")
        self.balance = 0
        self.active = False