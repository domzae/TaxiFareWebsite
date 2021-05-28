import streamlit as st
import datetime
import requests

'''
# Taxi Fare Calculator
'''

date = st.date_input("Pickup Date", datetime.date(2021,5,28))
time = st.time_input("Pickup Time", datetime.time(13,0))
date_time = str(date) + " " + str(time)
pickup_lon = st.number_input("Pickup Longitude",)
pickup_lat = st.number_input("Pickup Latitude",)
dropoff_lon = st.number_input("Dropoff Longitude",)
dropoff_lat = st.number_input("Dropoff Latitude",)
passenger_count = st.slider("Number of passengers",1,5)


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
