# Miniövning 3
# Bygg vidare på klassen BankAccount
# Lägg till metod, show_balance(), 
# Skapa två konton och testa deras metoder
# Skapa inloggning med lösenord
# Lägg till metod transfer_to(OtherAccount, amount)
# Testa genom att flytta pengar mellan två konton

class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__password = password
        self.is_logged_in = False

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if self.is_logged_in:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print("Successfully withdrew: ", amount)
            else:
                print("Invalid withdraw amount")
        else:
            print("User is not logged in")

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            print("Wrong password")
            return None
        
    def sign_in(self, password):
        if password == self.__password:
            print("Successfully logged in!")
            self.is_logged_in = True
        else:
            print("Wrong password")
            self.is_logged_in = False

                       
    def show_balance(self):
        if self.is_logged_in:
            print(f"{self.owner}s balance is: {self.__balance} SEK")
        else:
            print("User is not logged in")

    def transfer_to(self, other_account, amount):
        if amount > self.__balance:
            print("Insufficient funds for transfer")
        else:
           self.__balance -= amount
           other_account.__balance += amount
           print(f"Transferred {amount} SEK from {self.owner} to {other_account.owner}")


# Create bank accounts with passwords and initial balances
account1 = BankAccount("Said", "said123", 1000)
print("Saids current balance is", account1.get_balance("said123"))
account2 = BankAccount("Vincent", "visse123", 100)
print("Vincents current balance is", account2.get_balance("visse123"))

# Interactive login for both accounts
print("\n=== Login to Said's account ===")
password1 = input(f"Enter password for {account1.owner}: ")
account1.sign_in(password1)

print("\n=== Login to Vincent's account ===")
password2 = input(f"Enter password for {account2.owner}: ")
account2.sign_in(password2)  

# Use methods
account1.deposit(500)
account2.withdraw(50)

# Transfer money
account1.transfer_to(account2, 800)

# Show balanceself.__balance:
account1.show_balance()
account2.show_balance()

