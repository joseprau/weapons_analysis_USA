import sys

# Importem totes les funcions dels arxius ja que faran falta totes
from moduls.data_visualisation import *
from moduls.data_exploration import *
from moduls.reding_processing import *

def ex1():
    """
    Funció per executar exercici 1
    :param :
    :return:
    """
    print("\n")
    print("#"*50)
    print("Exercici 1")
    filename = "Data/nics-firearm-background-checks.csv"  # Definim el nom del fitxer
    import_df = read_csv(filename)  # Cridem funcio per importar csv
    df = clean_csv(import_df)  # Cridem funció per eliminar columnes
    df = rename_col(df)  # Cridem funció per renombrar columnes
    return df


def ex2():
    """
    Funció per executar ex2
    :param :
    :return:
    """
    df = ex1()
    print("\n")
    print("#"*50)
    print("Exercici 2")
    df = breakdown_date(df)  # Cridem funcio per separar mes i any
    df = erase_month(df)  # Cridem funcio per eliminar mes
    return df

def ex3():
    """
    Funció per executar ex3
    :param :
    :return:
    """
    df = ex2()
    print("\n")
    print("#"*50)
    print("Exercici 3")
    grouped = groupby_state_and_year(df)  # Cridem funcio per agrupar per any i estat
    print_biggest_handguns(grouped)  # Mostrem estat i any amb més hand guns
    print_biggest_longguns(grouped)  # Mostrem estat i any amb més long gun


def ex4():
    """
    Funció per executar ex4
    :return:
    """
    df = ex2()
    print("\n")
    print("#"*50)
    print("Exercici 4")
    time_evolution(df, "grafiques/")  # Cridem la funció per crear un gràfic evolutiu


def ex5():
    """
    Funció per executar ex5
    :return:
    """
    df = ex2()
    print("\n")
    print("#"*50)
    print("Exercici 5")
    grouped = groupby_state_and_year(df)  # Cridem funcio per agrupar per any i estat
    state_grouped = groupby_state(grouped)  # Cridem funció per agrupar per estat
    clean = clean_state(state_grouped)  # Cridem funció per eliminar estats
    file_pops = "Data/us-state-populations.csv"  # Definim full_path de fitxer amb poblacions
    pops_df = read_csv(file_pops)  # Cridem funcio per importar csv
    merged_df = merge_datasets(clean, pops_df)  # Cridem funcio per fusionar dos dfs
    perc_df = calculate_relative_value(merged_df)  # Cridem funció per calcular els valors relatius
    mean_permit_pct = perc_df['permit_perc'].mean()  # Calculem la mitja de permit_pct
    print("\nLa mitjana de permit_perc %.2f" % mean_permit_pct)  # Mostrem per pantalla la mitja de permit_perc
    kentucky = perc_df[perc_df['state'] == "Kentucky"]  # Seleccionem i mostrem les dades de kentucky
    print(kentucky)  # Mostrem dades de kentucky
    perc_df.loc[perc_df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_pct  # Modifiquem permit_perc de kentucky
    mean_permit_pct_1 = perc_df['permit_perc'].mean()  # Calculem de nou la mitja
    print("\nLa mitjana de permit_perc després de la modificació és %.2f" % mean_permit_pct_1)  # Mostrem la mitja nova
    return perc_df

def ex6():
    """"
    Funció per executar ex6
    """
    df = ex5()
    print("\n")
    print("#"*50)
    print("Exercici 6")
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )  # Definim la URL amb el fitxer JSON amb informació dels estats
    state_geo = f"{url}/us-states.json"  # Definim el full_path del fitxer json
    metrics = ["permit_perc", "longgun_perc",
               "handgun_perc"]  # Definim les mètriques per les quals volem obtienir un mapa
    for m in metrics:  # Iterem per les mètriques
        maping_folium(df, m, state_geo, "grafiques/")  # Cridem la funció per crear i guardar els mapes interactius


