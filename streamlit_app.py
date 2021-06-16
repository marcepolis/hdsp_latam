import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.write("wharap1")


DATA_URL = (
    "https://storage.googleapis.com/hdsp-data/CLUESBC.csv"
)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data

# CREATING FUNCTION FOR MAPS

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/marcepolis/ckpyumfy918u818p8emehkc8f",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "clues-aloz28",
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



st.write("CLUES")
map(data, zoom_level)