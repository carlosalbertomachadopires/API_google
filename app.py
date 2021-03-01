import requests
import pandas as pd
from config import api_key
from pprint import pprint

url = "https://maps.googleapis.com/maps/api/geocode/json"

data = requests.get(url, params={
    "address": "University of Texas",
    "key": api_key
}).json()

# pprint(data)
array_first_elemments = data["results"][0]
# pprint(array_first_elemments)
lat = data["results"][0]["geometry"]["location"]["lat"]
# pprint(lat)

lng = data["results"][0]["geometry"]["location"]["lng"]
# pprint(lng)

lat_lng = str(lat) + "," + str(lng)
# pprint(lat_lng)

url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

restaurants = ["Taco Cabana", "The University of Texas Club", "Texas Athletics Nutrition Center", "Chick-fil-A", "Zen"]

restaurant_list = []

for restaurant in restaurants:
    data_nearby = requests.get(url=url2, params={
    "location": lat_lng,
    "key": api_key,
    "radius": "300",
    "type": "restaurant"
    }).json()

    restaurant_list.append(data_nearby)
# pprint(restaurant_list)

df = pd.DataFrame(restaurant_list)
df = pd.json_normalize(restaurant_list, "results")
df.to_csv("data.csv")
pprint(df)

# restaurants = data_nearby["results"]

# pprint(restaurants)