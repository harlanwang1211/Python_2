#P143页 9.2 连习所用代码
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

#测试数据
my_new_car = Car('audi', 'a4', 2016)
print (my_new_car.get_description_name())
my_new_car.increment_odometer(-6)
my_new_car.read_odometer()
