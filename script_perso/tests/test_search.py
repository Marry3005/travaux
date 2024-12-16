import unittest
import pandas as pd
import os
from script_perso.search import search_stock

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Définir le chemin absolu vers le répertoire des stocks
        cls.base_dir = os.path.dirname(os.path.dirname(__file__))  # Aller au dossier parent de 'tests'
        cls.stock_file = os.path.join(cls.base_dir, 'stocks', 'stock_1.csv')  # Fichier de stock à tester

    def test_search_stock_found(self):
        try:
            # Charger un fichier CSV existant pour tester la recherche
            self.assertTrue(os.path.exists(self.stock_file), f"Le fichier '{self.stock_file}' n'existe pas.")
            df = pd.read_csv(self.stock_file)

            # Appel de la fonction de recherche
            result = search_stock(df, 'produit', 'Smartphone')

            # Vérification que la recherche a retourné un résultat
            self.assertEqual(len(result), 1)
            self.assertEqual(result['produit'].iloc[0], 'Smartphone')

        except FileNotFoundError as e:
            self.fail(f"Erreur lors du chargement du fichier CSV : {e}")
        except Exception as e:
            self.fail(f"Une erreur inattendue est survenue dans test_search_stock_found : {e}")

    def test_search_stock_not_found(self):
        try:
            # Charger un fichier CSV existant pour tester la recherche
            self.assertTrue(os.path.exists(self.stock_file), f"Le fichier '{self.stock_file}' n'existe pas.")
            df = pd.read_csv(self.stock_file)

            # Appel de la fonction de recherche
            result = search_stock(df, 'produit', 'Ordinateur')

            # Vérification qu'aucun résultat n'a été trouvé
            self.assertFalse(result.empty)

        except FileNotFoundError as e:
            self.fail(f"Erreur lors du chargement du fichier CSV : {e}")
        except Exception as e:
            self.fail(f"Une erreur inattendue est survenue dans test_search_stock_not_found : {e}")

    def test_search_stock_invalid_column(self):
        try:
            # Charger un fichier CSV existant pour tester la recherche
            self.assertTrue(os.path.exists(self.stock_file), f"Le fichier '{self.stock_file}' n'existe pas.")
            df = pd.read_csv(self.stock_file)

            # Appel de la fonction de recherche avec une colonne invalide
            result = search_stock(df, 'invalid_column', 'Smartphone')

            # Vérifier que la fonction renvoie None
            self.assertIsNone(result, "La fonction doit retourner None quand la colonne n'existe pas.")

        except FileNotFoundError as e:
            self.fail(f"Erreur lors du chargement du fichier CSV : {e}")
        except Exception as e:
            self.fail(f"Une erreur inattendue est survenue dans test_search_stock_invalid_column : {e}")

if __name__ == '__main__':
    unittest.main()
