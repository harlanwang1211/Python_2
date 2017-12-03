#骰子
from random import randint


class Die():
    '''扔骰子的简单尝试'''

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, times):
        i = 0
        while i < times:
            print(randint(1, self.sides))
            i += 1

num_one = Die(6)
num_one.roll_die(8)
