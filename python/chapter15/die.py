from random import randint


class Die:
    def __init__(self, numsize=6):
        self.numsize = numsize

    def roll(self):
        return randint(1, self.numsize)
