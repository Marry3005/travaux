import argparse
import pandas as pd
from consolidator import load_stock_files, save_consolidated_stock
from search import search_stock
from report import generate_report

STOCK_SIRECTORY = "stocks"
REPORT_FILE = "stock_report.csv"

def main():
    try:
        parser = argparse.ArgumentParser(description="gestion consolider les stocks")
        parser.add_argument("--consolider", action="store_true", help="consolider fichier csv en base unique")
        parser.add_argument("--rechercher", nargs=2, metavar=("COLONNE", "VALEUR"), help="recherche dans le stock par colonne et valeur")
        parser.add_argument("--rapport", action="store_true", help="Générer un rapport récapitulatif des stocks")
        parser.add_argument("--output", help="Spécifier le nom du fichier consolidé", default="consolidated_stock.csv")
        args = parser.parse_args()

        if args.consolider:
            try:
                dataframe = load_stock_files(STOCK_SIRECTORY)
                save_consolidated_stock(dataframe, args.output)
                print(f"Les fichiers de {STOCK_SIRECTORY} ont été consolidés dans {args.output}")
            except FileNotFoundError as e:
                print(f"Erreur : Le répertoire des fichiers de stock '{STOCK_DIRECTORY}' n'a pas été trouvé. {e}")
            except PermissionError as e:
                print(f"Erreur de permission : Impossible d'écrire dans le fichier '{args.output}'. {e}")
            except Exception as e:
                print(f"Une erreur inattendue est survenue lors de la consolidation des fichiers : {e}")

        if args.rechercher:
            try:
                column, value = args.rechercher
                dataframe = pd.read_csv(args.output)
                results = search_stock(dataframe, column, value)
                # Si aucun résultat n'a été trouvé (ou une colonne manquante)
                if results is None or results.empty:
                    pass

            except FileNotFoundError as e:
                print(f"Erreur : Le fichier '{args.output}' n'a pas été trouvé. {e}")
            except pd.errors.EmptyDataError as e:
                print(f"Erreur : Le fichier '{args.output}' est vide. {e}")
            except ValueError as e:
                print(f"Erreur de valeur : {e}")
            except Exception as e:
                print(f"Une erreur inattendue est survenue lors de la recherche dans le fichier : {e}")

        if args.rapport:
            try:
                dataframe = pd.read_csv(args.output)
                generate_report(dataframe, REPORT_FILE)
                print(f"Rapport généré dans {REPORT_FILE}")
            except FileNotFoundError as e:
                print(f"Erreur : Le fichier '{args.output}' n'a pas été trouvé. {e}")
            except pd.errors.EmptyDataError as e:
                print(f"Erreur : Le fichier '{args.output}' est vide. {e}")
            except PermissionError as e:
                print(f"Erreur de permission : Impossible d'écrire dans le fichier de rapport '{REPORT_FILE}'. {e}")
            except Exception as e:
                print(f"Une erreur inattendue est survenue lors de la génération du rapport : {e}")

    except argparse.ArgumentError as e:
        print(f"Erreur d'argument : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()