import streamlit as st
import pandas as pd
# Title of the app
st.title("Hello Title")

# Input fields for name and age
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

# Display user's name and age
if name and age:
    st.write(f"Your name is {name} and you are {age} years old.")
