from random import randint

class BankAccount :
    
    min_balance = 0
    
    def __init__(self, balance, name, number, existing_account_numbers): #constructor -- Runs once when bot is created
        
        self.balance = balance
        self.balance = 0.00
        
        self.name = name
        
        self.number = number
        self.number = randint(1000,9999)
        
        # Again, this isn't neccessary, but if there were multiple users, 
        # this would prevent 2 users from having the same account number
        while True :
            if self.number in existing_account_numbers :
                self.number = randint(1000,9999)
            else :
                existing_account_numbers.append(self.number)
                break
    
    def deposit(self) :
        deposit_amount = 0
        
        while True :
            try :
                deposit_amount = float(input("\nHow much would you like to deposit?\n$"))
                
                if deposit_amount >= 0 :
                    self.balance += deposit_amount
                else :
                    raise ValueError
            except ValueError :
                print("\nPlease enter a positive amount of money.")
            else :
                break
    
    def withdraw(self) :
        withdraw_amount = 0.00
        while True :
            try : 
                withdraw_amount = float(input("\nHow much would you like to withdraw?\n$"))
                
                if withdraw_amount < self.balance :
                    
                    if withdraw_amount >= 0 :
                        self.balance -= withdraw_amount
                        
                    else :
                        raise ValueError
                    
                else :
                    print(f"Your balance isn't big enough to withdraw ${withdraw_amount}")
                    print(f"Current Balance: ${self.balance:,.2f}")
                    continue
            
            except ValueError:
                print("\nPlease enter a positive number.")
                
            else :
                break
        
    def view_account(account) :
        print(f"\nName: {account.name}\
            \nAccount Number: {account.number}\
            \nBalance: ${account.balance:,.2f}")
        
    def quit() :
        print("\nThank you for your business!")