import streamlit as st
st.write('Hello, world!')

x = st.slider('x')
st.write(x, 'squared is', x * x)

import pandas as pd

death_db = st.file_uploader("Pick a file")



print('observations {0} and attributes {1}'.format(death_db.shape[0], (death_db.shape[1])))

