import pandas as pd

def generate_report(dataframe, output_file):
    """Génère un rapport récapitulatif des stocks."""
    try:

        if 'catégorie' not in dataframe.columns or 'quantité' not in dataframe.columns or 'prix_unitaire' not in dataframe.columns:
            raise KeyError("Les colonnes nécessaires ('catégorie', 'quantité', 'prix_unitaire') sont manquantes dans le DataFrame.")

        report = dataframe.groupby('catégorie').agg(
            total_quantité=('quantité', 'sum'),
            valeur_totale=('prix_unitaire', lambda x: (x * dataframe.loc[x.index, 'quantité']).sum())
        ).reset_index()
        report.to_csv(output_file, index=False)
        print(f"Rapport sauvegardé dans {output_file}.")

    except KeyError as e:
        print(f"Erreur : {e}")
    except PermissionError as e:
        print(f"Erreur de permission : Impossible d'écrire dans le fichier '{output_file}'. {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la génération du rapport : {e}")