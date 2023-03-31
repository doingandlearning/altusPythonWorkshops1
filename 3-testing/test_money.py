import unittest

# 5USD x 2 = 10USD
# 10EUR x 2 = 20EUR


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        # Arrange
        fiver = Money(5, "USD")
        # Act
        tenner = fiver.times(2)
        # Assert
        self.assertEqual(10, tenner.amount)
        self.assertEqual('USD', tenner.currency)

    def testMultiplicationSecondValue(self):
        # Arrange
        tenner = Money(10, "USD")
        # Act
        thirty = tenner.times(3)
        # Assert
        self.assertEqual(30, thirty.amount)
        self.assertEqual('USD', tenner.currency)

    def testMultiplicationInEuro(self):
        tenEuros = Money(10, "EUR")  # DRY Don't Repeat Yourself
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", twentyEuros.currency)


if __name__ == "__main__":
    unittest.main()


# self.assertEqual(a, b),
# self.assertNotEqual(a, b),
# self.assertTrue(x),
# self.assertFalse(x),
# self.assertIsNone(x),
# self.assertIsNotNone(x),
# self.assertIs(a, b),
# self.assertIsNot(a, b),
# self.assertIn(a, b),
# self.assertNotIn(a, b),
# self.assertIsInstance(a, b),
# self.assertNotIsInstance(a, b),
# self.assertRaises(),
# self.assertRaisesRegex(),
# self.assertWarns(),
# self.assertWarnsRegex(),
# self.assertLogs(),
