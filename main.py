import streamlit as st
import plotly.express as px
import roller

roll_input = st.text_input("", placeholder="Ex: 1d6")
size_of_dice = st.number_input("Dice size", min_value=2)
amount_of_dice = st.number_input("Dice amount", min_value=1)

roll = st.button("Roll")

if roll:
    roller.interpreter(roll_input)

    # Class because in the future there can be multi rolls of different sizes happening
    dice = roller.MultiDice(size_of_dice, amount_of_dice)
    result = dice.list_rolls()
    st.info(result)


if __name__ == "__main__":
    # Testing area
    """
    all_results = multiroll.generate_dict()
    
    Alternative Option on generating dictionary, not sure how to make it work thou:
        dictionary = {}
        for i in range(1, self.dice.size + 1):
            print(i)
            dictionary[i] = 0
        print(dictionary)
        for i in self.all_results:
            dictionary[i] += 1
        print(dictionary)
        
    # Chart
    figure = px.bar(all_results,
                    x=all_results["values"], y=all_results["results"],
                    labels={"x": "Value", "y": "Results"},
                    range_y=(0, amount_of_dice))
    st.plotly_chart(figure)"""