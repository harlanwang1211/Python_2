#<Python Crash Course> P153 9-6 冰淇淋小店
class Restaurant():

    """奇葩父类：饭店"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is now open!")

subway = Restaurant('subway', 'what?!')
subway.describe_restaurant()
subway.open_restaurant()

class IceCreacStand(Restaurant):

    '''子类：冰淇淋小店'''

    def __init__(self, restaurant_name, cuisine_type, flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = flavor

    def show_fucking_icecream(self):
        print(self.flavor)

shit = IceCreacStand('shit', 'damn', ['cafe', 'cholocate', 'apple', 'strawberry'])
shit.show_fucking_icecream()
