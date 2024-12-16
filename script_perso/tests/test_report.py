import unittest
import pandas as pd
import os
from script_perso.report import generate_report

class TestReport(unittest.TestCase):

    def test_generate_report(self):
        # Charger un fichier CSV existant pour tester la génération du rapport
        df = pd.read_csv('stocks/stock_1.csv')  # Assurez-vous que ce fichier existe

        # Définir le chemin du fichier de sortie pour le rapport
        report_file = "test_report_output.csv"

        # Générer le rapport
        generate_report(df, report_file)

        # Vérifier que le fichier rapport a été généré
        self.assertTrue(os.path.exists(report_file))

        # Lire le fichier rapport généré
        report_df = pd.read_csv(report_file)

        # Vérifier le contenu du rapport
        self.assertGreater(len(report_df), 0)
        self.assertTrue('catégorie' in report_df.columns)

        # Supprimer le fichier rapport après le test
        os.remove(report_file)

if __name__ == '__main__':
    unittest.main()