def all():
    """
     Funció per executar tots els exercicis alhora.
     :return:
     """
    # Ex1
    print("\n")
    print("#"*50)
    print("Exercici 1")
    filename = "Data/nics-firearm-background-checks.csv"  # Definim el nom del fitxer
    import_df = read_csv(filename)  # Cridem funcio per importar csv
    df = clean_csv(import_df)  # Cridem funció per eliminar columnes
    df = rename_col(df)  # Cridem funció per renombrar columnes

    # Ex2
    print("\n")
    print("#"*50)
    print("Exercici 2")
    df = breakdown_date(df)  # Cridem funcio per separar mes i any
    df = erase_month(df)  # Cridem funcio per eliminar mes

    # Ex3
    print("\n")
    print("#"*50)
    print("Exercici 3")
    grouped = groupby_state_and_year(df)  # Cridem funcio per agrupar per any i estat
    print_biggest_handguns(grouped)  # Mostrem estat i any amb més hand guns
    print_biggest_longguns(grouped)  # Mostrem estat i any amb més long gun

    # Ex4
    print("\n")
    print("#"*50)
    print("Exercici 4")
    time_evolution(df, "grafiques/")  # Cridem la funció per crear un gràfic evolutiu

    # Ex5
    print("\n")
    print("#" * 50)
    print("Exercici 5")
    state_grouped = groupby_state(grouped)  # Cridem funció per agrupar per estat
    clean = clean_state(state_grouped)  # Cridem funció per eliminar estats
    file_pops = "Data/us-state-populations.csv"  # Definim full_path de fitxer amb poblacions
    pops_df = read_csv(file_pops)  # Cridem funcio per importar csv
    merged_df = merge_datasets(clean, pops_df)  # Cridem funcio per fusionar dos dfs
    perc_df = calculate_relative_value(merged_df)  # Cridem funció per calcular els valors relatius
    mean_permit_pct = perc_df['permit_perc'].mean()  # Calculem la mitja de permit_pct
    print("\nLa mitjana de permit_perc %.2f" % mean_permit_pct)  # Mostrem per pantalla la mitja de permit_perc
    kentucky = perc_df[perc_df['state'] == "Kentucky"]  # Seleccionem i mostrem les dades de kentucky
    print(kentucky)  # Mostrem dades de kentucky
    perc_df.loc[perc_df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_pct  # Modifiquem permit_perc de kentucky
    mean_permit_pct_1 = perc_df['permit_perc'].mean()  # Calculem de nou la mitja
    print("\nLa mitjana de permit_perc després de la modificació és %.2f" % mean_permit_pct_1)  # Mostrem la mitja nova

    # Ex6
    print("\n")
    print("#"*50)
    print("Exercici 6")
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )  # Definim la URL amb el fitxer JSON amb informació dels estats
    state_geo = f"{url}/us-states.json"  # Definim el full_path del fitxer json
    metrics = ["permit_perc", "longgun_perc",
               "handgun_perc"]  # Definim les mètriques per les quals volem obtienir un mapa
    for m in metrics:  # Iterem per les mètriques
        maping_folium(perc_df, m, state_geo, "grafiques/")  # Cridem la funció per crear i guardar els mapes interactius


def main(dictat, ex):
    """
    Funció principal per executar en cas de que s'executi com programa
    :param dictat: dictat amb les funcions
    :param ex: excercici per executar
    :return:
    """
    if ex.isdigit():  # Comprova que el número sigui digit
        f = int(ex)  # Converteix a int 
        if f <=6:
            if f > 0:
                print("Executant Ex: {}".format(ex))
            else:
                print("Executant PAC completa.")
            dictat[f]()  # Executa la funció amb key f
        else:
            print("Argument fora del rang. Valor entre [0, 6]")
            pass
    else:
        print("Argument no numèric")  # Si el valor no és numèric passa
        pass


if __name__ == "__main__":  # Si executem com a programa principal executa la funció main.
    arg = sys.argv[1]
    dictat_funcions = {
        0: all,
        1: ex1,
        2: ex2,
        3: ex3,
        4: ex4,
        5: ex5,
        6: ex6
    }
    main(dictat_funcions, arg)

