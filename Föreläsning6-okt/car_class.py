# Miniövning 1

# Skapa en klass Car med attribut brand och speed
# Skriv metoderna: accelerate() som ökar farten med 10, 
# brake() som sänker farten med 10

class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10 # ökar farten med 10
        print(f"{self.brand} efter acceleration: {self.speed} km/h")

    def brake(self):
        self.speed -= 10 # sänker farten med 10
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} bromsar till {self.speed} km/h")

car1 = Car("Audi")
car2 = Car("Mercedes", 50)

car1.accelerate()
car1.brake()

car2.accelerate()
car2.brake()

