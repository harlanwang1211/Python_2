#P147 继承的练习
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        将里程表改为指定的值
        禁止将里程表读数往回调
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back an odometer !')

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cannot decrease the odometer!!!!")

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性,再初始化电动车特有的属性"""
        super().__init__(make, model, year)    #继承父类
        self.battery = Battery()

    def fill_gas_tank(self):
        print("The Electric Car doesn't have gas tank !")

class Battery():

    def __init__(self, battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + '-kWh battery.')

    def upgrade_battery(self):
        self.battery_size = 85

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        carrange = 0
        if self.battery_size == 70:
            carrange = 240
        elif self.battery_size == 85:
            carrange = 270

        message = "This car can go approximately " + str(carrange)
        message += " miles on a full charge."
        print(message)

#Testing Data
my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
