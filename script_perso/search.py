import pandas as pd

def search_stock(dataframe, column, value):
    """Recherche des éléments dans le stock selon une colonne et une valeur.

        PRE :
            - Vérification que le DataFrame `dataframe` est bien chargé et contient des données.
            - Vérification que la colonne `column` existe dans le DataFrame.

        POST :
            - Si la colonne existe et que des résultats sont trouvés, ils sont retournés et affichés.
            - Si aucun résultat n'est trouvé, un message est affiché indiquant qu'aucun élément n'a été trouvé.
            - Si la colonne n'existe pas, un message est affiché pour indiquer l'absence de cette colonne.

        RAISE :
            - `KeyError` : Si une erreur se produit lors de l'accès aux colonnes du DataFrame (par exemple, si la colonne n'existe pas).
            - `Exception` : Si une autre erreur inattendue se produit durant la recherche, comme un problème avec les types de données ou d'autres erreurs liées à l'exécution de la recherche.
    """

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
        return None
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la recherche dans le stock : {e}")
        return None