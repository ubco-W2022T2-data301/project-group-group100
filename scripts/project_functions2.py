import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import geopandas as gpd
import geoplot as gplt


def create_world_map_happiness(date_year_data_frame_happiness, title):
    # Load the world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Convert the projection of the world map to WGS84
    world = world.to_crs(epsg=4326)
    data = date_year_data_frame.groupby('Country')['Happiness Score'].mean().reset_index()

    data.rename(columns={'Country': 'name'}, inplace=True)

    # Merge the Happiness data with the world map data
    world_data = world.merge(data, on='name', how='left')

    world_data['Happiness Score'] = world_data['Happiness Score'].map(data.set_index('name')['Happiness Score'])

    # Merge the Happiness data with the world map data
    world_data = world.merge(data, on='name', how='left')

    world_data['Happiness Score'].fillna(0, inplace=True)

    # Create the heatmap on the world map
    fig, ax = plt.subplots(figsize=(12, 4))
    world_data.plot(column='Happiness Score', cmap='flare', legend=True, ax=ax, vmin=0., vmax=10)
    ax.set_title(title, fontsize = 20)
    plt.show()
    
    return None