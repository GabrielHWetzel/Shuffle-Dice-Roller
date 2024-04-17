import random
import re


class Dice:

    def __init__(self, size):
        """Generates dice as a list"""
        self.size = size
        self.dice = [i for i in range(1, size+1)]

    def roll(self):
        return self.dice[random.randint(0, self.size-1)]


class Multiroll:
    def __init__(self, dice_to_roll, times_to_roll):
        self.dice = dice_to_roll
        self.multi = times_to_roll
        self.all_results = []

    def roll(self):
        for i in range(0, self.multi):
            result = self.dice.roll()
            self.all_results.append(result)
        self.all_results.sort()
        return self.all_results

    def generate_dict(self):
        """ Generates dictionary with mapped values for graph display.

        Alternative Option, not sure how to make it work thou:
        dictionary = {}
        for i in range(1, self.dice.size + 1):
            print(i)
            dictionary[i] = 0
        print(dictionary)
        for i in self.all_results:
            dictionary[i] += 1
        print(dictionary)"""
        dictionary = {"values": [], "results": []}
        for i in range(1, self.dice.size + 1):
            dictionary["values"].append(i)
            dictionary["results"].append(0)
        for i in self.all_results:
            dictionary["results"][i-1] += 1
        return dictionary


def interpreter(text: str):
    text_list = text.split("+")
    text_list = [text.strip() for text in text_list]
    print(text_list)
    for i in text_list:
        pattern = re.compile("([0-9]+)[dD]([0-9]+)")
        dice_set = re.findall(pattern, i)[0]
        print(dice_set)
    pass


if __name__ == "__main__":
    # Testing area
    dice = Dice(20)
    multi = Multiroll(dice, 10)
    multi.roll()
    multi.generate_dict()
