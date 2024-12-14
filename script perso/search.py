import pandas as pd

def search_stock(dataframe, column, value):
    """Recherche des éléments dans le stock selon une colonne et une valeur."""
    results = dataframe[dataframe[column].astype(str).str.contains(value, case=False, na=False)]
    print(results)
    return results