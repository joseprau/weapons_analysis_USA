"""
En aquest modul es creen les funcions d'ànalisi del dataframe
"""

import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per agrupar el dataframe per any i estat amb valors acumulats
    :param df:
    :return: dataframe agrupat per any i estat
    """
    grouped_ = df.groupby(by=['year', 'state']).sum().reset_index()
    return grouped_


def print_biggest_handguns(grouped_df: pd.DataFrame):
    """
    Pinta el nom de l'estat i l'any on s'ha registrat un nombre més gran de hand_guns
    :param grouped_df:
    :return: None
    """
    max_handgun = grouped_df.loc[grouped_df['handgun'].idxmax()]
    print("\nL'estat amb més hand_gun és {} a l'any {}.".format(max_handgun['state'], max_handgun['year']))


def print_biggest_longguns(grouped_df: pd.DataFrame):
    """
    Pinta el nom de l'estat i l'any on s'ha registrat un nombre més gran de longguns
    :param grouped_df:
    :return:
    """
    max_longgun = grouped_df.loc[grouped_df['longgun'].idxmax()]
    print("\nL'estat amb més hand_gun és {} a l'any {}.".format(max_longgun['state'], max_longgun['year']))
