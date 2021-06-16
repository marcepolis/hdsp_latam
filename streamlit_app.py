import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


st.write('Hello, world!')

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write('This is a test')

dbase = st.file_uploader("Pick a file")

st.success('Success message')

st.text_input('Enter some text')


def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))


