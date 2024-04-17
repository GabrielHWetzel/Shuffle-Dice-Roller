import random
import re


class Dice:
    def __init__(self, dice_size):
        """Generates dice as a list"""
        self.dice_size = dice_size

    def roll(self):
        """ Singular dice roll"""
        return random.randint(0, self.dice_size - 1)+1


class MultiDice(Dice):
    def __init__(self, roll_amount, dice_size):
        super().__init__(dice_size)
        self.roll_amount = roll_amount
        self.all_results = []

    def list_rolls(self):
        """Rolls a number of times and stores rolls as a list"""
        for i in range(0, self.roll_amount):
            result = self.roll()
            self.all_results.append(result)
        return self.all_results

    def generate_dict(self):
        """ Generates dictionary with mapped values for graph display."""
        dictionary = {"values": [], "results": []}
        for i in range(1, self.dice_size + 1):
            dictionary["values"].append(i)
            dictionary["results"].append(0)
        for i in self.all_results:
            dictionary["results"][i-1] += 1
        return dictionary


def interpreter(text: str):
    # Splits Dice and Operations
    pattern = re.compile("[+-/*]")
    dice_list = re.split(pattern, text)
    dice_list = [i.strip() for i in dice_list]
    operation_list = re.findall(pattern, text)
    return dice_list, operation_list


def roll(text: str):
    dice_set, operation_set = interpreter(text)
    all_results = []

    # Filters out the dice and rolls
    for i in dice_set:
        # Dice is a tuple: (Amount to roll, Dice size)
        pattern = re.compile("([0-9]+)[dD]([0-9]+)")
        dice_set = re.findall(pattern, i)[0]
        print("Dice_set is:", dice_set)
        rest = re.split(pattern, i)
        rest = [i for i in rest if i not in dice_set and i != ""]
        print("The rest is:", rest)

        # Changes to int. Text is not valuable as of now
        dice_set = (int(dice_set[0]), int(dice_set[1]))
        print(dice_set)

        # Instantiates class and rolls
        multi = MultiDice(dice_set[0], dice_set[1])
        results = multi.list_rolls()
        print("Results are:", results)
        all_results.append(results)
    return all_results


if __name__ == "__main__":
    # Testing area
    roll("1d10 +asdge2D10teststsad* 3d10 - 4d10 / 5d10 , 6d10")
