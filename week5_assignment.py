#ACTIVITY 1
# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}% battery)"

# Inherited class (special smartphone type)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            self.battery -= 10
            print(f"Playing {game} on {self.brand} {self.model} 🎮. Battery now {self.battery}%")
        else:
            print("Battery too low! Please charge.")

    def __str__(self):
        return super().__str__() + f", Cooling: {self.cooling_system}"


# Example usage for ACTIVITY 1
phone = Smartphone("Samsung", "S21", 128)
print(phone)
phone.call("0712345678")
phone.charge(20)
print(phone)

gaming_phone = GamingPhone("Asus", "ROG Phone 5", 256, "Liquid Cooling")
print(gaming_phone)
gaming_phone.play_game("PUBG Mobile")
gaming_phone.play_game("Genshin Impact")
print(gaming_phone)

#ACTIVITY 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
