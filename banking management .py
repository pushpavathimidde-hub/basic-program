from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_details(self):
        pass


class BankAccount(Person):
    total_accounts = 0

    def __init__(self, name, acc_number, balance):
        super().__init__(name)
        self.acc_number = acc_number
        self.__balance = balance

        BankAccount.total_accounts += 1

    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    
    def check_balance(self):
        print("Current Balance:", self.__balance)

    
    def display_details(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.acc_number)
        print("Name           :", self.name)
        print("Balance        :", self.__balance)

    
    @classmethod
    def show_total_accounts(cls):
        print("Total Accounts:", cls.total_accounts)

    
    @staticmethod
    def bank_rules():
        print("\n------ Bank Rules ------")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 10 AM - 5 PM")



class SavingsAccount(BankAccount):
    def __init__(self, name, acc_number, balance):
        super().__init__(name, acc_number, balance)

    def display_details(self):
        print("\nSavings Account")
        super().display_details()



class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_number = int(input("Enter Account Number: "))

        if acc_number in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        account = SavingsAccount(name, acc_number, balance)
        self.accounts[acc_number] = account

        print("Account created successfully.")

    def search(self):
        acc_number = int(input("Enter Account Number: "))

        if acc_number in self.accounts:
            return self.accounts[acc_number]

        print("Account not found.")
        return None

    def deposit(self):
        account = self.search()

        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)

    def withdraw(self):
        account = self.search()

        if account:
            amount = float(input("Enter Withdrawal Amount: "))
            account.withdraw(amount)

    def display(self):
        account = self.search()

        if account:
            account.display_details()

    def balance(self):
        account = self.search()

        if account:
            account.check_balance()



bank = Bank()

while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Check Balance")
    print("6. Bank Rules")
    print("7. Total Accounts")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    elif choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.deposit()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.display()

    elif choice == 5:
        bank.balance()

    elif choice == 6:
        BankAccount.bank_rules()

    elif choice == 7:
        BankAccount.show_total_accounts()

    elif choice == 8:
        print("Thank You! Visit Again.")
        break

    else:
        print("Invalid Choice. Please try again.")