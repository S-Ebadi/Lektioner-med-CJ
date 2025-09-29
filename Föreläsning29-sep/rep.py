# Variabler
'''
my_int = 15
my_num_str = "15"
my_input_num_str = input("Skriv in ett värde 1-20")


if my_input_num_str.isdigit():
    if 1 <= int(my_input_num_str) <= 20:
        my_sum = my_int + int(my_input_num_str)
        print(my_sum)
    else: 
        print("Rätt datatyp, men värdet är inte mellan 1-20")


else:
    print("Du måste skriva in en siffra")

my_product = my_int * int(my_input_num_str)
print(my_product)


# while-loopar

counter = 0
user_name = input("Your name: ")
run_loop = True
while run_loop == True:
    counter += 1
    print(f"Hi, {user_name}, counter valute: {counter}")
    if counter > 10:
        run_loop = False


counter2 = 0
repetitions = int(input("How many repetitions"))
while counter2 < repetitions:
    print(f"Hi, {user_name}, counter value: {counter2}")
    counter2 += 1
print("Loop over")


# Listor

person1 = "Said"
person2 = "Sam"
person3 = "Mika"
user_list = [person1, person2, person3]
#      index:    0        1        2

print(user_list)
print(user_list[0])  #Said

# for-loopar
for user in user_list:
    print(user)


x = input("How many repetitions: ")
# range = [0, 1, 2, 3, 4]
for i in range(int(x)):
    for j in range(3):
        print(f"Print count for {i}, #{j+1}")



user_info1 = ["Said", "840930", "Stockholm"]
user_info2 = ["Sam", "950101", "Göteborg"]
user_info3 = ["Mika", "990202", "Malmö"]    

user_data = [user_info1, user_info2, user_info3]
#            0            1           2
for user in user_data:
    for data in user:
        # print each user's data on one line
        print(data, end=" | ")
    print() # new line after each user

while True:
    add_new_user = input("Do you want to add a new user? (Y/N): ")
    if add_new_user.upper() == 'Y' or add_new_user.lower() == "yes":
        name = input("Enter name: ")
        pnr = input("Enter personal number: ")
        city = input("Enter city: ")
        new_user = [name, pnr, city]
        user_data.append(new_user)
        print("New user added.")
    elif add_new_user.upper() == 'N' or add_new_user.lower() == "no":
        print("No new user added. Exiting.")
        break
    else:
        print("Invalid input. Please enter Y or N.")
    
print("Alla användare:")
for user in user_data:
    print("Namn:", user[0])
    print("Personnummer:", user[1])
    print("Stad:", user[2])
    print()  # tom rad mellan användare

'''

def say_hello(user_name, extra_message=""): # function definition
    print(f"Hello user {user_name} - {extra_message}")
    name_length = len(user_name)
    return name_length

name = input("Enter your name: ")

len1 = say_hello(name, "Fett sexig") # Anrop av funktionen
print(f"Length of name is: {len1}")
len2 = say_hello("Alexander")
print(f"Length of name is: {len2}")
len3 = say_hello("Sam")
print(f"Length of name {name} is: {len3}")

def f(x):
    y = x + 1
    return y

def square(x):
    y = x * x
    return y

print(square(2))
print(square(3))
print(square(4))



