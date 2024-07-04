"""
In this module, functions for analyzing the dataframe are created.
"""

import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to group the dataframe by year and state with accumulated values
    :param df:
    :return: dataframe grouped by year and state
    """
    grouped_ = df.groupby(by=['year', 'state']).sum().reset_index()
    return grouped_


def print_biggest_handguns(grouped_df: pd.DataFrame):
    """
    Prints the name of the state and the year with the highest number of hand_guns registered
    :param grouped_df:
    :return: None
    """
    max_handgun = grouped_df.loc[grouped_df['handgun'].idxmax()]
    print("\nThe state with the most hand_guns is {} in the year {}.".format(max_handgun['state'], max_handgun['year']))


def print_biggest_longguns(grouped_df: pd.DataFrame):
    """
    Prints the name of the state and the year with the highest number of longguns registered
    :param grouped_df:
    :return: None
    """
    max_longgun = grouped_df.loc[grouped_df['longgun'].idxmax()]
    print("\nThe state with the most long_guns is {} in the year {}.".format(max_longgun['state'], max_longgun['year']))
