import pandas as pd

def carregar_arquivo():
    print("Abrindo o arquivo...")
    return pd.read_csv(filepath_or_buffer="data/base.csv", sep="|")