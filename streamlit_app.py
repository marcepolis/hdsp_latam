import streamlit as st
import pandas as pd


st.write('Hello, world!')

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write('This is a test')

dbase = st.file_uploader("Pick a file")

st.success('Success message')



