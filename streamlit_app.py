import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


st.write('Hi! Welcome to the BMI calculator!')


weight=st.text_input('Enter your weight in kilograms')

height=st.text_input('Enter your height in centimeters')

#BMI CALCULATION

BMI=weight/(height)**


st.success('Hooray!')

st.write('Your BMI is' BMI)
