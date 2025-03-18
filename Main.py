class Calculator:
    """
    מחשבון בסיסי שמבצע חיבור, חיסור, כפל וחלוקה.

    פונקציות:
    - add: מחברת שני מספרים
    - subtract: מחסרת שני מספרים
    - multiply: מכפילה שני מספרים
    - divide: מחלקת שני מספרים. מעלה שגיאה אם מחלקים ב-0.
    """

    def add(self, a, b):
        """
        מחברת שני מספרים a ו-b ומחזירה את התוצאה.
        """
        return a + b

    def subtract(self, a, b):
        """
        מחסירה b מ-a ומחזירה את התוצאה.
        """
        return a - b

    def multiply(self, a, b):
        """
        מכפילה שני מספרים a ו-b ומחזירה את התוצאה.
        """
        return a * b

    def divide(self, a, b):
        """
        מחלקת את a ב-b ומחזירה את התוצאה. אם b שווה ל-0, מעלה שגיאה.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()


