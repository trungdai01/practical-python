# test_stock.py

from unittest import TestCase, main
from .stock import Stock


class TestStock(TestCase):
    def test_create(self):
        s = Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock("GOOG", 100, 490.1)
        self.assertEqual(s.cost, 49010.0)
        self.assertEqual(s.shares, 100)
        s.sell(10)
        self.assertEqual(s.shares, 90)
        self.assertFalse(s.shares == "100")


if __name__ == "__main__":
    main()
