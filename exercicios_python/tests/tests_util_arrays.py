import unittest
from utils import util_arrays
from utils.util_arrays import *


class TestUtilArrays(unittest.TestCase):
    def test_lista_normal(self):
        self.assertEqual(achar_maior([1,5,77,2,66,52]), 77)
        self.assertEqual(achar_menor([5,7,2,88,54]), 2)

    def test_todos_negativos(self):
        self.assertEqual(achar_maior([-6,-4,-22,-98]), -4)
        self.assertEqual(achar_menor([-2,-7,-8,-46]), -46)

    def test_unico_numero(self):
        self.assertEqual(achar_menor([1]), 1)
        self.assertEqual(achar_maior([55]), 55)

    def test_lista_vazia(self):
        self.assertIsNone(achar_maior([]))
        self.assertIsNone(achar_menor([]))

if __name__ == '__main__':
    unittest.main()