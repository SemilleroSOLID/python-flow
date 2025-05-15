# tests/test_calc.py
import unittest
from app.main import suma, resta

class TestCalc(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 2)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 2)

if __name__ == '__main__':
    unittest.main()
