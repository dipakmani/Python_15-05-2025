# class define krna
# constructor create krna
# variables assign krna hai
# object se constructor ko call karna

class AxisBank:

    def __init__(self,username,pan_no,address):
        self.username = username
        self.pan_no = pan_no
        self.address = address
        self.balance = 0

    def deposit(self,amount):
        self.balance=self.balance+amount


    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount

b=Bank()
            



