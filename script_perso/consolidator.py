import os
import pandas as pd

def load_stock_files(directory):
    """Charge les fichiers CSV depuis un répertoire donné et les consolide."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Le répertoire '{directory}' n'existe pas.")

        all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

        if not all_files:
            raise ValueError(f"Aucun fichier CSV trouvé dans le répertoire '{directory}'.")

        # Lire chaque fichier CSV et créer une liste de DataFrames.
        dataframes = []
        for file in all_files:
            try:
                df = pd.read_csv(file)
                dataframes.append(df)
            except pd.errors.ParserError as e:
                print(f"Erreur de parsing du fichier {file}: {e}")
                continue  # Ignore ce fichier et passe au suivant

        # Combine tous les DataFrames en un seul.
        if not dataframes:
            raise ValueError("Aucun fichier CSV valide n'a été chargé.")

        return pd.concat(dataframes, ignore_index=True)

    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors du chargement des fichiers : {e}")

def save_consolidated_stock(dataframe, output_file):
    """Sauvegarde le DataFrame consolidé dans un fichier CSV."""
    try:
        dataframe.to_csv(output_file, index=False)
        print(f"Le fichier consolidé a été sauvegardé dans {output_file}.")

    except PermissionError as e:
    print(f"Erreur de permission : Impossible d'écrire dans le fichier '{output_file}'. {e}")
    except FileNotFoundError as e:
    print(f"Erreur : Le répertoire pour sauvegarder le fichier '{output_file}' n'a pas été trouvé. {e}")
    except Exception as e:
    print(f"Une erreur inattendue est survenue lors de la sauvegarde du fichier : {e}")

