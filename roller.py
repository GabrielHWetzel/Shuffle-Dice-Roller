import random


class Dice:

    def __init__(self, size):
        """Generates dice as a list"""
        self.dice = [i for i in range(1, size+1)]

    def roll(self):
        size = len(self.dice)
        return self.dice[random.randint(0, size-1)]


class Multiroll:
    def __init__(self):
        pass

    def generate_dict(self, size):
        dictionary = {"values": [], "results": []}
        for i in range(1, size + 1):
            dictionary["values"].append(i)
            dictionary["results"].append(0)
        return dictionary
