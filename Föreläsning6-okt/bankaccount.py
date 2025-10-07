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

    def transfer_to(self, other_account, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        else:
           self.balance -= amount
           other_account.balance += amount
           print(f"Transferred {amount} SEK from {self.owner} to {other_account.owner}")


# Create bank accounts
account1 = BankAccount("Said", 1000)
account2 = BankAccount("Christian", 100)

# Use methods
account1.deposit(0)
account2.withdraw(0)

# Transfer money
account1.transfer_to(account2, 800)

# Show balances
account1.show_balance()
account2.show_balance()

