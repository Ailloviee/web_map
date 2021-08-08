import folium

# from folium, creating a map based on location and set zooming and tiles
map = folium.Map(
    location=[43.773291, -79.412817], zoom_start=10, tiles="Stamen Terrain"
)
# create a feature group
fg = folium.FeatureGroup(name="My Map")
# add objects to the feature group
for coordinates in [[43.773291, -79.412817], [44, -79]]:
    fg.add_child(
        folium.Marker(
            location=coordinates, popup="Test", icon=folium.Icon(color="green"),
        )
    )
# add the feature group to the map
map.add_child(fg)
# convert the map object to a html file
map.save("Map1.html")
