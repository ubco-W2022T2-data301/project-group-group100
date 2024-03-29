import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import geoplot as gplt

def create_world_map_happiness(date_year_data_frame_happiness, title):
    """
    Creates a heat world map based on happiness.
    date_year_data_frame_happiness(Dataframe) = Dataframe that is the year
    title(String) = The title of the plot
    
    Returns None
    """
    # Load the world map data
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Convert the projection of the world map to WGS84
    world = world.to_crs(epsg=4326)
    data = date_year_data_frame_happiness.groupby('Country')['Happiness Score'].mean().reset_index()

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

def region_barplot(DataAllRegion,column_name):
    region_data = DataAllRegion.groupby('Region').apply(lambda x: pd.Series({column_name: x[column_name].mean()})).reset_index()

    # Create a horizontal bar plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=column_name, y='Region', data=region_data, ax=ax)

    # Set the axis labels and title
    ax.set_xlabel(column_name, fontsize=16)
    ax.set_ylabel('Region', fontsize=16)
    ax.set_title(f'Mean {column_name} Score by Region from 2015-2022', fontsize=20)

    # Show the plot
    plt.show()

    return None
