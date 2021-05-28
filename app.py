import streamlit as st
import pandas as pd
import datetime
import requests

'''
# Taxi Fare Calculator
'''

pickup_lon = -73.9798156
pickup_lat = 40.7614327
dropoff_lon = -73.8803331
dropoff_lat = 40.6513111

date = st.sidebar.date_input("Pickup Date", datetime.date(2021,5,28))
time = st.sidebar.time_input("Pickup Time", datetime.time(13,0))
date_time = str(date) + " " + str(time)
pickup_lon = st.sidebar.number_input("Pickup Longitude", value=pickup_lon)
pickup_lat = st.sidebar.number_input("Pickup Latitude", value=pickup_lat)
dropoff_lon = st.sidebar.number_input("Dropoff Longitude", value=dropoff_lon)
dropoff_lat = st.sidebar.number_input("Dropoff Latitude", value=dropoff_lat)
passenger_count = st.sidebar.slider("Number of passengers",1,5)

map_loc = pd.DataFrame({'lon': [pickup_lon, dropoff_lon], 'lat': [pickup_lat, dropoff_lat]},index=['pickup', 'dropoff'])

map_loc

st.map(data=map_loc,zoom=10)

url = 'https://taxifare.lewagon.ai/predict'

params = {"pickup_datetime": date_time,
          "pickup_longitude": pickup_lon,
          "pickup_latitude": pickup_lat,
          "dropoff_longitude": dropoff_lon,
          "dropoff_latitude": dropoff_lat,
          "passenger_count": passenger_count}


if st.button('Calculate fare!'):
    response = requests.get(url, params=params)
    prediction = response.json()['prediction']
    st.markdown("## Expected fare:")
    st.write(prediction)
