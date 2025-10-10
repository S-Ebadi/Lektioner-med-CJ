# A tiny zoo, be nice to the animals and please don't feed them 🙂

# Inheritance / Arv: A class can inherit attributes and methods from another class

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def speak(self):
        print("Some sound")

    def describe(self):
        print(f"{self.name} has {self.legs} legs")

# Subclass/childclass
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 4)
    
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 4)
    
    def speak(self):
        print(f"{self.name} says: Meow!")

class Fish(Animal):
    # Fish should have zero legs
    def __init__(self, name):
        super().__init__(name, 0)

    def speak(self):
        print(f"{self.name} says: Blub blub!")

class Human(Animal):
    def __init__(self, name):
        super().__init__(name, 2)

def create_animal(animal_type, name):
    if animal_type == "dog":
        return Dog(name)
    elif animal_type == "cat":
        return Cat(name)
    elif animal_type == "fish":
        return Fish(name)
    elif animal_type == "human":
        return Human(name)
    else:
        return Animal(name, 4)  # Default animal with 4 legs

# Test the animals
some_animal = Animal("Roger", 5)
dog = Dog("Buddy")
cat = Cat("Jackan")
fish = Fish("Goldie")

print("=== Animal descriptions ===")
cat.describe()
dog.describe()
fish.describe()

print("\n=== Animal sounds ===")
fish.speak()
some_animal.speak()
dog.speak()
cat.speak()

# Interactive animal creator
print("\n=== Create your own animals ===")
animal_list = []
while True:
    animal_type = input("Which kind of animal? dog/cat/fish/human: ").lower()
    animal_name = input("What's their name? ")
    new_animal = create_animal(animal_type, animal_name)
    animal_list.append(new_animal)
    
    new_animal.describe()
    new_animal.speak()
    
    cont = input("Create another animal? (y/n): ").lower()
    if cont != 'y' and cont != 'yes':
        break

print(f"\nYou created {len(animal_list)} animals! Thanks for visiting the zoo! 🦁")

