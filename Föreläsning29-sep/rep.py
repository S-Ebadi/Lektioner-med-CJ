# Variabler

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


