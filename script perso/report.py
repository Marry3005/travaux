import pandas as pd

def generate_report(dataframe, output_file):
    """Génère un rapport récapitulatif des stocks."""
    report = dataframe.groupby('catégorie').agg(
        total_quantité=('quantité', 'sum'),
        valeur_totale=('prix_unitaire', lambda x: (x * dataframe.loc[x.index, 'quantité']).sum())
    ).reset_index()
    report.to_csv(output_file, index=False)
    print(f"Rapport sauvegardé dans {output_file}.")