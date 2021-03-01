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

def extract_data_0(data_0):
    return {
        "name1": data_0["results"][0]["name"],
        "name2": data_0["results"][1]["name"], 
        # "name3": data_0["results"][2]["name"],
        # "name4": data_0["results"][3]["name"], 
        # "name5": data_0["results"][4]["name"],
        # "business_status1": data_0["results"][0]["business_status"], 
        # "business_status2": data_0["results"][1]["business_status"], 
        # "business_status3": data_0["results"][2]["business_status"], 
        # "business_status4": data_0["results"][3]["business_status"], 
        # "business_status5": data_0["results"][4]["business_status"],
        # "opening_hours1": data_0["results"][0]["opening_hours"]["open_now"], 
        # "opening_hours2": data_0["results"][1]["opening_hours"]["open_now"], 
        # "Opening_hours3": data_0["results"][2]["opening_hours"]["open_now"], 
        # "opening_hours4": data_0["results"][3]["opening_hours"]["open_now"], 
        # "opening_hours5": data_0["results"][4]["opening_hours"]["open_now"],
        "rating1": data_0["results"][0]["rating"], 
        "rating2": data_0["results"][1]["rating"], 
        # "rating3": data_0["results"][2]["rating"], 
        # "rating4": data_0["results"][3]["rating"],
        # "rating5": data_0["results"][4]["rating"],
        # "user_ratings_total1": data_0["results"][0]["user_ratings_total"], 
        # "user_ratings_total2": data_0["results"][1]["user_ratings_total"], 
        # "user_ratings_total3": data_0["results"][2]["user_ratings_total"],
        # "user_ratings_total4": data_0["results"][3]["user_ratings_total"],
        # "user_ratings_total5": data_0["results"][4]["user_ratings_total"],
        "lat": data_0["results"][0]["geometry"]["location"]["lat"],
        "lat": data_0["results"][1]["geometry"]["location"]["lat"],
        # "lat3": data_0["results"][2]["geometry"]["location"]["lat"],
        # "lat4": data_0["results"][3]["geometry"]["location"]["lat"],
        # "lat5": data_0["results"][4]["geometry"]["location"]["lat"],
        "lng": data_0["results"][0]["geometry"]["location"]["lng"],
        "lng": data_0["results"][1]["geometry"]["location"]["lng"],
        # "lng3": data_0["results"][2]["geometry"]["location"]["lng"],
        # "lng4": data_0["results"][3]["geometry"]["location"]["lng"],
        # "lng5": data_0["results"][4]["geometry"]["location"]["lng"],        
        "vicinity1": data_0["results"][0]["vicinity"], 
        "vicinity2": data_0["results"][1]["vicinity"], 
        # "vicinity3": data_0["results"][2]["vicinity"], 
        # "vicinity4": data_0["results"][3]["vicinity"],
        # "vicinity5": data_0["results"][4]["vicinity"]

    }


restaurant_list = []

data_0 = extract_data_0(requests.get(url2, params={
    "location": lat_lng,
    "radius": 1000,
    "type": "restaurant",
    "key": api_key
    }).json())

restaurant_list.append(data_0) 
# pprint(restaurant_list)

# df = pd.DataFrame(restaurant_list).drop_duplicates()
# pprint(df)

df = pd.DataFrame(restaurant_list)
pprint(df)

fig = px.scatter_mapbox(df, lat="lat", lon="lng")

fig.show()




# # df_append_4.to_csv("data2.csv") 








