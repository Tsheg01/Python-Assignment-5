# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("The vehicle is moving.")

# Child classes with polymorphism
class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is Sailing 🚤")


# Create instances
vehicles = [
    Car("Toyota", "Corolla"),
    Plane("Boeing", "747"),
    Boat("Yamaha", "FX Cruiser")
]

# Loop through each vehicle and call the move() method
for v in vehicles:
    v.move()

