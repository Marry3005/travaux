import unittest
import pandas as pd
import os
from script_perso.search import search_stock

class TestSearch(unittest.TestCase):

    def test_search_stock_found(self):
        # Charger un fichier CSV existant pour tester la recherche
        df = pd.read_csv('stocks/stock_1.csv')  # Assurez-vous que ce fichier existe

        # Appel de la fonction de recherche
        result = search_stock(df, 'produit', 'Smartphone')

        # Vérification que la recherche a retourné un résultat
        self.assertEqual(len(result), 1)
        self.assertEqual(result['produit'].iloc[0], 'Smartphone')

    def test_search_stock_not_found(self):
        # Charger un fichier CSV existant pour tester la recherche
        df = pd.read_csv('stocks/stock_1.csv')  # Assurez-vous que ce fichier existe

        # Appel de la fonction de recherche
        result = search_stock(df, 'produit', 'Ordinateur')

        # Vérification qu'aucun résultat n'a été trouvé
        self.assertTrue(result.empty)

    def test_search_stock_invalid_column(self):
        # Charger un fichier CSV existant pour tester la recherche
        df = pd.read_csv('stocks/stock_1.csv')  # Assurez-vous que ce fichier existe

        # Vérification que KeyError est levé
        with self.assertRaises(KeyError):
            search_stock(df, 'invalid_column', 'Smartphone')

if __name__ == '__main__':
    unittest.main()
