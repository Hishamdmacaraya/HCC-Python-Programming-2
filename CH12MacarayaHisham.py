'''
Python Programming 2: Chapter 10 Lab
Coder: Hisham D Macaraya
Date: 07.24.2024
Program Topic: Object-Oriented Programming, Classes, Objects, Inheritance
Program Name: Bank Account Inheritance Lab
Description: The Bank Account Inheritance Lab is a simple banking system using object-oriented programming. The `Account` class encapsulates fundamental account attributes, and the `CheckingAccount` class inherits from it, adding additional functionality. To manage multiple accounts and transactions, including deposits, withdrawals, and balance checks, the `Bank` class has been introduced. Additionally, the program has incorporated a feature to identify the account with the highest balance.
'''
class Account:
	def __init__(self, name="John Doe", AccountID="1234546", balance=0.0):
		self.name = name
		self.AccountID = AccountID
		self.balance = balance

	# Getter functions
	def get_name(self):
		return self.name

	def get_AccountID(self):
		return self.AccountID

	def get_balance(self):
		return self.balance

	# Setter functions
	def set_name(self, name):
		self.name = name

	def set_AccountID(self, AccountID):
		self.AccountID = AccountID

	def set_balance(self, balance):
		self.balance = balance

	# makeDeposit function
	def makeDeposit(self, amount):
		self.balance += amount

	# withdraw function
	def withdraw(self, amount):
		if amount > self.balance:
			print("insufficient funds")
		else:
			self.balance -= amount

	def display_account_info(self):
            print(f"{self.name:<15} {self.AccountID:<12} ${self.balance:<10.2f}")

class CheckingAccount(Account):
    FEE = 50.0  # Constant variable

    def __init__(self, name="John Doe", AccountID="1234546", balance=0.0, bonus=0.0):
        super().__init__(name, AccountID, balance)  # Call the superclass initializer
        self.bonus = bonus

    # Getter function for bonus
    def get_bonus(self):
        return self.bonus

    # Override makeDeposit function
    def makeDeposit(self, amount):
        self.balance += amount + self.bonus
        return self.balance

    # Override withdraw function
    def withdraw(self, amount):
        if self.balance < 500:
            self.balance -= self.FEE
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
        self.balance

    def display_account_info(self):
    # Includes bonus information
        print(f"{self.name:<15} {self.AccountID:<12} ${self.balance:<10.2f} ${self.bonus:<5}")

class Bank:
    def __init__(self):

        # Initialize the accounts list
        self.accounts = []
        
        # Creating account objects
        self.mike = Account("Mike", "T12564", 1250)
        self.john = CheckingAccount("John", "T52643", 256, 20)
        self.cecilia = CheckingAccount("Cecilia", "T24964", 5200, 50)

        # Adding account objects to the accounts list
        self.accounts.append(self.mike)
        self.accounts.append(self.john)
        self.accounts.append(self.cecilia)

    def display_all_account_info(self):
        print(f"{'Account Holder':<15} {'Account ID':<12} {'Balance':<10} {'Bonus':<5} {'Note':<70}")
        print("-" * 120)  # Adjust the length based on your column widths
        for account in self.accounts:
            note = f"This account belongs to {account.name}, has an account id of {account.AccountID}, and a balance of ${account.balance:.2f}."
            # Safely get 'bonus' attribute, default to 'N/A' if not present
            bonus = getattr(account, 'bonus', 'N/A')
            print(f"{account.name:<15} {account.AccountID:<12} ${account.balance:<10.2f} {bonus:<5} {note:<50}")

    def maxBalance(self):
        # Check if accounts list is not empty
        if not self.accounts:
            return None  # Return None if the list is empty

        # Initialize max_account with the first account in the list
        max_account = self.accounts[0]

        # Iterate through the accounts to find the one with the max balance
        for account in self.accounts[1:]:  # Start from the second element
            if account.balance > max_account.balance:
                max_account = account

        return max_account

    def main(self):
        #Welcome Message
        print("Welcome to the Bank of PY!\n")

        # Displaying initial account information for all accounts
        self.display_all_account_info()


        # Making deposits
        print("\nMaking deposits...")
        self.mike.makeDeposit(300)
        self.john.makeDeposit(400)

        # Withdrawing money
        print("\nWithdrawing money...")
        self.cecilia.withdraw(500)
		
        # Displaying Cecilia's bonus
        print(f"\nAccount holder, Cecilia, has a bonus of ${self.cecilia.bonus}.")

        # Displaying updated account information
        print("\nUpdated account information:")
        self.display_all_account_info()
        
        # Find the account with the maximum balance
        max_account = self.maxBalance()
        if max_account:
            print(f"\nThe account with the maximum balance is {max_account.get_name()} with a balance of ${max_account.get_balance():.2f}")
        else:
            print("No accounts found.")
        
        # Closing message
        print("\nThank you for banking with us!")

if __name__ == "__main__":
    bank = Bank()
    bank.main()

