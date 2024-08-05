class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
class Car(Vehicle):
    def get_brand(self):
        print(self.brand)
    def get_colour(self):
        print(self.colour)
x=Car("BMW","Brown")
x.get_brand()
x.get_colour()
#
class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
class Fuel:
    def fuel(self):
        print("Petrol")
class Car(Vehicle,Fuel):
    def get_brand(self):
        print(self.brand)
    def get_colour(self):
        print(self.colour)
x=Car("BMW","Brown")
x.get_brand()
x.get_colour()
x.fuel()
#
class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
class Car(Vehicle):
    def __init__(self,brand,colour,fuel):
        super().__init__(brand,colour)
        self.fuel=fuel
    def get_details(self):
        print(self.brand)
        print(self.colour)
        print(self.fuel)
x=Car("BMW","Brown","Petrol")
x.get_details()
#
class Vehicle:
    def __init__(self,brand,colour,type):
        self.brand=brand
        self.colour=colour
        self.type=type
class Bike(Vehicle):
    def get_bike(self):
        print(self.type)
class Car(Vehicle):
    def get_brand(self):
        print(self.brand)
    def get_colour(self):
        print(self.colour)
x=Car("BMW","Brown","Sports")
x.get_brand()
x=Bike("BMW","Brown","Sports")
x.get_bike()
#
class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
class Car(Vehicle):
    def get_brand(self):
        print(self.brand)
    def get_colour(self):
        print(self.colour)
class Fuel(Car):
    def get_fuel(self):
        print("Petrol")
x=Fuel("BMW","Brown")
x.get_brand()
x.get_colour()
x.get_fuel()
#
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
x=Vehicle("BMW")
print(x.brand)