import streamlit as st
import pandas as pd

data = pd.read_csv("data/Automobile_data.csv")

st.title("Here's a simple app")

button_state = st.toggle("Render the data", False)

if button_state:
    st.dataframe(data)
