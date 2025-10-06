'''
class person:
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

p1 = person("Said", 41)
p2 = person("Sam", 37)
p3 = person("Mika", 35)
p4 = person("Levie", 27)

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

# Miniövning 1

# Skapa en klass Car med attribut brand och speed
# Skriv metoderna: accelerate() som ökar farten med 10, 
# brake() som sänker farten med 10

class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} efter acceleration: {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} bromsar till {self.speed} km/h")

car1 = Car("Audi")
car2 = Car("Mercedes", 50)

car1.accelerate()
car1.brake()

car2.accelerate()
car2.brake()

'''

# Miniövning 2
# Skapa en klass student med attibut name och points
# Lägg till metoder, add_points(x), has passed() som returnerar True 
# om poängen hos ett Student objekt är >= 50

class Student:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def add_points(self, x):
        self.points += x
        print(f"{self.name} har nu {self.points} poäng")

    def has_passed(self):
        return self.points >= 50

student1 = Student("Said")
student2 = Student("Sam", 45)

student1.add_points(30)
student1.add_points(25)
print(f"{student1.name} har klarat kursen: {student1.has_passed()}")

student2.add_points(10)
print(f"{student2.name} har klarat kursen: {student2.has_passed()}")






