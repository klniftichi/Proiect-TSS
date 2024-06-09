import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1000, 2000), 3000)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_substract(self):
        self.assertEqual(self.calc.substract(10, 5), 5)
        self.assertEqual(self.calc.substract(0, 0), 0)
        self.assertEqual(self.calc.substract(-1, -1), 0)
        self.assertEqual(self.calc.substract(-1, 1), -2)
        self.assertEqual(self.calc.substract(2000, 1000), 1000)
        self.assertEqual(self.calc.substract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(100, 200), 20000)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(2000, 1000), 2)
        self.assertEqual(self.calc.divide(4.5, 1.5), 3.0)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
