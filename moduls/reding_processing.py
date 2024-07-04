"""
This module defines functions to import files, process data, and make modifications.
"""

# Import libraries
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Function to import the file defined as a parameter.
    :param file_path: Path to the CSV file
    :return: DataFrame
    """
    print("\nReading the file: {}".format(file_path))
    df = pd.read_csv(file_path, sep=",")
    print(df.columns[:5])
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to clean the DataFrame by removing a series of columns.
    :param df: Input DataFrame
    :return: Cleaned DataFrame
    """
    print("\nRemoving some columns")
    keep = ["month", "state", "permit", "handgun", "long_gun"]
    try:
        df_clean = df[keep]
        print(df_clean.columns)
        return df_clean
    except KeyError as e:  # If a column is not found, show the error.
        print(e)
        return df


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to rename the column long_gun to longgun.
    :param df: Input DataFrame
    :return: DataFrame with renamed column
    """
    print("\nRenaming column longgun")
    modified_df = df.rename({"long_gun": "longgun"}, axis=1)  # Rename the column
    print(modified_df.columns)
    return modified_df


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to split the 'month' column into year and month.
    :param df: Input DataFrame
    :return: DataFrame with separated date information
    """
    print("\nSplitting month and year")
    df[['year', 'month']] = df['month'].str.split("-", expand=True).astype(int)
    print(df.head(5))
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to remove the 'month' column.
    :param df: Input DataFrame
    :return: DataFrame without the 'month' column
    """
    print("\nRemoving month column")
    df = df.drop(columns=['month'])
    print("First 5 rows:")
    print(df.head(5))
    print("\nColumns: ")
    print(df.columns)
    return df


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to group data by state.
    :param df: DataFrame grouped by year and state
    :return: DataFrame grouped by state with total values
    """
    state_grouped = df.groupby(by='state')[['permit', 'handgun', 'longgun']].sum().reset_index()
    print(state_grouped.head(5))
    return state_grouped


def clean_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to remove the states of Guam, Mariana Islands, Puerto Rico, and Virgin Islands.
    :param df: DataFrame grouped by states
    :return: DataFrame without the removed states
    """
    print("\nRemoving states")
    to_remove = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]

    present = set()
    not_present = set()

    for s in to_remove:
        if s in set(df.state):
            present.add(s)
        else:
            not_present.add(s)

    print("\nStates found in the DataFrame: {}".format(present))
    if len(not_present) > 0:
        print("States not present in the DataFrame: {}".format(not_present))

    print("\nBefore removing states, there are {} states detected".format(df['state'].nunique()))
    df_clean = df[~df['state'].isin(present)]
    print("\nAfter removing states, there are {} states left".format(df_clean['state'].nunique()))

    return df_clean


def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the two datasets received as parameters based on the state column.
    :param df1: First dataset
    :param df2: Second dataset
    :return: Merged dataset
    """
    print("\nMerging dataframes")
    merged_df = df1.merge(df2, 'left', on='state')
    print(merged_df.head(5))
    return merged_df


def calculate_relative_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the relative values of permits, handguns, and longguns as percentages.
    :param df: Initial DataFrame
    :return: DataFrame with added percentage columns
    """
    print("\nCalculating relative values")
    df['permit_perc'] = df['permit'] * 100 / df['pop_2014']
    df['handgun_perc'] = df['handgun'] * 100 / df['pop_2014']
    df['longgun_perc'] = df['longgun'] * 100 / df['pop_2014']
    return df
