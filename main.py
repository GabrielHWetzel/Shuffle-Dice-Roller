import streamlit as st
import plotly.express as px
import roller

roll_input = st.text_input("Insert dice to roll:", placeholder="Ex: 1d6")

roll = st.button("Roll")

try:
    if roll and roll_input:
        result = roller.roll(roll_input)
        st.info(result)
    elif roll:
        st.info("No dice detected")
except IndexError:
    st.info("Dice roll error. Check if the syntax is correct.")

if __name__ == "__main__":
    # Testing area
    pass