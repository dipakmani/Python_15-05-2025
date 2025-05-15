

class Bank:
    bankname="Central India Bank"
    branch="Pune,MH,India"

    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0 # starting account balance 0 
    
    def show_details(self,username,acc_no)
        print(f'{self.username}')

    #deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully')

    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficent Fund...')

    #ministatement
    def ministatement(self):
        print(f'Your account balance is {self.balance}')


print(f'Welcome to {Bank.bankname} , {Bank.branch}')
#collect user data for account creation
username=input('Enter Your name :')
pan=input('Enter PAN card number : ')
address=input('Enter Your address : ')

b=Bank(username,pan,address) # object creation based on user provided data

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop')
    option=int(input(' '))

    if option==1:
        amount=float(input('Enter Deposited amount : '))
        b.deposit(amount)

    elif option==2:
        amount=float(input('Enter Withdraw amount : '))
        b.withdraw(amount)

    elif option==3:
        b.ministatement()

    elif option==4:
        print('Thanks for using Central India Bank .... ')
        break
    else:
        print('Invalid Option plz select a valid option')
