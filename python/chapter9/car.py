class Car():
    def __init__(self, make, moedl, year):
        self.make = make
        self.model = moedl
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def icrement_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('this car has a'+str(self.battery_size)+'-KWH battery')

    def get_range(self):
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270
        print("this car can go "+str(self.range)+"kilometer")

    def upgrade_battry(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, moedl, year):
        super().__init__(make, moedl, year)
        self.battery = Battery()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_used_car = Car('lynco', '03', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(22000)
my_used_car.read_odometer()
my_used_car.icrement_odometer(100)
my_used_car.read_odometer()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battry()
my_tesla.battery.get_range()
