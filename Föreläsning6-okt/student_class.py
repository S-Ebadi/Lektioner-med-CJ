# Miniövning 2
# Skapa en klass student med attribut name och points
 # Lägg till metoder, add_points(x), has_passed() som returnerar True
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

# Studenter
s1 = Student("Said")
s2 = Student("Sam", 45)
s3 = Student("Christian", 10)

# Addera poäng och kolla om studenten har klarat kursen
s1.add_points(30)
s1.add_points(25)
print(f"{s1.name} har klarat kursen: {s1.has_passed()}")

s2.add_points(10)
print(f"{s2.name} har klarat kursen: {s2.has_passed()}")

s3.add_points(35)   
print(f"{s3.name} har klarat kursen: {s3.has_passed()}")

