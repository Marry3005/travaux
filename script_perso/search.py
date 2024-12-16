import pandas as pd

def search_stock(dataframe, column, value):
    """Recherche des éléments dans le stock selon une colonne et une valeur."""
    try:
        # Vérifie que la colonne existe
        if column not in dataframe.columns:
            print(f"La colonne '{column}' n'existe pas dans le DataFrame.")
            return None

        #recherche éléments dans la colonne donnée
        results = dataframe[dataframe[column].astype(str).str.contains(value, case=False, na=False)]
        if results.empty:
            print(f"Aucun résultat trouvé pour la valeur '{value}' dans la colonne '{column}'.")
        else:
            print(f"Recherche effectuée pour {value} dans la colonne {column}")
            print(results)
        return results

    except KeyError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la recherche dans le stock : {e}")