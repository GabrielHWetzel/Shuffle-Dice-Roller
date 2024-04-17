import streamlit as st
import plotly.express as px
import roller

size_of_dice = st.number_input("Dice size", min_value=2)
amount_of_dice = st.number_input("Dice amount", min_value=1)
dice_rolled = 0

roll = st.button("Roll")

if roll:
    dice = roller.Dice(size_of_dice)
    if amount_of_dice > 1:
        multiroll = roller.Multiroll()
        all_results = multiroll.generate_dict(size_of_dice)
        while dice_rolled < amount_of_dice:

            # Rolls dice
            dice_result = dice.roll()

            # Stores results to dictionary
            all_results["results"][dice_result-1] += 1

            dice_rolled += 1
        figure = px.bar(all_results,
                        x=all_results["values"], y=all_results["results"],
                        labels={"x": "Value", "y": "Results"},
                        range_y=(0, amount_of_dice))
        st.plotly_chart(figure)
    else:
        result = dice.roll()
        result = str(result)
        st.info(result)

if __name__ == "__main__":
    print("its main")
