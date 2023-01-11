# Bank that manages a dictionary of Account objects

from account import *


class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.new_account_number = 0

    def ask_for_valid_account_number(self):
        account_number = input('What is your account number? ')
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if account_number not in self.accounts_dict:
            raise AbortTransaction('There is no account ' + str(account_number))
        return account_number

    def get_users_account(self):
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.askForValidPassword(account)
        return account

    def ask_for_valid_password(self, account):
        password = input('Please enter your password: ')
        account.check_password_match(password)

    def create_account(self, name, starting_amount, password):
        account = Account(name, starting_amount, password)
        new_account_number = self.new_account_number
        self.accounts_dict[new_account_number] = account
        # Increment to prepare for next account to be created
        self.new_account_number = self.new_account_number + 1
        return new_account_number

    def open_account(self):
        print('*** Open Account ***')
        name = input('What is the name for the new user account? ')
        starting_amount = input('What is the starting balance for this account? ')
        starting_amount = int(starting_amount)
        password = input('What password would you want to use for this account? ')

        account_number = self.create_account(name, starting_amount, password)
        print('Your new account number is:', account_number)
        print()

    def close_account(self):
        print('*** Close Account ***')
        account_number = input('What is your account number? ')
        account_number = int(account_number)
        password = input('What is your password? ')
        account = self.accounts_dict[account_number]
        balance = account.get_balance(password)

        if balance is not None:
            print('You had', balance, 'in your account, which is being returned to you.')
            # Remove user's account from the list of accounts
            del self.accounts_dict[account_number]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        account_number = input('Please enter your account number: ')
        account_number = int(account_number)
        password = input('Please enter the password: ')
        account = self.accounts_dict[account_number]
        balance = account.get_balance(password)
        if balance is not None:
            print('Your balance is:', balance)

    def deposit(self):
        print('*** Deposit ***')
        account_number = input('Please enter the account number: ')
        account_number = int(account_number)
        deposit_amount = input('Please enter amount to deposit: ')
        deposit_amount = int(deposit_amount)
        password = input('Please enter the password: ')
        account = self.accounts_dict[account_number]
        balance = account.deposit(deposit_amount, password)
        if balance is not None:
            print('Your new balance is:', balance)

    def show(self):
        print('*** Show ***')
        for account_number in self.accounts_dict:
            account = self.accounts_dict[account_number]
            print('   Account number:', account_number)
            account.show()

    def withdraw(self):
        print('*** Withdraw ***')
        account_number = input('Please enter your account number: ')
        account_number = int(account_number)
        amount = input('Please enter the amount to withdraw: ')
        amount = int(amount)
        password = input('Please enter the password: ')
        account = self.accounts_dict[account_number]
        balance = account.withdraw(amount, password)
        if balance is not None:
            print('Withdrew:', amount)
            print('Your new balance is:', balance)

    def bank_info(self):
        print('Closed because of inflation')
        print('Address: 11 Igal Alon Street, Tel Aviv, Israel')
        print('Phone:  (972) 672-1585')
        print('We currently have', len(self.accounts_dict), 'account(s) open. And we are very rich!')
