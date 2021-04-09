class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """getting full name of the car"""
        longname=(f'{self.year} {self.make} {self.model}')
        return longname.title()

class Battery():
    """defining the new battery class"""
    def __init__(self, battery_size=75, range='unknown'):
        self.battery_size=battery_size
        self.range = range
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        if self.battery_size==75:
            self.range=260
        elif self.battery_size==100:
            self.range=315
        print (f'This car can go about {self.range} miles on a full charge')

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.battery = Battery(self.battery_size)

my_tesla=ElectricCar('tesla','benz','2016', 75)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()