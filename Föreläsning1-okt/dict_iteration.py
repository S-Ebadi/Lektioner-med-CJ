int_list = [1, 5, 3, 7, 1]
#           0. 1. 2.

for elem in int_list:
    print(elem)

try: 
    index_to_check = int(input("Which index do you want to look up? "))
    print(int_list[index_to_check])
except IndexError:
    print("Index does not exist.")
except TypeError:
    print("Index has wrong data type.")
except ValueError:
    print("Invalid input. Please enter a number.")


print()

d = {"Said": 41, "Encro": 5}

print(d["Said"])
print(d["Encro"])

print()

for key in d:
    print(key)

print()

for val in d.values():
    print(val)

print()

for key, val in d.items():
    print(key, val)
    #print("Key:", key)
    #print("Value:", val)

name = input("Name to look up: ")
# Approach #1
age = d.get(name, "Could not find name") # Returns none if keys are missing

print(age)

# Approach #2
if name in d:
    print(d[name])
else:
    print(f"key {name} doesn't exist in dict.")

# Approach #3
while True:
    try:
        print(d[name])
        break
    except KeyError:
        print(f"Key {name} not in dict.")
        name = input("Please enter a new, existing name: ")

