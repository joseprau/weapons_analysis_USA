import sys

# Import all functions from the modules as they will all be needed
from moduls.data_visualisation import *
from moduls.data_exploration import *
from moduls.reding_processing import *

def ex1():
    """
    Function to execute exercise 1
    :param :
    :return:
    """
    print("\n")
    print("#" * 50)
    print("Exercise 1")
    filename = "Data/nics-firearm-background-checks.csv"  # Define the file name
    import_df = read_csv(filename)  # Call function to import csv
    df = clean_csv(import_df)  # Call function to remove columns
    df = rename_col(df)  # Call function to rename columns
    return df


def ex2():
    """
    Function to execute exercise 2
    :param :
    :return:
    """
    df = ex1()
    print("\n")
    print("#" * 50)
    print("Exercise 2")
    df = breakdown_date(df)  # Call function to split month and year
    df = erase_month(df)  # Call function to remove month
    return df

def ex3():
    """
    Function to execute exercise 3
    :param :
    :return:
    """
    df = ex2()
    print("\n")
    print("#" * 50)
    print("Exercise 3")
    grouped = groupby_state_and_year(df)  # Call function to group by year and state
    print_biggest_handguns(grouped)  # Show state and year with the most handguns
    print_biggest_longguns(grouped)  # Show state and year with the most long guns


def ex4():
    """
    Function to execute exercise 4
    :return:
    """
    df = ex2()
    print("\n")
    print("#" * 50)
    print("Exercise 4")
    time_evolution(df, "graphs/")  # Call function to create a time evolution graph


def ex5():
    """
    Function to execute exercise 5
    :return:
    """
    df = ex2()
    print("\n")
    print("#" * 50)
    print("Exercise 5")
    grouped = groupby_state_and_year(df)  # Call function to group by year and state
    state_grouped = groupby_state(grouped)  # Call function to group by state
    clean = clean_state(state_grouped)  # Call function to remove states
    file_pops = "Data/us-state-populations.csv"  # Define the file path for the population data
    pops_df = read_csv(file_pops)  # Call function to import csv
    merged_df = merge_datasets(clean, pops_df)  # Call function to merge two dataframes
    perc_df = calculate_relative_value(merged_df)  # Call function to calculate relative values
    mean_permit_pct = perc_df['permit_perc'].mean()  # Calculate the average of permit_pct
    print("\nThe average permit_perc is %.2f" % mean_permit_pct)  # Display the average permit_perc
    kentucky = perc_df[perc_df['state'] == "Kentucky"]  # Select and display Kentucky data
    print(kentucky)  # Display Kentucky data
    perc_df.loc[perc_df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_pct  # Modify Kentucky's permit_perc
    mean_permit_pct_1 = perc_df['permit_perc'].mean()  # Recalculate the average
    print("\nThe average permit_perc after modification is %.2f" % mean_permit_pct_1)  # Display the new average
    return perc_df

def ex6():
    """"
    Function to execute exercise 6
    """
    df = ex5()
    print("\n")
    print("#" * 50)
    print("Exercise 6")
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )  # Define the URL with the JSON file containing state information
    state_geo = f"{url}/us-states.json"  # Define the file path for the JSON file
    metrics = ["permit_perc", "longgun_perc", "handgun_perc"]  # Define the metrics for which we want to obtain a map
    for m in metrics:  # Iterate over the metrics
        mapping_folium(df, m, state_geo, "graphs/")  # Call the function to create and save interactive maps


def all():
    """
    Function to execute all exercises at once.
    :return:
    """
    # Ex1
    print("\n")
    print("#" * 50)
    print("Exercise 1")
    filename = "Data/nics-firearm-background-checks.csv"  # Define the file name
    import_df = read_csv(filename)  # Call function to import csv
    df = clean_csv(import_df)  # Call function to remove columns
    df = rename_col(df)  # Call function to rename columns

    # Ex2
    print("\n")
    print("#" * 50)
    print("Exercise 2")
    df = breakdown_date(df)  # Call function to split month and year
    df = erase_month(df)  # Call function to remove month

    # Ex3
    print("\n")
    print("#" * 50)
    print("Exercise 3")
    grouped = groupby_state_and_year(df)  # Call function to group by year and state
    print_biggest_handguns(grouped)  # Show state and year with the most handguns
    print_biggest_longguns(grouped)  # Show state and year with the most long guns

    # Ex4
    print("\n")
    print("#" * 50)
    print("Exercise 4")
    time_evolution(df, "graphs/")  # Call the function to create a time evolution graph

    # Ex5
    print("\n")
    print("#" * 50)
    print("Exercise 5")
    state_grouped = groupby_state(grouped)  # Call function to group by state
    clean = clean_state(state_grouped)  # Call function to remove states
    file_pops = "Data/us-state-populations.csv"  # Define the file path for the population data
    pops_df = read_csv(file_pops)  # Call function to import csv
    merged_df = merge_datasets(clean, pops_df)  # Call function to merge two dataframes
    perc_df = calculate_relative_value(merged_df)  # Call function to calculate relative values
    mean_permit_pct = perc_df['permit_perc'].mean()  # Calculate the average of permit_pct
    print("\nThe average permit_perc is %.2f" % mean_permit_pct)  # Display the average permit_perc
    kentucky = perc_df[perc_df['state'] == "Kentucky"]  # Select and display Kentucky data
    print(kentucky)  # Display Kentucky data
    perc_df.loc[perc_df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_pct  # Modify Kentucky's permit_perc
    mean_permit_pct_1 = perc_df['permit_perc'].mean()  # Recalculate the average
    print("\nThe average permit_perc after modification is %.2f" % mean_permit_pct_1)  # Display the new average

    # Ex6
    print("\n")
    print("#" * 50)
    print("Exercise 6")
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )  # Define the URL with the JSON file containing state information
    state_geo = f"{url}/us-states.json"  # Define the file path for the JSON file
    metrics = ["permit_perc", "longgun_perc", "handgun_perc"]  # Define the metrics for which we want to obtain a map
    for m in metrics:  # Iterate over the metrics
        mapping_folium(perc_df, m, state_geo, "graphs/")  # Call the function to create and save interactive maps


def main(function_dict, ex):
    """
    Main function to execute if running as a program
    :param function_dict: Dictionary with the functions
    :param ex: Exercise to execute
    :return:
    """
    if ex.isdigit():  # Check that the number is a digit
        f = int(ex)  # Convert to int
        if f <= 6:
            if f > 0:
                print("Executing Exercise: {}".format(ex))
            else:
                print("Executing complete PAC.")
            function_dict[f]()  # Execute the function with key f
        else:
            print("Argument out of range. Value between [0, 6]")
            pass
    else:
        print("Non-numeric argument")  # If the value is not numeric, pass
        pass


if __name__ == "__main__":  # If running as the main program, execute the main function.
    arg = sys.argv[1]
    function_dict = {
        0: all,
        1: ex1,
        2: ex2,
        3: ex3,
        4: ex4,
        5: ex5,
        6: ex6
    }
    main(function_dict, arg)
