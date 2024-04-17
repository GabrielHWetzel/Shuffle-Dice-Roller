import streamlit as st
import plotly.express as px
import roller

size_of_dice = st.number_input("Dice size", min_value=2)
amount_of_dice = st.number_input("Dice amount", min_value=1)

roll = st.button("Roll")

if roll:
    dice = roller.Dice(size_of_dice)
    # Multi Roll Option
    if amount_of_dice > 1:
        # Class because in the future there can be multi rolls of different sizes happening
        multiroll = roller.Multiroll(dice, amount_of_dice)
        result = multiroll.roll()
        st.info(result)
        # Chart
        all_results = multiroll.generate_dict()
        figure = px.bar(all_results,
                        x=all_results["values"], y=all_results["results"],
                        labels={"x": "Value", "y": "Results"},
                        range_y=(0, amount_of_dice))
        st.plotly_chart(figure)

    # Single Dice Option
    else:
        result = dice.roll()
        result = str(result)
        st.info(result)

if __name__ == "__main__":
    # Testing area
    print("its main")
