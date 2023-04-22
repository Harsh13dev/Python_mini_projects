import pandas as pd
import folium as fo
import matplotlib_inline

map = fo.Map()

population = pd.read_csv('us cities pop.csv')
lat_po = list(population['lat'])
lon_po = list(population['lon'])
name_po = list(population['name'])
pop_po = list(population['pop'])

po = fo.FeatureGroup(name='My Map')


def mar(popu):
    if popu > 30000:
        return 'red'
    elif (popu > 10000) and (popu <= 35000):
        return 'blue'
    else:
        return 'green'


for lat, lon, name, pop in zip(lat_po, lon_po, name_po, pop_po):
    po.add_child(fo.Marker(location=[lat, lon], popup=[pop, name], icon=fo.Icon(color=mar(pop))))

# po.add_child(fo.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(po)

map.show_in_browser()
