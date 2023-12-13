from bank_exceptions import *

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    

    def deposit(self, amount):
            if amount < 0:
                raise NegativeAmountError(f"Amount cannot be negative: ${amount}")
            self.balance += amount
            return f"Balance: ${self.balance:.2f}"




    def get_balance(self):
        return f"Balance: ${self.balance:.2f}"



    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError(f"Amount cannot be negative: ${amount}")

        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. You tried to withdraw ${amount}, but your balance is only ${self.balance}.")
        self.balance -= amount
        return f"Balance: ${self.balance:.2f}"



if __file__ == "__main__":
    account1 = BankAccount(101,"Alice",1000)
    account2 = BankAccount(102,"Bob",500)
    while True:
        print("Welcome to the bank account system, you may we be of assistance")
        print("Choice 1: Deposit")
        print("Choice 2: Withdraw")
        print("Choice 3: Get Balance")
        print("Choice 4: Exit")
        choice = int(input("Select option (1/2/3/4):"))

        if choice == 1:
            dep = int(input("Please Enter a number to deposit: "))
            try:
                print(account1.deposit(dep))
            except NegativeAmountError as e:
                print(e)

        elif choice == 2:
            width = int(input("Please Enter a number to withdraw: "))
            try:
                print(account1.withdraw(width))
            except NegativeAmountError as e:
                print(e)

        elif choice == 3:
            print(account1.get_balance())
                
        elif choice == 4:
            print("Exiting")
            break
        else:
            print("Invalid choice")










