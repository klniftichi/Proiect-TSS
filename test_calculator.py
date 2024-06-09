import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 6), 10)
        self.assertEqual(self.calc.add(-1, 2),1)
        self.assertEqual(self.calc.add(-3, 5), 2)

    def test_substract(self):
        self.assertEqual(self.calc.substract(12, 5), 7)
        self.assertEqual(self.calc.substract(-1, 6), -7)
        self.assertEqual(self.calc.substract(-1, -4), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(9, 8), 72)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        # self.assertEqual(self.calc.multiply(5, 6), 1)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(24, 6), 4)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
