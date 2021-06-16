import streamlit as st
import pandas as pd


st.write('Hello, world!')

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write('This is a test')

death_db = pd.read_csv(file_uploader)

print('observations {0} and attributes {1}'.format(death_db.shape[0], (death_db.shape[1])))


