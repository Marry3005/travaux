import unittest
from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - num est un entier positif valide, le den ne peut être null ou égale a 0
        POST : - la fraction est initialisé
        """
        if den == 0:
            raise ZeroDivisionError("Denominator cannnot be 0")

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and denominator must be integers")

        self.numerator = num
        self.denominator = den
        self.reduce()


    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Numerator must be an integer")
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("Denominator must be an integer")
        if value == 0:
            raise ValueError("Denominator cannnot be 0")
        self._denominator = value

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : - l'objet doit être valide, avec un num et den entier positif, le den ne peut pas être égal a 0
        POST : - affichage de la fraction
        """
        if self.denominator == 0:
            raise ZeroDivisionError("Error: den cannot be 0")
        elif self.denominator == 1: #si le denominateur est égal à 1 on renvoie directement de numérateur (ex: 4/1 = 4)
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"


    def reduce(self):
        """ réduction de la fraction de base
        PRE: - le num et den sont des entier positif valide, den ne peut être égal à 0 ou null
        POST: - réduit la fraction grâce à un commun diviseur
        """
        pgcd = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // pgcd
        self.denominator = self.denominator // pgcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction
        une fraction propre le num doit être strictement inférieur au dénominateur (ex: 1/2, 7/10)
        un nombre mixte combinaison d'un entier et d'une fraction propre(ex: 9/4--> quotient = 2 et le reste = 1)

        PRE : - num et den entier positif valide, den ne peut pas être null ou égale a 0
        POST : - affiche la somme d'un entier et d'une fraction
        """
        if self.denominator == 0:
            raise ZeroDivisionError("Error: den cannot be 0")

        #calcul de l'entier et du reste
        self.reduce()
        entier = self.numerator // self.denominator #partie entière
        reste = self.numerator % self.denominator #le reste de la division

        if reste == 0:  #si le reste est à 0 on renvoie directement l'entier
            return f"{entier}"
        return f"{entier}, {reste}/{self.denominator}"  #sinon, on affiche l'entier (quotient) + le reste sur le dénominateur



    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : - l'objet 'other' doit être une instance de 'Fraction'
               - le denominator de 'self' et 'other' ne peut être égal à 0 ou null
         POST : - return l'addition de 2 fractions
         """
        if not isinstance(other, Fraction): #si other n'est pas une instance de Fraction (ex: un entier) erreur est afficher
            raise TypeError("Addition seulement avec une autre fraction")

        new_numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : - l'objet 'other' doit être une instance de 'Fraction'
               - le denominator de 'self' et 'other' ne peut être égal à 0 ou null
        POST : - return la soustraction de 2 fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Subtraction seulement avec une autre fraction")

        new_numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)



    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : - l'objet 'other' doit être une instance de 'Fraction'
               - le denominator de 'self' et 'other' ne peut être égal à 0 ou null
        POST : - return la multiplication de 2 fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Multiplication seulement avec une autre fraction")

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)



    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : - l'objet 'other' doit être une instance de 'Fraction'
               - le denominator de 'self' ne peut être égal à 0 ou null
               - le numerator de 'other' ne peut pas être égal à 0 ou null
        POST : - return la division de 2 fractions
        """
        if not isinstance(other, Fraction):
            raise TypeError("Division seulement avec une autre fraction")

        if other.numerator == 0:
            raise ZeroDivisionError("Division d'une fraction avec un numérateur nul n'est pas possible")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : - 'other' doit être un entier
               - le denominator ne peut être égal à 0 ou null
        POST : - return la fraction élevé a la puissance 'other'
               - si 'other' est négatif, la fraction sera inversée avant l'élévation
               - exception 'ZeroDivisionError' si le denominator de la fraction inversée est égal à 0
        """
        if not isinstance(other, int):
            raise TypeError("L'exposant doit être un entier")

        if other == 0:
            return Fraction(1, 1) #toute fraction à la puissance 0 est = 1/1
        elif other < 0:
            if self.numerator == 0:
                raise ZeroDivisionError("La fraction peut pas être élevé avec un numérateur nul ")

            new_numerator = self.denominator ** abs(other) #abs renvoie une valeur absolue, valeur sans tenir compte de son signe
            new_denominator = self.numerator ** abs(other)
        else:
            new_numerator = self.numerator ** other
            new_denominator = self.denominator ** other

        return Fraction(new_numerator, new_denominator)


    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : - l'objet 'other' doit être une instance de 'Fraction'
        POST : - return True si les 2 fractions sont égales (après réduction)
               - exception 'TypeError' si 'other' n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Equality seulement avec une autre fraction")

        #crée une copie des fractions d'origine pour éviter leurs modifications. Si on ne fait pas de copie ca risque de faire des problème par la suite
        self_copy = Fraction(self.numerator, self.denominator)
        other_copy = Fraction(other.numerator, other.denominator)

        #reduction des fractions
        self_copy.reduce()
        other_copy.reduce()

        return self.numerator == other.numerator and self.denominator == other.denominator


    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : - l'objet doit être valide.
              - le num et den sont entier valide
              - den ne peut pas être null ou égal à 0
        POST : - return le nombre decimal de la fraction sous forme de flottant
        """
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0")

        return self.numerator / self.denominator



    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -l'objet doit être correctement initialisé
              - le num et den doivent être valide
              - le den ne peut pas être égal à 0
        POST : - return True si valeur de la fraction est zero
               - aussi non return False
        """
        return self.numerator == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -l'objet doit être correctement initialisé
              - le num et den doivent être valide
              - le den ne peut pas être égal à 0
        POST : - return True si valeur de la fraction est entier (num divisé par den sans reste)
               - aussi non return False
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1
        la valeur absolue d'un nombre positif est égale à lui-même
        la valeur absolue d'un nombre négatif est le même nombre sans le signe négatif

        pour qu'une fraction soit propre il faut que la valeur absolue du numérateur soit plus petit que la valeur absolue du dénominateur
        la fraction aura une valeure absolue inférieur a 1 tant que le num est plus petit que le den (ex: 3/4 = 0.75 ce qui est < 1 et 4/3 = 1.33 est > 1)
        si num = 0 toujours < 1

        PRE : -l'objet doit être correctement initialisé
              - le num et den doivent être valide
              - le den ne peut pas être égal à 0
        POST : - return True si valeur absolue de la fraction est strictement inférieur à 1
               - aussi non return False
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        la copie de la fraction c'est pour évité de modifier la fraction de base et d'évité les bug

        PRE : -l'objet doit être correctement initialisé
              - le num et den doivent être valide
              - le den ne peut pas être égal à 0
        POST : - return True si le numérateur de la fraction réduite est égale à 1
               - aussi non return False
        """
        copy = Fraction(self.numerator, self.denominator)
        copy.reduce()
        return copy.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : -l'objet 'other' doit être correctement initialisé
              - fractions valide et den non nul
        POST : - Retourne True si la valeur absolue de la différence des deux fractions est une fraction unité (numérateur = 1)
               - Retourne False sinon
        """
        if not isinstance(other, Fraction):
            raise TypeError("Comparaion est uniquement avec une fraction")

        #calcul de la dif des valeurs absolue
        diff_numerator = abs(self.numerator * other.denominator - other.numerator * self.denominator)
        diff_denominator = self.denominator * other.denominator

        #vérifier si fraction unité
        gcd_diff = gcd(diff_numerator, diff_denominator)
        diff_numerator //= gcd_diff #même chose que diff_numerator // gcd_diff
        diff_denominator //= gcd_diff

        return diff_numerator == 1
