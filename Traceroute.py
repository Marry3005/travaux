import subprocess
import re
import argparse

#argument parser pour gérer les options
parser = argparse.ArgumentParser(description="Exécuter un traceroute et extraire les adresses IP des sauts")
parser.add_argument("-p", "--progressive", action="store_true", help="Afficher les IPs au fur et à mesure de l'exécution")
parser.add_argument("-o", "--output-file", type=str, help="Nom du fichier où enregistrer le résultat")

args = parser.parse_args()

# Exécution commande tracert (équivalent de traceroute)
command = ["tracert", "-h", "5", "www.google.com"]

#Expression régulière pour extraire les IPs (IPv4 et IPv6)
ip_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b|(?:[a-fA-F0-9]{1,4}:){2,7}[a-fA-F0-9]{1,4}\b")

output_file = None
if args.output_file:
    output_file = open(args.output_file, "w")

try:
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        print("Traceroute en cours ...\n")

        #lire la sortie ligne par ligne
        for line in process.stdout:
            line = line.strip()
            #affichier ligne fur et à mesure si l'option -p activée
            if args.progressive:
                print(line)

            #Ecrire dans le fichier si option -o fournie
            if output_file:
                output_file.write(line + "\n")

            #rechercher les IPs dans la ligne
            match = ip_pattern.findall(line)
            if match:
                for ip in match:
                    #afficher IPs au fur et à mesure si option -p est activée
                    if args.progressive:
                        print(f"IP trouvée: {ip}")

                    #Ecrire les IPs dans le fichier si option -o activée
                    if output_file:
                        output_file.write(f"IP trouvée: {ip}\n")

    # vérification erreur
    return_code = process.wait()
    if return_code != 0:
        print("Erreur avec code retour: {return_code}")
        if output_file:
            output_file.write(f"Erreur avec code retour: {return_code}\n")

except Exception as e:
    print(f"Erreur: {e}")

finally:
    if output_file:
        output_file.close()