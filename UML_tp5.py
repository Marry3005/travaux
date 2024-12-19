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
