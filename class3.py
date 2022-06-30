from class2 import Car, ElectricCar

# When you keep on adding the attributes of a class so why not define a seperate class and
# use that class instance as an attribute in another class

class Battery:
    def __init__(self,battery_size=60):
        """ To Initialize the battery's attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"battery size is {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size==60:
            range = 180
        elif self.battery_size==80:
            range = 250
        print(f"this car can go about {range} miles on a full charge")

class Tesla(ElectricCar): # CamelCase styling notation is used in class
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # object as an attribute
    def describe_battery(self): # method overriding
        print("This Tesla car having battery size: ",self.battery.battery_size)

tesla_car = Tesla('audi','model CVT',1985)
tesla_car.describe_battery()
tesla_car.battery.get_range()

# python standard library
from random import randint
print(randint(2,10))
from random import choice
players = ['sachin','sehwag','pathan','srikanth','dhoni']
chosen = choice(players)
print(chosen)
