"""
Aquest modul definieix les funcions per importar els arxius, processar les dades i realitzar
modificacions.
"""

# Importem llibreries
import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Funció per importar el fitxer definit com a parametre.
    :param file_path:
    :return: dataframe
    """
    print("\nLlegint el fitxer: {}".format(file_path))
    df = pd.read_csv(file_path, sep=",")
    print(df.columns[:5])
    return df


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per netejar el dataframe eliminant una serie de columnes
    :param df:
    :return: dataframe net
    """
    print("\nEliminant algunes columnes")
    keep = ["month", "state", "permit", "handgun", "long_gun"]
    try:
        df_clean = df[keep]
        print(df_clean.columns)
        return df_clean
    except KeyError as e:  # Si no troba alguna columna mostra l'error.
        print(e)
        return df


def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per canviar el nom de la columna long_gun a longgun
    :param df:
    :return: dataframe amb nom canviat
    """
    print("\nReanomenant columna longgun")
    modified_df = df.rename({"long_gun": "longgun"}, axis=1)  # Canviem el nom de la columna
    print(modified_df.columns)
    return modified_df


def breakdown_date(df:pd.DataFrame) -> pd.DataFrame:
    """
    Funció per dividir la columna 'month' en any i mes.
    :param df:
    :return: el dataframe amb la informació de la data dividida
    """
    print("\nSeparant mes i any")
    df[['year', 'month']] = df['month'].str.split("-", expand=True).astype(int)
    print(df.head(5))
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funcióper eliminar la columna 'month'
    :param df:
    :return: df sense la columna month
    """
    print("\nEliminant columna mes")
    df = df.drop(columns=['month'])
    print("Primeres 5 files:")
    print(df.head(5))
    print("\nColumnes: ")
    print(df.columns)
    return df


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per agrupar les dades només per estat
    :param df agrupat per any i estat
    :return: df agrupat per estat amb valors totals
    """
    state_grouped = df.groupby(by='state')[['permit', 'handgun', 'longgun']].sum().reset_index()
    print(state_grouped.head(5))
    return state_grouped


def clean_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció per eliminar els estats de Guam,Mariana Islands, Puerto Rico i Virgin Islands.
    :param df: agrupada per estats
    :return: df sense els estats eliminats
    """
    print("\nEliminant estats")
    a_eliminar = ["Guam", "Mariana Islands", "Puerto Rico", "Virgin Islands"]

    present = set()
    no_presents = set()

    for s in a_eliminar:
        if s in set(df.state):
            present.add(s)
        else:
            no_presents.add(s)

    print("\nEstats trobats en el dataframe: {}".format(present))
    if len(no_presents) > 0:
        print("Estats no presents en el dataframe: {}".format(no_presents))

    print("\nAbans d'eliminar els estats, s'han detectat {} estats".format(df['state'].nunique()))
    df_clean = df[~df['state'].isin(present)]
    print("\nDesprés d'eliminar els estats, queden {} estats".format(df_clean['state'].nunique()))

    return df_clean


def merge_datasets(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Fusiona els dos datasets rebuts com a parametres basats en columna state
    :param df1: primer dataset
    :param df2: segon dataset
    :return: conjunt fusionat
    """
    print("\nFusionant dataframes")
    merge_df = df1.merge(df2, 'left', on='state')
    print(merge_df.head(5))
    return merge_df


def calculate_relative_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula els valors relatius dels permisos, armes lleugeres i armes curtes en percentatge.
    :param df: Dataframe inicial
    :return df: Dataframe amb columnes de percentatges afegides

    """
    print("\nCalculant valors relatius")
    df['permit_perc'] = df['permit']*100/df['pop_2014']
    df['handgun_perc'] = df['handgun']*100/df['pop_2014']
    df['longgun_perc'] = df['longgun']*100/df['pop_2014']
    return df