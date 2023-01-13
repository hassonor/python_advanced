# Main program for controlling a Bank made up of Accounts

# Bring in all the code of the Bank class
from bank import *

# Create an instance of the Bank
swissBank = Bank()

# Main code
# Create two test accounts
hasson_account_number = swissBank.create_account('OrHasson', 100, '12345')
print("Or Hasson first account account number is:", hasson_account_number)

another_hasson_account_number = swissBank.create_account('OrHasson2', 12345, '12345')
print("Or Hasson second account  account number is:", another_hasson_account_number)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()

    try:
        if action == 'b':
            swissBank.balance()

        elif action == 'c':
            swissBank.close_account()

        elif action == 'd':
            swissBank.deposit()

        elif action == 'i':
            swissBank.bank_info()

        elif action == 'o':
            swissBank.open_account()

        elif action == 's':
            swissBank.show()

        elif action == 'q':
            break

        elif action == 'w':
            swissBank.withdraw()

    except AbortTransaction as error:
        # Print out the text of the error message
        print(error)

print('Done')
