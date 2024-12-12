import unittest
from my_fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        """
        Test vérifie l'init de la class Fraction fonctionne dans
        les cas normaux, avec une valeur par défaut
        et les cas invalide
        """
        #init de base
        f = Fraction(6, 8) # création fraction 6/8 sui est réduite à 3/4
        self.assertEqual(f.numerator, 3) #vérifie que le num est égal à 3
        self.assertEqual(f.denominator, 4) #vérifie que le dem égal à 4

        f2 = Fraction(-4, 8)
        self.assertEqual(f2.numerator, -1)
        self.assertEqual(f2.denominator, 2)

        f3 = Fraction(4, -8)
        self.assertEqual(f3.numerator, -1)
        self.assertEqual(f3.denominator, 2)

        f4 = Fraction(-4, -8)
        self.assertEqual(f4.numerator, 1)
        self.assertEqual(f4.denominator, 2)

        #init par défaut
        f_defaut = Fraction()
        self.assertEqual(f_defaut.numerator, 0)
        self.assertEqual(f_defaut.denominator, 1)

        #vérifie création fraction avec den de 0 déclenche cette exception
        with self.assertRaises(ZeroDivisionError):
            Fraction(1,0)

        #vérifie si l'utilisation d'un numérateur non valide déclenche cette exception
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)

    def test_str(self):
        """ vérifie que la focntion __str__ renvoie
        bonne représentation textuelle de la fraction"""

        self.assertEqual(str(Fraction(6, 8 )), "3/4" ) #vérifie que la fraction retourne bien la fration simplifier sous forme de string
        self.assertEqual(str(Fraction(4, 1)), "4" ) #vérifie que la fraction renvoie bien le num sous forme de string
        self.assertEqual(str(Fraction(0, 1)), "0" ) #vérifie que la fraction renvoie la chaine 0
        self.assertEqual(str(Fraction(3, -4)), "-3/4" )
        self.assertEqual(str(Fraction(-3, 4)), "-3/4" )
        self.assertEqual(str(Fraction(-3, -4)), "3/4" )

    def test_as_mixed_number(self):
        """ Test convertion d'une fraction en un nombre mixte"""

        self.assertEqual(Fraction(9, 4).as_mixed_number(), "2, 1/4") #renvoie l'entier 2 et le reste de la fraction 1/4
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2") #renvoie un entier car c'est une fraction 4/2 est aussi representer comme étant 2
        self.assertEqual(Fraction(3, 1).as_mixed_number(), "3") #renvoie un entier car 3/1 = 3
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "0, 1/2") # le quotien est de 0 et le fraction restante est 1/2

    def test_add(self):
        """Test l'addition des fractions"""

        f1 = Fraction(1, 2 )
        f2 = Fraction(1, 3 )
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

        f3 = Fraction(0, 1)
        f4 = Fraction(1, 2)
        result2 = f3 + f4
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 2)

        f5 = Fraction(0, 1)
        f6 = Fraction(0, 2)
        result3 = f5 + f6
        self.assertEqual(result3.numerator, 0)
        self.assertEqual(result3.denominator, 1)

        f7 = Fraction(-1, 3)
        f8 = Fraction(1, 2)
        result4 = f7 + f8
        self.assertEqual(result4.numerator, 1)
        self.assertEqual(result4.denominator, 6)

        f9 = Fraction(-1, 3)
        f10 = Fraction(-1, 2)
        result5 = f9 + f10
        self.assertEqual(result5.numerator, -5)
        self.assertEqual(result5.denominator, 6)

    def test_sub(self):
        ''' Test la soustraction des fractions '''
        f1 = Fraction(1, 2 )
        f2 = Fraction(1, 3 )
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        f3 = Fraction(0, 1)
        f4 = Fraction(1, 2)
        result2 = f3 - f4
        self.assertEqual(result2.numerator, -1)
        self.assertEqual(result2.denominator, 2)

        f5 = Fraction(0, 1)
        f6 = Fraction(0, 2)
        result3 = f5 - f6
        self.assertEqual(result3.numerator, 0)
        self.assertEqual(result3.denominator, 1)

        f7 = Fraction(-1, 3)
        f8 = Fraction(1, 2)
        result4 = f7 - f8
        self.assertEqual(result4.numerator, -5)
        self.assertEqual(result4.denominator, 6)

        f9 = Fraction(-1, 3)
        f10 = Fraction(-1, 2)
        result5 = f9 - f10
        self.assertEqual(result5.numerator, 1)
        self.assertEqual(result5.denominator, 6)

    def test_mul(self):
        ''' Test la multiplication des fractions '''
        f1 = Fraction(1, 2 )
        f2 = Fraction(2, 3 )
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        f3 = Fraction(0, 1)
        f4 = Fraction(1, 2)
        result2 = f3 * f4
        self.assertEqual(result2.numerator, 0)
        self.assertEqual(result2.denominator, 1)

        f5 = Fraction(-1, 3)
        f6 = Fraction(1, 2)
        result3 = f5 * f6
        self.assertEqual(result3.numerator, -1)
        self.assertEqual(result3.denominator, 6)

        f7 = Fraction(-1, 3)
        f8 = Fraction(-2, 5)
        result4 = f7 * f8
        self.assertEqual(result4.numerator, 2)
        self.assertEqual(result4.denominator, 15)


    def test_div(self):
        ''' Tester la division des fractions '''
        f1 = Fraction(1, 2 )
        f2 = Fraction(2, 3 )
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

        f3 = Fraction(1, 2)
        f4 = Fraction(-1, 3)
        result2 = f3 / f4
        self.assertEqual(result2.numerator, -3)
        self.assertEqual(result2.denominator, 2)

        f5 = Fraction(-1, 3)
        f6 = Fraction(-2, 5)
        result3 = f5 / f6
        self.assertEqual(result3.numerator, 5)
        self.assertEqual(result3.denominator, 6)

        f7 = Fraction(0, 1)
        f8 = Fraction(1, 2)
        result4 = f7 / f8
        self.assertEqual(result4.numerator, 0)
        self.assertEqual(result4.denominator, 1)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2)/Fraction(0, 1)

    def test_power(self):
        ''' Tester l'élévation à la puissance de la fraction'''
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

        result2 = f ** -1
        self.assertEqual(result2.numerator, 3)
        self.assertEqual(result2.denominator, 2)

        result3 = f ** 0
        self.assertEqual(result3.numerator, 1)
        self.assertEqual(result3.denominator, 1)

        f_zero = Fraction(0, 1)
        result4 = f_zero ** 2
        self.assertEqual(result4.numerator, 0)
        self.assertEqual(result4.denominator, 1)

        with self.assertRaises(ZeroDivisionError):
            result4 = f_zero ** -1

        with self.assertRaises(TypeError):
            result = f ** 1.5


    def test_eq(self):
        ''' Tester l'égalitée des fractions '''
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4)) #vérifie que 1/2 est égal à 2/4
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3)) #vérifier que 1/2 n'est pas égal à 2/3

        self.assertTrue(Fraction(1, 2) == Fraction(-1, -2))
        self.assertFalse(Fraction(1, 2) == Fraction(1, -2))

        with self.assertRaises(TypeError):
            Fraction(1, 2) == 1

    def test_float(self):
        ''' Test convertion des fractions en nombre flottant'''
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)

        self.assertEqual(float(Fraction(0, 1)), 0.0)

        self.assertEqual(float(Fraction(-1, 2)), -0.5)
        self.assertEqual(float(Fraction(3, -4)), -0.75)

        self.assertEqual(float(Fraction(-3, -4)), 0.75)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_properties(self):
        #Test is_zero
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(3, 4).is_zero())
        self.assertFalse(Fraction(-1, 2).is_zero())

        #Test is_integer
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(-3, 2).is_integer())

        #Test is_proper
        self.assertTrue(Fraction(2, 4).is_proper())
        self.assertFalse(Fraction(-5, 4).is_proper()) #valeur absolue ignore le signe

        #Test is_unit
        self.assertTrue(Fraction(2, 4).is_unit()) #valeur num fraction réduite = 1
        self.assertFalse(Fraction(-2, 3).is_unit())

    def test_is_adjacent_to(self):
        ''' Test si les 2 fractions sont adjacentes'''
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(2, 3)))
        self.assertFalse(Fraction(1, 3).is_adjacent_to(Fraction(1, 5)))
        
        #fraction nulle n'est adjacente à aucune autre
        self.assertFalse(Fraction(0, 1).is_adjacent_to(Fraction(2, 5)))

        #fraction négative
        self.assertTrue(Fraction(-1, 2).is_adjacent_to(Fraction(-1, 3)))
        self.assertFalse(Fraction(-1, 2).is_adjacent_to(Fraction(1, 3)))

        #fraction avec 2 négatif
        self.assertTrue(Fraction(-1, -2).is_adjacent_to(Fraction(-1, -3)))

        with self.assertRaises(TypeError):
            Fraction(1, 2).is_adjacent_to(Fraction("1/3"))




if __name__ == "__main__":
    unittest.main()