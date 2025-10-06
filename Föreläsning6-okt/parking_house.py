from car_class import Car

class ParkingHouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []  # lista för att hålla reda på parkerade bilar

    def park_car(self, car):
        if len(self.cars) < self.capacity:
            self.cars.append(car)
            print(f"{car.brand} parkerad. Totalt antal bilar: {len(self.cars)}")
        else:
            print("Parkeringshuset är fullt!")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car.brand} har lämnat parkeringshuset. Totalt antal bilar: {len(self.cars)}")
        else:
            print(f"{car.brand} finns inte i parkeringshuset.")