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
            """
                PRE : Vérification que les fichiers de stock sont disponibles et consolidation.
                POST: Confirmer que la consolidation a été réalisée avec succès.
                RAISE :
                    - `FileNotFoundError` : Si le répertoire des fichiers de stock est introuvable.
                    - `PermissionError` : Si le programme ne peut pas écrire dans le fichier de sortie.
                    - `Exception` : Erreur générale si une autre exception inattendue survient.
            """
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

            print("Consolidation terminée.")


        if args.rechercher:
            """
                PRE: Vérification que le fichier consolidé est chargé correctement pour la recherche.
                POST : Afficher les résultats de la recherche ou indiquer qu'aucun résultat n'a été trouvé.
                RAISE :
                    - `FileNotFoundError` : Si le fichier consolidé n'est pas trouvé.
                    - `pd.errors.EmptyDataError` : Si le fichier est vide.
                    - `ValueError` : Si les paramètres de recherche sont incorrects.
                    - `Exception` : Erreur générale si une autre exception inattendue survient.
            """
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

            print("Recherche terminée.")


        if args.rapport:
            """
                PRE : Vérification du fichier consolidé avant la génération du rapport.
                POST : Confirmation de la génération du rapport.
                RAISE :
                    - `FileNotFoundError` : Si le fichier consolidé est introuvable.
                    - `pd.errors.EmptyDataError` : Si le fichier consolidé est vide.
                    - `PermissionError` : Si le programme ne peut pas écrire dans le fichier de rapport.
                    - `Exception` : Erreur générale si une autre exception inattendue survient.
            """
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

            print("Génération du rapport terminée.")


    except argparse.ArgumentError as e:
        print(f"Erreur d'argument : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()