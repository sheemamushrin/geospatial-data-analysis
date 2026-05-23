import pandas as pd
import folium

# Load dataset
data = pd.read_csv('data/sample.csv')

# Create base map
map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers
for index, row in data.iterrows():
    folium.Marker(
        [row['Latitude'], row['Longitude']],
        popup=f"{row['Region']} - Sales: {row['Sales']}"
    ).add_to(map)

# Save map
map.save("sales_map.html")

print("Map generated successfully!")
