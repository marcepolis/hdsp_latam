import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.error('Enter all the data')


st.write('Hi! Welcome to the BMI calculator!')


weight=int(st.text_input('Enter your weight in kilograms'))

height=int(st.text_input('Enter your height in centimeters'))



#BMI CALCULATION
height=height/100
height=height*height

BMI=weight/height

>>> with st.spinner(text='Calculating your chunkyness'):
>>>     time.sleep(5)
>>>     st.success('Done')

st.success('Hooray!')

st.write('Your BMI is', BMI)



