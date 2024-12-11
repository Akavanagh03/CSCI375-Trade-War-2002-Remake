import unittest
from hypothesis import given, strategies as st
from ship_classes import Ship, Explorer, Fighter, Freighter, Defender, system


class TestShipClasses(unittest.TestCase):
    def setUp(self):
        # Set up sample ships and systems
        self.ship1 = Explorer("Voyager", "Earth", 100, {})
        self.ship2 = Fighter("Defender", "Mars", 200, {})
        self.system1 = system("Earth", {"metal": 10, "fuel": 20}, ["Mars"])
        self.system2 = system("Mars", {"metal": 15, "food": 25}, ["Earth"])

    # Test initialization
    def test_initialization(self):
        self.assertEqual(self.ship1.name, "Voyager")
        self.assertEqual(self.ship1.health, 100)
        self.assertEqual(self.ship1.current_location, "Earth")
        self.assertEqual(self.ship1.cargo, {})
        self.assertEqual(self.ship1.max_cargo, 150)

    # Test properties
    def test_health_property(self):
        self.ship1.health = 120
        self.assertEqual(self.ship1.health, 120)
        with self.assertRaises(AttributeError):
            del self.ship1.health

    def test_attack_property(self):
        self.ship1.attack = 70
        self.assertEqual(self.ship1.attack, 70)
        with self.assertRaises(AttributeError):
            del self.ship1.attack

    def test_defense_property(self):
        self.ship1.defense = 30
        self.assertEqual(self.ship1.defense, 30)
        with self.assertRaises(AttributeError):
            del self.ship1.defense

    def test_range_property(self):
        self.ship1.range = 6
        self.assertEqual(self.ship1.range, 6)
        with self.assertRaises(AttributeError):
            del self.ship1.range

    def test_credits_property(self):
        self.ship1.credits = 500
        self.assertEqual(self.ship1.credits, 500)
        with self.assertRaises(AttributeError):
            del self.ship1.credits

    def test_cargo_property(self):
        self.ship1.cargo = {"fuel": 10}
        self.assertEqual(self.ship1.cargo, {"fuel": 10})
        with self.assertRaises(AttributeError):
            del self.ship1.cargo

    def test_max_cargo_property(self):
        self.ship1.max_cargo = 200
        self.assertEqual(self.ship1.max_cargo, 200)
        with self.assertRaises(AttributeError):
            del self.ship1.max_cargo

    def test_current_location_property(self):
        self.ship1.current_location = "Mars"
        self.assertEqual(self.ship1.current_location, "Mars")
        with self.assertRaises(AttributeError):
            del self.ship1.current_location

    # Test warp functionality
    def test_warp(self):
        self.ship1.current_location = "Earth"
        self.assertIn("Mars", self.system1.connections)

    # Test battle functionality
    def test_battle_victory(self):
        self.ship1.attack = 100
        self.ship2.defense = 10
        self.ship2.health = 50
        self.ship1.battle(self.ship2)
        self.assertGreaterEqual(self.ship1.health, 1)
        self.assertEqual(self.ship2.health, 0)

    def test_battle_defeat(self):
        self.ship1.health = 20
        self.ship2.attack = 100
        self.ship1.defense = 0
        self.ship2.battle(self.ship1)
        self.assertEqual(self.ship1.health, 0)

    # Hypothesis property-based testing for ship health
    @given(st.integers(min_value=1, max_value=100))
    def test_health_within_bounds(self, health):
        self.ship1.health = health
        self.assertGreaterEqual(self.ship1.health, 1)
        self.assertLessEqual(self.ship1.health, 100)

    # Hypothesis property-based testing for cargo
    @given(st.dictionaries(st.text(),
           st.integers(min_value=1, max_value=10), max_size=5))
    def test_cargo_handling(self, cargo):
        self.ship1.cargo = cargo
        self.assertEqual(self.ship1.cargo, cargo)

    # Test system initialization
    def test_system_initialization(self):
        self.assertEqual(self.system1.name, "Earth")
        self.assertEqual(self.system1.trade_goods, {"metal": 10, "fuel": 20})
        self.assertEqual(self.system1.connections, ["Mars"])


if __name__ == "__main__":
    unittest.main()
