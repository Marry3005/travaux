#1.1 animaux

class Animal:
    def __init__(self, nom, tete, corp, membres ):
        self.nom = nom
        self.tete = tete
        self.corp = corp
        self.membres = membres
        self.type = None
        self.categorie = None
        self.habitat = []

class Categorie:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = [] #liste des animaux dans cette catégorie

    def ajouter_animal(self, animal):
        if animal not in self.animaux:
            self.animaux.append(animal)
            animal.categorie = self #l'animal appartient à cette catégorie

class Habitat:
    def __init__(self, nom, type_habitat):
        self.nom = nom
        self.type_habitat = type_habitat #ex: terrestre, aquatique
        self.animaux = [] #Liste des animaux dans cet habitat

    def ajouter_animal(self, animal):
        if animal not in self.animaux:
            self.animaux.append(animal)
            if self not in animal.habitat: #l'animal vit dans cet habitat
                animal.habitat.append(self)

class Type:
    def __init__(self, nom):
        self.nom = nom #Herbivore, carnivore
        self.animaux = [] #Liste des animaux associés à ce type

    def ajouter_animal(self, animal):
        if animal not in self.animaux:
            self.animaux.append(animal)
            animal.type = self #l'animal appartient à ce type

# Création de types
herbivore = Type("Herbivore")
carnivore = Type("Carnivore")

# Création de catégories
lapin = Categorie("Lapin")
lion = Categorie("Lion")

# Création d'habitats
foret = Habitat("Forêt", "Terrestre")
savane = Habitat("savane", "Terrestre")

# Création d'animaux
lapin1 = Animal("Lapin", "Petite tête", "Corps de lapin", ["pattes", "oreilles"])
lion1 = Animal("Lion", "Grande tête", "Corps de lion", ["pattes", "queue"])

# Associer les animaux aux types
herbivore.ajouter_animal(lapin1)
carnivore.ajouter_animal(lion1)

# Associer les animaux aux catégories
lapin.ajouter_animal(lapin1)
lion.ajouter_animal(lion1)

# Associer les animaux aux habitats
foret.ajouter_animal(lapin1)
savane.ajouter_animal(lion1)

# Affichage des résultats
print(f"Animaux dans la Forêt : {[animal.nom for animal in foret.animaux]}")
print(f"Animaux dans la savane : {[animal.nom for animal in savane.animaux]}")
print ("\n\n")


#1.2 Classe

from datetime import date

class DossierPersonnel:
    def __init__(self, nom, prenom, date_naiss, email, num_tel, lieux_naiss, nationalite):
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.email = email
        self.num_tel = num_tel
        self.lieux_naiss = lieux_naiss
        self.nationalite = nationalite

    def __str__(self):
        return (
            f"DossierPersonnel(nom={self.nom}, prenom={self.prenom}, date_naiss={self.date_naiss.strftime('%d/%m/%Y')}, "
            f"email={self.email}, num_tel={self.num_tel}, lieux_naiss={self.lieux_naiss}, nationalite={self.nationalite})")

class Professeur:
    def __init__(self, nom, prenom, date_naiss, adresse, email, num_tel):
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.email = email
        self.num_tel = num_tel
        self.dossier_personnel = None  # Relation de composition avec DossierPersonnel
        self.classes = []  # Liste des classes qu'un professeur peut enseigner

    def ajouter_classe(self, classe):
        if classe not in self.classes:
            self.classes.append(classe)
            classe.prof = self  # Lien vers le professeur

    def ajouter_dossier_personnel(self, dossier):
        self.dossier_personnel = dossier

    def __str__(self):
        return (f"Professeur(nom={self.nom}, prenom={self.prenom}, date_naiss={self.date_naiss.strftime('%d/%m/%Y')}, "
                f"adresse={self.adresse}, email={self.email}, num_tel={self.num_tel}, "
                f"dossier_personnel={self.dossier_personnel}, classes={[classe.nom for classe in self.classes]})")


