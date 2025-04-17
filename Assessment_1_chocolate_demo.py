# Assignment 1: Design Your Own Class Using Chocolates as an Example

class Chocolate:
    def __init__(self, brand, cocoa_percentage, weight_grams):
        self.brand = brand
        self.cocoa_percentage = cocoa_percentage  # Cocoa content percentage
        self.weight_grams = weight_grams           # Weight in grams
        self.__secret_ingredient = "a pinch of magic"  # Private attribute to demonstrate encapsulation

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Cocoa Percentage: {self.cocoa_percentage}%")
        print(f"Weight: {self.weight_grams} grams")
        print("Secret Ingredient: " + self.get_secret_ingredient())

    def get_secret_ingredient(self):
        # Provides controlled access to the private attribute
        return self.__secret_ingredient


# Inheritance Example: Subclasses for specific chocolate brands

class LindtChocolate(Chocolate):
    def __init__(self, cocoa_percentage, weight_grams, flavor):
        # Lindt is a well-known brand, so we hardcode the brand name.
        super().__init__("Lindt", cocoa_percentage, weight_grams)
        self.flavor = flavor  # e.g., "Hazelnut", "Milk", "Dark"

    def display_info(self):
        # Call the base class display_info and then add Lindt-specific details.
        super().display_info()
        print(f"Flavor: {self.flavor}")
        print("-" * 40)


class CadburyChocolate(Chocolate):
    def __init__(self, cocoa_percentage, weight_grams, country_origin):
        # Cadbury is also well-known, so the brand is specified here.
        super().__init__("Cadbury", cocoa_percentage, weight_grams)
        self.country_origin = country_origin  # e.g., "UK", "India"

    def display_info(self):
        super().display_info()
        print(f"Country of Origin: {self.country_origin}")
        print("-" * 40)


# One more choice: a custom brand (for example, "Ghirardelli")
class GhirardelliChocolate(Chocolate):
    def __init__(self, cocoa_percentage, weight_grams, bar_style):
        super().__init__("Ghirardelli", cocoa_percentage, weight_grams)
        self.bar_style = bar_style  # e.g., "Squares", "Blocks"

    def display_info(self):
        super().display_info()
        print(f"Bar Style: {self.bar_style}")
        print("-" * 40)


# Demonstration of the classes:
if __name__ == "__main__":
    # Create instances of each subclass
    lindt = LindtChocolate(cocoa_percentage=70, weight_grams=100, flavor="Dark with Hazelnut")
    cadbury = CadburyChocolate(cocoa_percentage=45, weight_grams=150, country_origin="UK")
    ghirardelli = GhirardelliChocolate(cocoa_percentage=68, weight_grams=90, bar_style="Squares")

    # Display the information for each chocolate
    print("=== Chocolate Showcase ===\n")
    lindt.display_info()
    cadbury.display_info()
    ghirardelli.display_info()





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