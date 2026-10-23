"""Create a Python banking program for a customer who wants to manage a simple bank account.
Your program should ask the customer for their name and then create an account for them. You
may assign a random account #.

The account should begin with a balance of $0.00.

The customer should be able to:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit

When the customer makes a deposit, ask how much money they would like to add to the account.

When the customer makes a withdrawal, ask how much money they would like to withdraw. The
program should not allow the customer to withdraw more money than they currently have in the
account.

When the customer chooses to view account information, display: the customer’s name, account
number, and current balance.

If the customer enters an invalid menu choice, display an appropriate message and allow them to
try again. Continue displaying the menu until the customer chooses to quit.

Your program should use a BankAccount class to represent the customer’s account. Organize
your program into at least two Python files so that the class and the main program are separate.
"""

from BankFunctions import BankAccount

# This isn't neccessary for the assignment, but this list will hold account numbers so no 2 users have the same account #
existing_account_numbers = []

print("\nWelcome to CougarBank!\n")

# Gets and verifies name
account_name = input("Enter your name: ")
while True:
    answer = input(
        f"Verify your name. This information cannot be changed. \nIs this your name? '{account_name}' "
    )
    if answer.lower() == "yes":
        break
    elif answer.lower() == "no":
        account_name = input("Enter your name: ")
    else:
        print("Please enter yes or no.")

# Creates a new account
account = BankAccount(account_name, existing_account_numbers)

# While user wants to complete transactions, loop runs
while True:
    transaction_number = input("\nPlease choose an option: \
                            \n1. Make a deposit\
                            \n2. Make a withdrawal\
                            \n3. View account information\
                            \n4. Quit\n\n")

    try:
        if transaction_number not in "1,2,3,4":
            raise ValueError
        
    except ValueError:
        print("Please type a valid number (1-4)")
        
    # If transaction_number is 1-4, run checks to run the correct function
    else:
        if transaction_number == "1":
            balance = BankAccount.deposit(account)
        elif transaction_number == "2":
            balance = BankAccount.withdraw(account)
        elif transaction_number == "3":
            BankAccount.view_account(account)
        elif transaction_number == "4":
            BankAccount.quit()
            break
