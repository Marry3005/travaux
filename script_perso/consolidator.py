import os
import pandas as pd

def load_stock_files(directory):
    """Charge les fichiers CSV depuis un répertoire donné et les consolide.
        PRE :
            - Vérification que le répertoire spécifié existe.
            - Vérification que le répertoire contient des fichiers CSV valides.

        POST :
            - Retourne un DataFrame consolidé contenant toutes les données des fichiers CSV.
            - Si des fichiers sont trouvés et chargés correctement, retourne un DataFrame consolidé.

        RAISE :
            - `FileNotFoundError` : Si le répertoire n'existe pas ou si aucun fichier CSV n'est trouvé dans le répertoire.
            - `ValueError` : Si aucun fichier CSV valide n'a été chargé.
            - `Exception` : Si une erreur inattendue survient pendant la lecture des fichiers CSV ou la consolidation.
    """
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Le répertoire '{directory}' n'existe pas.")

        all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

        if not all_files:
            raise FileNotFoundError(f"Aucun fichier CSV trouvé dans le répertoire '{directory}'.")

        # Lire chaque fichier CSV et créer une liste de DataFrames.
        dataframes = [pd.read_csv(file) for file in all_files]

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
    """Sauvegarde le DataFrame consolidé dans un fichier CSV.
        PRE :
            - Vérification que le DataFrame passé en argument contient des données valides.
            - Vérification que le chemin vers le fichier de sortie est valide.

        POST :
            - Sauvegarde le DataFrame consolidé dans le fichier spécifié.
            - Confirme la réussite de la sauvegarde par un message.

        RAISE :
            - `PermissionError` : Si le fichier de sortie ne peut être écrit à cause d'un problème de permission.
            - `FileNotFoundError` : Si le répertoire pour sauvegarder le fichier n'existe pas.
            - `Exception` : Si une erreur inattendue survient pendant la sauvegarde du fichier.

    """
    try:
        dataframe.to_csv(output_file, index=False)
        print(f"Le fichier consolidé a été sauvegardé dans {output_file}.")

    except PermissionError as e:
        print(f"Erreur de permission : Impossible d'écrire dans le fichier '{output_file}'. {e}")
    except FileNotFoundError as e:
        print(f"Erreur : Le répertoire pour sauvegarder le fichier '{output_file}' n'a pas été trouvé. {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la sauvegarde du fichier : {e}")

