import folium
import pandas as pd

m = folium.Map(location=[36, -95], zoom_start=10)

fg_places = folium.FeatureGroup(name = "Places")

folium.Marker(location= [39.8283, -98.5795], popup="US", icon=folium.i|con.Icon(color='blue')).add_to(fg_places)
folium.Marker(location= [30.5595, -22.9375], popup ="South Africa", icon = folium.Icon(color='green')).add_to(fg_places)
folium.Marker(location= [36.2048, 138.2529], popup="Japan", icon=folium.Icon(color='green')).add_to(fg_places)
folium.Marker(location= [54.5260, 15.2551], popup="Europe", icon=folium.Icon(color='red')).add_to(fg_places)
folium.Marker(location= [14.2350, -51.9253], popup="Brazil", icon=folium.Icon(color='green')).add_to(fg_places)

places = [
    { 
        "name": "US",
        "location": [39.8283, -98.5795],
        "Compared to USD": "1 USD = 1 USD",
    },
    { 
        "name": "South Africa",
        "location": [30.5595, -22.9375],
        "Compared to USD": "1 USD = 18.00 ZAR",
    },
    { 
        "name": "Japan",
        "location": [36.2048, 138.2529],
        "Compared to USD": "1 USD = 110.00 JPY",
    },
    { 
        "name": "Europe",
        "location": [54.5260, 15.2551],
        "Compared to USD": "1 USD = 0.85 EUR",
    },
    { 
        "name": "Brazil",
        "location": [14.2350, -51.9253],
        "Compared to USD": "1 USD = 5.25 BRL",
    }
]
