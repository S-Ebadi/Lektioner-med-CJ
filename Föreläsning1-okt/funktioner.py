'''
Förstå varför funktioner används.

Känna till syntaxen för att definiera och anropa funktioner.

Förstå parametrar, returvärden och scope.

Träna på att refaktorera kod med funktioner.
'''



# Nested strings:
print("This is a quote by Uncle Bob: \"Clean code is a code that is easy to read.\"")
print("This is a qoute by Uncle Bob: \'Clean code is a code that is easy to read.\'")

# Varför funktioner?
# Återanvändbarhet - Reusability
# Om vi har logik som används på flera ställen i koden

def greet(name): # Function definition
    if name.isalpha() == True:
        return f"Hello {name}!"
    else:
        print("Not a valid name")

def main():
    def read_user():
        return input("Name? ")
    name = read_user()
    greeting_message = greet(name)
    print(greeting_message)


# Enklare att läsa
def calculate_discount(price, rate):
    discounted_price = price * (1 - rate)
    return discounted_price

calculate_discount(100, 0.2)    
calculate_discount(120, 0.2)
calculate_discount(100, 0.4)
calculate_discount(140, 0.9)


# Testbarhet
def square(x):
    return x * x

def test_square():
    assert square(2) == 4
    assert square(10) == 100
    assert square(-3) == 9

test_square()
print()

# Undvika upprepning (DRY - Don't Repeat Yourself
def print_heading(text):
    print("="*len(text))
    print(text)
    print("="*len(text))

header_text1 = input("Enter a header text: ")
print_heading(header_text1)

header_text2 = input("Enter a header text: ")
print_heading(header_text2)



# Scope (Lokala variabler)
def f():
    x = 10 # Lokal variabel

y = 10 # Global variabel

# Modularisering)
'''
project/
        tasks/
            main.py
            helper.functions.py
'''


def say_hello(user_name, extra_message=""):
    print(f"Hello user {user_name} - {extra_message}")
    name_length = len(user_name)
    return name_length


def get_name_length(name):
    length = len(name)
    return length

name = input("Your name: ")

name1 = "Said"
len1 = say_hello(name1, "Vad fin du är!")
len1 = get_name_length(name1)
print(f"Length of name {name1} is {len1}")

name2 = "Encro"
say_hello(name2, "Du är snäll!")
len2 = len(name2)
print(f"Length of name {name2} is {len2}")

name3 = "Nero"
say_hello(name3)

print()
print("Hello world!")
print("Hello world again", end=", ")


def f(x):
    y = x * x
    return y

first_square = square(2)
second_square = square(3)
third_square = square(4)

print(first_square)

squared_square = square(square(first_square))

main()
