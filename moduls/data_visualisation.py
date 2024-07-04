"""
Module for data visualization. In this module, we find functions to create
interactive maps and other graphs.
"""

import folium
import selenium
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image


def time_evolution(df: pd.DataFrame, directory: str):
    """
    Creates a graph of the time evolution of the variables permit, handgun, and longgun.
    :param df: DataFrame containing the data
    :param directory: Directory to save the graph
    :return: None
    """

    grouped_year = df.groupby(by="year").sum().reset_index()  # Group the df by year

    plt.figure(figsize=(8, 6))  # Define the size of the figure

    # Create the series
    plt.plot(grouped_year['year'], grouped_year['permit'], label="Permit")
    plt.plot(grouped_year['year'], grouped_year['handgun'], label="Handgun")
    plt.plot(grouped_year['year'], grouped_year['longgun'], label="Longgun")

    # Define the axis titles and the graph title
    plt.xlabel("Year")
    plt.ylabel("Registrations")
    plt.title("Evolution of weapon and license registrations")

    # Show the year labels
    plt.xticks(grouped_year['year'], rotation=45)

    plt.legend()
    plt.savefig(directory + "time_evolution.png")
    print("\nThe evolutionary graph for exercise 4 can be found in the folder {}".format(directory))


def mapping_folium(df: pd.DataFrame, metric: str, states_info: str, directory: str):
    """
    Function to create interactive maps using folium. Exports the files to the images folder
    :param df: DataFrame containing the data
    :param metric: Column with the values to represent
    :param states_info: .json file with the states information
    :param directory: Directory to save the map
    :return: None
    """
    m = folium.Map(location=[40, -95], zoom_start=4)
    folium.Choropleth(
        geo_data=states_info,
        name="choropleth",
        data=df,
        columns=['code', metric],
        key_on="feature.id",
        fill_color="YlGn",
        legend_name="{} by state".format(metric)
    ).add_to(m)
    folium.LayerControl().add_to(m)
    filename = directory + "{}_statesmap.png".format(metric)
    img_data = m._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(filename)
    print("The map of {} has been successfully exported to the folder {}".format(metric, directory))
