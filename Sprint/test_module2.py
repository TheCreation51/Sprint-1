import unittest
from module2 import Drink, Order, create_order

class TestDrink(unittest.TestCase):
    def test_get_base(self):
        drink = Drink()
        drink.set_base("Water")
        self.assertEqual(drink.get_base(), "Water")

    def test_get_flavors(self):
        drink = Drink()
        drink.add_flavor("Lemon")
        drink.add_flavor("Mint")
        self.assertEqual(drink.get_flavors(), ["Lemon", "Mint"])

    def test_get_size(self):
        drink = Drink()
        drink.set_size("Mega")
        self.assertEqual(drink.get_size(), "Small")

    def test_set_base_invalid(self):
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.set_base("InvalidBase")

    def test_set_size_invalid(self):
        drink = Drink()
        drink.set_size("InvalidSize")
        self.assertEqual(drink.get_size(), "InvalidSize")

    def test_add_flavor_invalid(self):
        drink = Drink()
        with self.assertRaises(ValueError):
            drink.add_flavor("InvalidFlavor")

    def test_add_flavor_duplicate(self):
        drink = Drink()
        drink.add_flavor("Lemon")
        with self.assertRaises(ValueError):
            drink.add_flavor("Lemon")

    def test_calculate_price(self):
        drink = Drink()
        drink.set_base("Water")
        drink.set_size("Mega")
        drink.add_flavor("Lemon")
        drink.add_flavor("Mint")
        self.assertAlmostEqual(drink.calculate_price(), 2.45)

class TestOrder(unittest.TestCase):
    def test_get_items(self):
        order = Order()
        drink = Drink()
        drink.set_base("Water")
        drink.set_size("Mega")
        order.add_item(drink)
        self.assertEqual(len(order.get_items()), 1)

    def test_get_receipt(self):
        order = Order()
        drink = Drink()
        drink.set_base("Water")
        drink.set_size("Mega")
        drink.add_flavor("Lemon")
        order.add_item(drink)
        receipt = order.get_receipt()
        self.assertIn("Subtotal", receipt)
        self.assertIn("Tax", receipt)
        self.assertIn("Total", receipt)

    def test_add_item_invalid(self):
        order = Order()
        with self.assertRaises(TypeError):
            order.add_item("NotADrink")

class TestCreateOrder(unittest.TestCase):
    def test_create_order_valid(self):
        order_data = [
            {"base": "Water", "size": "Mega", "flavors": ["Lemon", "Mint"]},
            {"base": "Pokeacola", "size": "Mega", "flavors": ["Cherry"]},
        ]
        result = create_order(order_data)
        self.assertIn("receipt", result)

    def test_create_order_invalid_base(self):
        order_data = [
            {"base": "InvalidBase", "size": "Mega", "flavors": ["Lemon", "Mint"]},
        ]
        result = create_order(order_data)
        self.assertIn("error", result)

    def test_create_order_invalid_size(self):
        order_data = [
            {"base": "Water", "size": "InvalidSize", "flavors": ["Lemon", "Mint"]},
        ]
        result = create_order(order_data)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()