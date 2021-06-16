import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

st.write("wharap2")


DATA_URL = ("https://storage.googleapis.com/hdsp-data/CLUESBC.csv")

data = pd.read_csv(DATA_URL)


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

zoom_level=12
pintest=[32.6675696, -115.428741]

st.write("CLUES")
map(data,pintest[0], pintest[1],zoom_level)



