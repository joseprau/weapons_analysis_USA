"""
Modul per a la visualització de dades. En aquest modul hi trobem les funcions per crear
mapes interactius i altres gràfiques
"""

import folium
import selenium
import pandas as pd
import matplotlib.pyplot as plt

def time_evolution(df: pd.DataFrame,directori):
    """
    Crea un gràfic de l'evoluciño temporal de les variables permit,hand_gun i long_gun
    :param df:
    :return:
    """

    grouped_year = df.groupby(by="year").sum().reset_index()  # Agrupem el df per any

    plt.figure(figsize=(10, 8))  # Definim el tamany de la figura

    # Creem les series
    plt.plot(grouped_year['year'], grouped_year['permit'], label="Permit")
    plt.plot(grouped_year['year'], grouped_year['handgun'], label="Handgun")
    plt.plot(grouped_year['year'], grouped_year['longgun'], label="Longgun")

    # Definim els titols dels eixos i del gràfic
    plt.xlabel("Any")
    plt.ylabel("Registres")
    plt.title("Evolució dels registres d'armes i llicències")

    # Mostrar les etiquetes dels anys
    plt.xticks(grouped_year['year'], rotation=45)

    plt.legend()
    plt.savefig(directori+"time_evolution.png")
    print("\n El gràfic evolutiu de l'exercici 4 es pot trobar a la carpeta {}".format(directori))


def maping_folium(df: pd.DataFrame, metric: str, states_info: str, directori: str):
    """
    Funció per crear mapes interactius usant folium. Exporta els fitxers a la carpeta imatges
    :param df: dataframe
    :param metric: columna amb els valors a representar
    :param states_info: fitxer .json amb la informacio dels estats
    :return: None
    """
    m = folium.Map(location=[40,-95],zoom_start=4)
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
    filename = directori+"{}_statesmap.html".format(metric)
    m.save(filename)
    print("El mapa de {} s'ha exportat correctament a la carpeta {}".format(metric, directori))