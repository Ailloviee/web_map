import folium
import pandas

# load data from file using pandas
data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
# store latitude, longitude and elevation into lists
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# from folium, creating a map based on location and set zooming and tiles
map = folium.Map(
    location=[41.983208, -114.021853], zoom_start=5, tiles="Stamen Terrain"
)
# create a feature group
fg_v = folium.FeatureGroup(name="Volcanoes")
# add objects to the feature group
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg_v.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            popup=folium.Popup(iframe),
            fill_color=color_producer(el),
            color="grey",
            fill_opacity=0.7,
        )
    )

fg_p = folium.FeatureGroup(name="Population")
# add geojson object, which reads geo data from world.json file (the x in lambda represents features)
fg_p.add_child(
    folium.GeoJson(
        data=(open("Webmap_datasources/world.json", "r", encoding="utf-8-sig").read()),
        style_function=lambda x: {
            "fillColor": "yellow"
            if x["properties"]["POP2005"] < 10000000
            else "orange"
            if 10000000 <= x["properties"]["POP2005"] < 20000000
            else "red"
        },
    )
)
# add the feature groups to the map
map.add_child(fg_v)
map.add_child(fg_p)
# add layer control to the map (this allows control for feature groups)
map.add_child(folium.LayerControl())
# convert the map object to a html file
map.save("Map1.html")
