import argparse
import pandas as pd
from consolidator import load_stock_files, save_consolidated_stock
from search import search_stock
from report import generate_report

STOCK_SIRECTORY = "stocks"
OUTPUT_FILE = "consolidated_stock.csv"
REPORT_FILE = "stock_report.csv"

def main():
    try:
        parser = argparse.ArgumentParser(description="gestion consolider les stocks")
        parser.add_argument("--consolider", action="store_true", help="consolider fichier csv en base unique")
        parser.add_argument("--rechercher", nargs=2, metavar=("COLONNE", "VALEUR"), help="recherche dans le stock par colonne et valeur")
        parser.add_argument("--rapport", action="store_true", help="Générer un rapport récapitulatif des stocks")
        args = parser.parse_args()

        if args.consolider:
            dataframe = load_stock_files(STOCK_SIRECTORY)
            save_consolidated_stock(dataframe, OUTPUT_FILE)
            print(f"Les fichiers de {STOCK_SIRECTORY} ont été consolidés dans {OUTPUT_FILE}")

        if args.rechercher:
            column, value = args.rechercher
            dataframe = pd.read_csv(OUTPUT_FILE)
            search_stock(dataframe, column, value)
            print(f"Recherche effectuée pour {value} dans la colonne {column}")

        if args.rapport:
            dataframe = pd.read_csv(OUTPUT_FILE)
            generate_report(dataframe, REPORT_FILE)
            print(f"Rapport généré dans {REPORT_FILE}")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()