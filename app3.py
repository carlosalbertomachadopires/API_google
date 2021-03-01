import requests
import pandas as pd
from config import api_key
from config import mapbox_token
import plotly.express as px
px.set_mapbox_access_token(mapbox_token)
from pprint import pprint

url = "https://maps.googleapis.com/maps/api/geocode/json"

data = requests.get(url, params={
    "address": "University of Houston Downtow",
    "key": api_key
}).json()

# pprint(data)

results = data["results"]
# pprint(results)


array_first_elemments = data["results"][0]
# pprint(array_first_elemments)
lat = data["results"][0]["geometry"]["location"]["lat"]
# pprint(lat)

lng = data["results"][0]["geometry"]["location"]["lng"]
# pprint(lng)

lat_lng = str(lat) + "," + str(lng)
# pprint(lat_lng)

types = data["results"][0]["types"]
# pprint(types)

url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

data2 = requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
}).json()

# pprint(data2)

business_status = data2["results"][0]["business_status"]
# pprint(business_status)
name = data2["results"][0]["name"]
# pprint(name)
opening_hours = data2["results"][0]["opening_hours"]["open_now"]
# pprint(opening_hours)
# price_level = data2["results"][0]["price_level"]
# pprint(price_level)
rating = data2["results"][0]["rating"]
# pprint(rating)
user_ratings_total = data2["results"][0]["user_ratings_total"]
# pprint(user_ratings_total)
vicinity = data2["results"][0]["vicinity"]
# pprint(vicinity)

# pprint(results)

def extract_data_0(data_0):
    return {
        "name": data_0["results"][0]["name"],
        "business_status": data_0["results"][0]["business_status"],
        "opening_hours": data_0["results"][0]["opening_hours"]["open_now"],
        # "price_level": data_0["results"][0]["price_level"],
        "rating": data_0["results"][0]["rating"],
        "user_ratings_total": data_0["results"][0]["user_ratings_total"],
        "lat": data_0["results"][0]["geometry"]["location"]["lat"],
        "lng": data_0["results"][0]["geometry"]["location"]["lng"], 
        "vicinity": data_0["results"][0]["vicinity"]

    }

def extract_data_1(data_1):
     return {
        "name": data_1["results"][1]["name"],
        "business_status": data_1["results"][1]["business_status"],
        "opening_hours": data_1["results"][1]["opening_hours"]["open_now"],
        "price_level": data_1["results"][1]["price_level"],
        "rating": data_1["results"][1]["rating"],
        "user_ratings_total": data_1["results"][1]["user_ratings_total"],
        "lat": data_1["results"][1]["geometry"]["location"]["lat"],
        "lng": data_1["results"][1]["geometry"]["location"]["lng"],
        "vicinity": data_1["results"][1]["vicinity"]

    }   
 
def extract_data_2(data_2):
    return {
        "name": data_2["results"][2]["name"],
        "business_status": data_2["results"][2]["business_status"],
        # "opening_hours": data_2["results"][2]["opening_hours"]["open_now"],
        "price_level": data_2["results"][2]["price_level"],
        "rating": data_2["results"][2]["rating"],
        "user_ratings_total": data_2["results"][2]["user_ratings_total"],
        "lat": data_2["results"][2]["geometry"]["location"]["lat"],
        "lng": data_2["results"][2]["geometry"]["location"]["lng"],
        "vicinity": data_2["results"][2]["vicinity"]

    } 

def extract_data_3(data_3):
    return {
        "name": data_3["results"][3]["name"],
        "business_status": data_3["results"][3]["business_status"],
        "opening_hours": data_3["results"][3]["opening_hours"]["open_now"],
        "price_level": data_3["results"][3]["price_level"],
        "rating": data_3["results"][3]["rating"],
        "user_ratings_total": data_3["results"][3]["user_ratings_total"],
        "lat": data_3["results"][3]["geometry"]["location"]["lat"],
        "lng": data_3["results"][3]["geometry"]["location"]["lng"],
        "vicinity": data_3["results"][3]["vicinity"]

    }

def extract_data_4(data_4):
     return {
        "name": data_4["results"][4]["name"],
        "business_status": data_4["results"][4]["business_status"],
        "opening_hours": data_4["results"][4]["opening_hours"]["open_now"],
        "price_level": data_4["results"][4]["price_level"],
        "rating": data_4["results"][4]["rating"],
        "user_ratings_total": data_4["results"][4]["user_ratings_total"],
        "lat": data_4["results"][4]["geometry"]["location"]["lat"],
        "lng": data_4["results"][4]["geometry"]["location"]["lng"],
        "vicinity": data_4["results"][4]["vicinity"]

    }   


restaurant_list_0 = []
restaurant_list_1 = []
restaurant_list_2 = []
restaurant_list_3 = []
restaurant_list_4 = []

data_0 = extract_data_0(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list_0.append(data_0) 
# pprint(restaurant_list_0)

df = pd.DataFrame(restaurant_list_0).drop_duplicates()
# pprint(df)

data_1 = extract_data_1(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list_1.append(data_1) 
# pprint(restaurant_list_1)

df1 = pd.DataFrame(restaurant_list_1).drop_duplicates()
# pprint(df1)

data_2 = extract_data_2(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list_2.append(data_2) 
# pprint(restaurant_list_2)

df2 = pd.DataFrame(restaurant_list_2).drop_duplicates()
# pprint(df2)

data_3 = extract_data_3(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list_3.append(data_3) 
# pprint(restaurant_list_3)

df3 = pd.DataFrame(restaurant_list_3).drop_duplicates()
# # pprint(df3)

data_4 = extract_data_4(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list_4.append(data_4) 
# pprint(restaurant_list_4)

df4 = pd.DataFrame(restaurant_list_4).drop_duplicates()
# # pprint(df4)

df_append_1 = df.append(df1)
# pprint(df_append_1)
df_append_2 = df_append_1.append(df2)
# pprint(df_append_2)
df_append_3 = df_append_2.append(df3)
# pprint(df_append_3)
df_append_4 = df_append_3.append(df4)
pprint(df_append_4)

fig = px.scatter_mapbox(df_append_4, lat="lat", lon="lng", color="rating", size="user_ratings_total", color_continuous_scale=px.colors.cyclical.IceFire, size_max=30, zoom=15)

fig.show()





# # df_append_4.to_csv("data2.csv") 








