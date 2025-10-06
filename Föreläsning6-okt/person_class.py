class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Namn: {self.name} | Ålder: {self.age}"

    def greet(self):
        print(f"Hej, jag heter {self.name} och är {self.age} år gammal.")

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

p1 = Person("Said", 41)
p2 = Person("Sam", 37)
p3 = Person("Mika", 35)
p4 = Person("Levie", 27)

p1.greet()
p2.greet()
p3.greet()
p4.greet()

person_list = [p1, p2, p3, p4]

print(f"{p1.name} är {p1.age} år gammal.")

# range(x) = intervallet 0 upp till x
for i in range(len(person_list)):
    print(f"Person #{i+1}: {person_list[i]}")

for person in person_list:
    print(person)

new_name = input(f"Ange ett nytt namn för {p1.get_name()}: ")
p1.name = new_name
print(f"Nytt namn är {p1.name}")

new_name = input(f"Ange ett nytt namn för {p1.name}: ")
p1.change_name(new_name)
print(f"Nytt namn är", p1.get_name())

person_dict = {"Said": p1, "Sam": p2, "Mika": p3, "Levie": p4}