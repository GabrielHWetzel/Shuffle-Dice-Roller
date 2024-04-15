import random
import streamlit as st
import plotly.express as px


class Dice:

    def __init__(self, size):
        """Generates dice as a list"""
        self.dice = [i for i in range(1, size+1)]

    def roll_dice(self):
        size = len(self.dice)
        return self.dice[random.randint(0, size-1)]


def generate_dict(size):
    dictionary = {"values": [], "results": []}
    if size == 1:
        return {"values": 1, "results": 0}
    else:
        for i in range(1, size + 1):
            dictionary["values"].append(i)
            dictionary["results"].append(0)
        return dictionary


size_of_dice = st.number_input("Dice size", min_value=2)
amount_of_dice = st.number_input("Dice amount", min_value=1)
dice_rolled = 0

roll = st.button("Roll")

if roll:
    dice = Dice(size_of_dice)
    all_results = generate_dict(size_of_dice)
    while dice_rolled < amount_of_dice:

        # Rolls dice
        dice_result = dice.roll_dice()

        # Stores results to dictionary
        all_results["results"][dice_result-1] += 1

        dice_rolled += 1

    figure = px.bar(all_results,
                    x=all_results["values"], y=all_results["results"],
                    labels={"x": "Value", "y": "Results"},
                    range_y=(0,amount_of_dice))
    st.plotly_chart(figure)


if __name__ == "__main__":
    print("its main")
