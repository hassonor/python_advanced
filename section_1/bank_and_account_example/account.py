# Account class

# Define a custom exception
class AbortTransaction(Exception):
    """raise this exception to abort a bank transaction"""
    pass


class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validate_amount(balance)
        self.password = password

    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer.')
        if amount <= 0:
            raise AbortTransaction('Amount must be a positive number.')
        return amount

    def check_password_match(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account.')

    def deposit(self, amount_to_deposit, password):
        self.check_password_match(password)
        amount_to_deposit = self.validate_amount(amount_to_deposit)
        self.balance = self.balance + amount_to_deposit
        return self.balance

    def withdraw(self, amount_to_withdraw, password):
        self.check_password_match(password)
        amount_to_withdraw = self.validate_amount(amount_to_withdraw)
        if amount_to_withdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')

        self.balance = self.balance - amount_to_withdraw
        return self.balance

    def get_balance(self, password):
        self.check_password_match(password)
        return self.balance

    # Added for debugging
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()
