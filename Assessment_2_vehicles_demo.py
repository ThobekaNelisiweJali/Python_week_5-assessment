# Activity 2: Polymorphism Challenge!

# Base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Define subclasses that override the move() method differently.
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Polymorphism: Iterate over a list of vehicles and call move()
print("\n=== Vehicle Movement Examples ===")
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()