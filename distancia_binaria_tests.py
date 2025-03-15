import unittest

# Se importa el código a testear.
from distancia_binaria import distancia_binaria, son_aledaños, \
                   aledaños_menores, cant_aledaños, densidad_intervalo

#####################################################################

class TestVecinosBinarios(unittest.TestCase):
    ## ATENCION: los nombres de estas funciones deben empezar con test_

    def test_distancia_binaria(self):
        self.assertEqual(distancia_binaria(1, 1), 0)
        self.assertEqual(distancia_binaria(6, 18), 2)
        self.assertEqual(distancia_binaria(18, 6), 2)
        self.assertEqual(distancia_binaria(127 ,128), 8)
        self.assertEqual(distancia_binaria(128 ,127), 8)

    def test_vecinos_aledanos(self):
        self.assertTrue(son_aledaños(8, 12))
        self.assertTrue(son_aledaños(12, 8))
        self.assertFalse(son_aledaños(11, 12))
        self.assertFalse(son_aledaños(12, 11))

    def test_aledaños_menores(self):
        self.assertEqual(aledaños_menores(11), [3, 9, 10])
        self.assertEqual(aledaños_menores(16), [])

    def test_cantidad_aledaños(self):
        self.assertEqual(cant_aledaños(10, 8, 13), 2)
        self.assertEqual(cant_aledaños(32, 1, 31), 0)

    def test_densidad_intervalo(self):
        self.assertAlmostEqual(densidad_intervalo(10, 8, 13), 0.33333)
        self.assertAlmostEqual(densidad_intervalo(32, 1, 31), 0.0)

unittest.main()
