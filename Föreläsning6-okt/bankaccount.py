# Miniövning 3
# Bygg vidare på klassen BankAccount
# Lägg till metod, show_balance(), 
# Skapa två konton och testa deras metoder
# Lägg till metod transfer_to(OtherAccount, amount)
# Testa genom att flytta pengar mellan två konton

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}s balance is: {self.balance} SEK")

    
# Create bank accounts
account1 = BankAccount("Said", 1000)
account2 = BankAccount("Christian", 100)

# Use methods
account1.deposit(999000)
account2.withdraw(99)

# Show balances
account1.show_balance()
account2.show_balance()

