import random
import re


class Dice:

    def __init__(self, size):
        """Generates dice as a list"""
        self.size = size
        self.dice = [i for i in range(1, size+1)]

    def roll(self):
        return self.dice[random.randint(0, self.size-1)]


class MultiDice(Dice):
    def __init__(self, times_to_roll, size):
        super().__init__(size)
        self.multi = times_to_roll
        self.all_results = []

    def list_rolls(self):
        for i in range(0, self.multi):
            result = self.roll()
            self.all_results.append(result)
        self.all_results.sort()
        return self.all_results

    def generate_dict(self):
        """ Generates dictionary with mapped values for graph display."""
        dictionary = {"values": [], "results": []}
        for i in range(1, self.size + 1):
            dictionary["values"].append(i)
            dictionary["results"].append(0)
        for i in self.all_results:
            dictionary["results"][i-1] += 1
        return dictionary


def interpreter(text: str):
    # Splits dice apart
    text_list = text.split("+")
    text_list = [text.strip() for text in text_list]
    print("Unfiltered text:", text_list)

    # Filters out the dice
    for i in text_list:
        pattern = re.compile("([0-9]+)[dD]([0-9]+)")
        # Dice is a tuple: (Amount to roll, Dice size)
        dice_set = re.findall(pattern, i)[0]
        print(dice_set)
        # Changes to int. Text is not valuable as of now
        dice_set = (int(dice_set[0]), int(dice_set[1]))
        print(dice_set)
        multi = MultiDice(dice_set[0], dice_set[1])
        print("Results are:", multi.list_rolls())
    pass


if __name__ == "__main__":
    # Testing area
    interpreter("2d10 + asdge1D10teststsad")
