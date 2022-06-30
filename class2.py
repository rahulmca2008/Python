class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default value

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer_reading(self,odometer_increment):
        self.odometer_reading = self.odometer_reading + odometer_increment

# inheritance


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")


if __name__ == "__main__":
    car1 = Car("Honda","Amaze",'2013')
    print(car1.odometer_reading)
    car1.odometer_reading = 20
    detail1 = car1.get_descriptive_name()
    print(detail1)
    print("Car1 odometer reading", car1.odometer_reading)
    car1.update_odometer_reading(30)
    print(car1.odometer_reading)
    tesla = ElectricCar('Tesla','model abc', 2019)
    detail2 = tesla.get_descriptive_name()
    print(tesla.battery_size)
    print(tesla.odometer_reading)
    tesla.describe_battery()
