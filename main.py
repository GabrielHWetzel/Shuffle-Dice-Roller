import streamlit as st
import plotly.express as px
import roller

roll_input = st.text_input("", placeholder="Ex: 1d6")
size_of_dice = st.number_input("Dice size", min_value=2)
amount_of_dice = st.number_input("Dice amount", min_value=1)

roll = st.button("Roll")

if roll:
    result = roller.interpreter(roll_input)
    st.info(result)


if __name__ == "__main__":
    # Class because in the future there can be multi rolls of different sizes happening
    dice = roller.MultiDice(size_of_dice, amount_of_dice)
    result = dice.list_rolls()
    # Testing area
    """    # Chart
        figure = px.bar(results, y=results["results"],
                        labels={"x": "Value", "y": "Results"},
                        range_y=(0, amount_of_dice))
        st.plotly_chart(figure)"""