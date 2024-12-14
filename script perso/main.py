from consolidator import load_stock_files, save_consolidated_stock

if __name__ == "__main__":
    # Spécifier le répertoire contenant les fichiers CSV
    directory = "stocks"

    # Charger et consolider les fichiers CSV
    try:
        dataframe = load_stock_files(directory)
        print("Fichiers CSV chargés et consolidés:")
        print(dataframe)

        # Sauvegarder le DataFrame consolidé dans un fichier CSV
        output_file = "consolidated_stock.csv"
        save_consolidated_stock(dataframe, output_file)
        print(f"Fichier consolidé sauvegardé sous {output_file}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
