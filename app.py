import streamlit as st
import pandas as pd
import datetime
import requests
import pydeck as pdk

'''
# Taxi Fare Calculator
'''

# map starting coords
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
    #st.markdown("## Expected fare:")
    st.write("${0:.2f}".format(prediction))



###
# Testing pdk
###

#view_state = pdk.ViewState(latitude=40.7614327, longitude=-73.9798156, zoom=10, bearing=0, pitch=0)
# view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=11, bearing=0, pitch=45)

# TRIPS_LAYER_DATA = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf.trips.json"  # noqa
# df = pd.read_json(TRIPS_LAYER_DATA)

# df["coordinates"] = df["waypoints"].apply(lambda f: [item["coordinates"] for item in f])
# df["timestamps"] = df["waypoints"].apply(lambda f: [item["timestamp"] - 1554772579000 for item in f])
# df["coordinates"] = [[-122.39079879999997, 37.7664413], [-122.3908298, 37.9664413]]
# df.drop(["waypoints"], axis=1, inplace=True)
# st.pydeck_chart(pdk.Deck(
#     map_style='mapbox://styles/mapbox/streets-v11',
#     initial_view_state=view_state,
#     layers = [pdk.Layer(
#         "TripsLayer",
#         df,
#         get_path="coordinates",
#         get_timestamps="timestamps",
#         get_color=[253, 128, 93],
#         opacity=0.8,
#         width_min_pixels=5,
#         rounded=True,
#         trail_length=600,
#         current_time=500,)]
# ))
###
# End testing pdk
###

st.map(data=map_loc,zoom=10)
