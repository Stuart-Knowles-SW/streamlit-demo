import streamlit as st
import pandas as pd

data = pd.read_csv("data/Automobile_data.csv")

st.title("Here's a simple app")

cols = st.columns([2, 2, 1, 1])
with cols[0]:
    render_data = st.toggle("Render the data", False)
with cols[1]:
    show_chart = st.toggle("Show the chart", False)
with cols[2]:
    st.button("Balloons", on_click=st.balloons)
with cols[3]:
    st.button("Snowflakes", on_click=st.snow)

if render_data:
    st.dataframe(data)

if show_chart:
    data["price"] = data["price"].where(data["price"] != "?", pd.NA).astype(float)
    chart_data = data.groupby("make").agg({"price": "mean"})
    st.bar_chart(chart_data)
