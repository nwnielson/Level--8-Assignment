from random import randint


class BankAccount:

    # Creates min_balance which is shared among all Bank Accounts
    min_balance = 0

    # Creates each bank account
    def __init__(self, name, existing_account_numbers):

        self.name = name

        self.balance = 0.00
        self.number = randint(1000, 9999)

        # Again, this isn't neccessary, but if there were multiple users,
        # this would prevent 2 users from having the same account number
        while True:
            if self.number in existing_account_numbers:
                self.number = randint(1000, 9999)
            else:
                existing_account_numbers.append(self.number)
                break

    def deposit(self):
        deposit_amount = 0

        # Runs until valid input is given (not negative), or we get a weird error
        while True:
            try:
                
                deposit_amount = float(
                    input(
                        "\nHow much would you like to withdraw?\n"
                        f"Current Balance: ${self.balance:,.2f}\n"
                        "Withdrawl Amount: $"
                    )
                )

                # Checks that deposit_amount is not negative.
                if deposit_amount >= 0:
                    self.balance += deposit_amount

                else:
                    raise ValueError

            # If deposit_amount is negative, tells user to give positive amount of money.
            except ValueError:
                print("\nPlease enter a positive amount of money.")
                
            # If there's rando error, print message then return to menu.
            except:
                print("Unknown Error. Returning to menu.")
                break
            
            # Prints amounte entered and new balance, then returns to menu
            else:
                print(
                    f"\nDeposited ${deposit_amount:,.2f}.\n"
                    f"New Balance: ${self.balance:,.2f}"
                )
                break

    def withdraw(self):
        withdraw_amount = 0.00

        # Runs until valid input is given (not negative), or we get a weird error
        while True:
            try:
                withdraw_amount = float(
                    input(
                        "\nHow much would you like to withdraw?\n"
                        f"Current Balance: ${self.balance:,.2f}\n"
                        "Withdrawl Amount: $"
                    )
                )

                # Checks that withdraw_amount is less than the balance
                if withdraw_amount <= self.balance:

                    # Checks that withdraw_amount is not negative.
                    if withdraw_amount >= 0:
                        self.balance -= withdraw_amount

                    else:
                        raise ValueError

                # Prompts user to enter number smaller than current balance and displays balance, then continues
                else:
                    print(
                        f"\nYour balance isn't big enough to withdraw ${withdraw_amount:,.2f}"
                    )
                    print(f"Current Balance: ${self.balance:,.2f}")
                    continue

            # If withdraw_amount is negative, tells user to give positive amount of money.
            except ValueError:
                print("\nPlease enter a positive amount of money.")
                
            # If there's rando error, print message then return to menu.
            except:
                print("Unknown Error. Returning to menu.")
                break
            
            # Prints amounte entered and new balance, then returns to menu
            else:
                print(
                    f"\nWithdrew ${withdraw_amount:,.2f}.\n"
                    f"New Balance: ${self.balance:,.2f}"
                )
                break

    def view_account(self):
        # Prints Account Info
        print(f"\nName: {self.name}\
            \nAccount Number: {self.number}\
            \nBalance: ${self.balance:,.2f}")

    def quit():
        print("\nThank you for your business!")
