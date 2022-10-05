import unittest
from calculadoraVectoresMatrices import *


class PruebasDoubleSplit(unittest.TestCase):
    def testN1WithNaturalValues(self):
        print("Con numeros naturales")
        matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (1, 0)],
                  [(0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                  [(1, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)]]

        vector = [(6, 0), (2, 0), (1, 0), (5, 0), (3, 0), (10, 0)]
        print(vector, "Valor Inicial")
        print(consecutiveMultiplicy(matriz, vector, 1), "N = 1")

    def testN1WithProbabilities(self):
        print("Probabilities")
        matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(1 / 6, 0), (1 / 3, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(1 / 6, 0), (1 / 3, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                  [(1 / 3, 0), (1 / 3, 0), (1 / 3, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                  [(1 / 6, 0), (0, 0), (1 / 3, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
                  [(1 / 6, 0), (0, 0), (1 / 3, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]

        vector = [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        print(vector, "Initial value")
        print(consecutiveMultiplicy(matriz, vector, 1), "N = 1")


if __name__ == "__main__":
    unittest.main()