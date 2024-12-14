import os
import pandas as pd

def load_stock_files(directory):
    """Charge les fichiers CSV depuis un répertoire donné et les consolide."""
    all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

    # Lire chaque fichier CSV et créer une liste de DataFrames.
    dataframes = [pd.read_csv(file) for file in all_files]

    # Combine tous les DataFrames en un seul.
    return pd.concat(dataframes, ignore_index=True)

def save_consolidated_stock(dataframe, output_file):
    """Sauvegarde le DataFrame consolidé dans un fichier CSV."""
    dataframe.to_csv(output_file, index=False)

