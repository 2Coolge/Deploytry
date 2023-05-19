# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:16:07 2023

@author: Ahsan
"""

import streamlit as st
import pandas as pd

df = pd.read_csv('wellbore_exploration_all.csv', 
                  usecols=['wlbWellboreName', 'wlbNsDecDeg', 'wlbEwDesDeg'])

df.columns = ['Well Name', 'latitude', 'longitude']

import plotly.express as px

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", zoom=3)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", 
hover_name='Well Name', zoom=3)