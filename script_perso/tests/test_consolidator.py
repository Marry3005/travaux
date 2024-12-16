import unittest
import pandas as pd
import os
from script_perso.consolidator import load_stock_files, save_consolidated_stock

class TestConsolidator(unittest.TestCase):

    def test_load_stock_files(self):
        # Définir le répertoire des fichiers CSV existants
        
        # Générer le chemin absolu vers le dossier stocks
        base_dir = os.path.dirname(os.path.dirname(__file__))  # Aller au dossier parent de 'tests'
        directory = os.path.join(base_dir, "stocks")  # Chemin absolu vers 'stocks'

        # Vérifier que le répertoire existe
        self.assertTrue(os.path.exists(directory), f"Le répertoire '{directory}' n'existe pas.")

        # Charger les fichiers CSV dans un DataFrame consolidé
        result = load_stock_files(directory)

        # Vérifier que les données ont été correctement consolidées
        self.assertIsNotNone(result, "La fonction load_stock_files a retourné None.")
        self.assertGreater(len(result), 0)  # Vérifier qu'il y a des données dans le DataFrame
        self.assertTrue('produit' in result.columns)  # Vérifier que la colonne "produit" existe

    def test_save_consolidated_stock(self):
        # Créer un DataFrame de test
        df = pd.DataFrame({
            'produit': ['Smartphone', 'T-shirt'],
            'catégorie': ['Électronique', 'Vêtements'],
            'quantité': [50, 200],
            'prix_unitaire': [300, 15]
        })

        # Définir le chemin du fichier de sortie
        output_file = "test_consolidated_output.csv"

        # Sauvegarder le DataFrame dans le fichier CSV
        save_consolidated_stock(df, output_file)

        # Vérifier que le fichier a bien été créé
        self.assertTrue(os.path.exists(output_file))

        # Lire le fichier sauvegardé et vérifier son contenu
        saved_df = pd.read_csv(output_file)
        self.assertEqual(len(saved_df), 2)
        self.assertEqual(saved_df['produit'].iloc[0], 'Smartphone')

        # Supprimer le fichier de sortie après le test
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
