import unittest
from calculadora.functions import sumar, dividir, restar, multiplicar

class test_calculadora(unittest.TestCase):
    def test_sumar(self):
        result = sumar(2,3)
        self.assertEqual(result, 5, "El resultado debería ser 5")

    def test_restar(self):
        result = restar(5,4)
        self.assertEqual(result, 1, "El resultado debería ser 1")

    def test_multiplicar(self):
        result = multiplicar(3,4)
        self.assertEqual(result, 12, "El resultado debería ser 12")

    def test_dividir(self):
        result = dividir(12,3)
        self.assertEqual(result, 4, "El resultado debería ser 4")


if __name__ == "__main__":
    unittest.main()