class Eleve:
    def __init__(self, nom, prenom, date_naiss, adresse, email, num_tel):
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.adresse = adresse
        self.email = email
        self.num_tel = num_tel
        self.dossier_personnel = None  # Relation de composition avec DossierPersonnel
        self.classe = None  # Relation d'association avec Classe

    def ajouter_classe(self, classe):
        self.classe = classe
        classe.ajouter_eleve(self)  # Lien vers la classe

    def ajouter_dossier_personnel(self, dossier):
        self.dossier_personnel = dossier

    def __str__(self):
        return (f"Eleve(nom={self.nom}, prenom={self.prenom}, date_naiss={self.date_naiss.strftime('%d/%m/%Y')}, "
                f"adresse={self.adresse}, email={self.email}, num_tel={self.num_tel}, "
                f"dossier_personnel={self.dossier_personnel}, classe={self.classe.nom if self.classe else None})")


class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.prof = None  # Lien vers le Professeur
        self.eleves = []  # Liste des élèves dans la classe

    def ajouter_professeur(self, professeur):
        if self.prof is None:
            self.prof = professeur
            professeur.ajouter_classe(self)

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30 and eleve not in self.eleves:
            self.eleves.append(eleve)
            eleve.ajouter_classe(self)  # Lien vers l'élève

    def __str__(self):
        return (f"Classe(nom={self.nom}, prof={self.prof.nom if self.prof else None}, "
                f"eleves={[eleve.nom for eleve in self.eleves]})")

# Création des dossiers personnels
dossier_prof = DossierPersonnel("Dupont", "Jean", date(1980, 5, 1), "jean.dupont@email.com", 123456789, "Paris", "Française")
dossier_eleve1 = DossierPersonnel("Martin", "Paul", date(2005, 8, 15), "paul.martin@email.com", 987654321, "Lyon", "Français")
dossier_eleve2 = DossierPersonnel("Durand", "Alice", date(2006, 3, 22), "alice.durand@email.com", 654987321, "Nice", "Française")

# Création du professeur et de sa classe
professeur = Professeur("Dupont", "Jean", date(1980, 5, 1), "1 rue des écoles", "jean.dupont@email.com", 123456789)
professeur.ajouter_dossier_personnel(dossier_prof)

classe = Classe("3ème A")
classe.ajouter_professeur(professeur)

# Création des élèves et ajout à la classe
eleve1 = Eleve("Martin", "Paul", date(2005, 8, 15), "10 rue des écoles", "paul.martin@email.com", 987654321)
eleve1.ajouter_dossier_personnel(dossier_eleve1)
eleve1.ajouter_classe(classe)

eleve2 = Eleve("Durand", "Alice", date(2006, 3, 22), "15 rue des écoles", "alice.durand@email.com", 654987321)
eleve2.ajouter_dossier_personnel(dossier_eleve2)
eleve2.ajouter_classe(classe)

# Affichage
print(classe)
print(professeur)
print(eleve1)
print(eleve2)
print ("\n\n")
#1.3 Email

from typing import List, Optional

class Fichier:
    def __init__(self, nom: str, taille: int, type_mime: str):
        self.nom = nom
        self.taille = taille
        self.type_mime = type_mime


class Email:
    def __init__(self, expediteur: str, destinataire: str, titre: Optional[str] = None, texte: Optional[str] = None, fichiers_joins: Optional[List[Fichier]] = None):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.titre = titre
        self.texte = texte
        self.fichiers_joins = fichiers_joins if fichiers_joins is not None else []

    def ajouter_fichier(self, fichier: Fichier):
        """Ajoute un fichier joint à l'email."""
        self.fichiers_joins.append(fichier)
# Création de fichiers joints
fichier1 = Fichier("document.pdf", 500, "application/pdf")
fichier2 = Fichier("image.png", 1200, "image/png")
fichier3 = Fichier("audio.mp3", 3400, "audio/mpeg")

# Création d'un email
email = Email(
    expediteur="alice@example.com",
    destinataire="bob@example.com",
    titre="Projet Important",
    texte="Bonjour Bob, \n\nVoici les fichiers pour le projet important. \n\nCordialement, \nAlice"
)

# Ajout des fichiers joints
email.ajouter_fichier(fichier1)
email.ajouter_fichier(fichier2)
email.ajouter_fichier(fichier3)

# Affichage des détails de l'email
print(f"Expéditeur: {email.expediteur}")
print(f"Destinataire: {email.destinataire}")
print(f"Titre: {email.titre}")
print(f"Texte: {email.texte}")
print("Fichiers joints:")
for fichier in email.fichiers_joins:
    print(f"  - Nom: {fichier.nom}, Taille: {fichier.taille} Ko, Type: {fichier.type_mime}")
