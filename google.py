import pandas as pd
df = pd.read_csv("location.csv")
df
import googlemaps
gmaps_key = googlemaps.Client(key="AIzaSyDTDezluu996azBujFtLCkV-zJJ8V9rFCA")
df["LAT"]=None
df["LON"]=None

for i in range(0, len(df), 1):
    geocode_result = gmaps_key.geocode(df.iat[i,0])
    try:
        lat

    except:
