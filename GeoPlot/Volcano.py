import numpy as np
import pandas as pd
import folium as fo
import matplotlib_inline

map = fo.Map()

# Example-
# x = fo.FeatureGroup(name='My Map')
# x.add_child(fo.Marker(location=[40, -80], popup='hey', icon=fo.Icon(color='blue')))
# map.add_child(x)
#-------------------------------

volcano = pd.read_csv('volcano.csv')
lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])

vol = fo.FeatureGroup(name='My Map')

for lat, lon, name in zip(lat_vo, lon_vo, name_vo):
    vol.add_child(fo.Marker(location=[lat, lon], popup=name, icon=fo.Icon(color='red')))

vol.add_child(fo.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(vol)

map.show_in_browser()