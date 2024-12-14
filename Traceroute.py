import subprocess
import re

# Exécution commande tracert (équivalent de traceroute)
command = ["tracert", "-h", "5", "www.google.com"]

try:
    # Exécuter commande est récupérer la sortie
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # vérification erreur
    if result.returncode != 0:
        print("Erreur lors exécution commande tracert")
    else:
        # Extraire les IPs des sauts via expression régulière
        ip_addresses = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b|[a-fA-F0-9:]+", result.stdout)

        # afficher les IPs extraites
        print("Liste des IPs des sauts: ", ip_addresses)
except Exception as e:
    print(f"Erreur: {e}")