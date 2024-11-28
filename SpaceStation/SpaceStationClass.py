from typing import Dict

class SpaceStation:
    def __init__(self, name: str, items_for_trade: Dict[str, int], repair_cost: int, upgrade_cost: int):
        """
        Initializes a space station.

        Args:
            name (str): The name of the space station.
            items_for_trade (Dict[str, int]): A dictionary of items available for trade and their prices.
            repair_cost (int): The cost per unit of health to repair a ship.
            upgrade_cost (int): The cost for upgrading a ship's attribute.
        """
        self._name = name
        self._items_for_trade = items_for_trade
        self._repair_cost = repair_cost
        self._upgrade_cost = upgrade_cost

    @property
    def name(self) -> str:
        """Gets the name of the space station."""
        return self._name

    @property
    def items_for_trade(self) -> Dict[str, int]:
        """Gets the items available for trade and their prices."""
        return self._items_for_trade

    def trade(self, ship, action: str, item: str = None, amount: int = 1) -> bool:
        """
        Facilitates trading at the space station.

        Args:
            ship (Ship): The ship conducting the trade.
            action (str): The action to perform ('buy' or 'sell').
            item (str): The item to trade.
            amount (int): The amount of the item to trade.

        Returns:
            bool: True if the trade was successful, False otherwise.
        """
        if action == "buy":
            if item in self._items_for_trade and self._items_for_trade[item] * amount <= ship.credits:
                ship.credits -= self._items_for_trade[item] * amount
                ship.cargo[item] = ship.cargo.get(item, 0) + amount
                print(f"{ship.name} bought {amount} {item}(s) for {self._items_for_trade[item] * amount} credits.")
                return True
            print(f"Not enough credits or invalid item.")
            return False

        elif action == "sell":
            if item in ship.cargo and ship.cargo[item] >= amount:
                ship.cargo[item] -= amount
                ship.credits += self._items_for_trade.get(item, 0) // 2 * amount
                print(f"{ship.name} sold {amount} {item}(s) for {self._items_for_trade.get(item, 0) // 2 * amount} credits.")
                if ship.cargo[item] == 0:
                    del ship.cargo[item]
                return True
            print(f"Not enough {item} to sell or invalid item.")
            return False

        print("Invalid action. Use 'buy' or 'sell'.")
        return False

    def repair_ship(self, ship, amount: int) -> bool:
        """
        Repairs the ship at the space station.

        Args:
            ship (Ship): The ship to repair.
            amount (int): The amount of health to repair.

        Returns:
            bool: True if the repair was successful, False otherwise.
        """
        total_cost = self._repair_cost * amount
        if ship.credits >= total_cost and ship.health < 100:
            repair_amount = min(amount, 100 - ship.health)  # Can't exceed max health
            ship.credits -= self._repair_cost * repair_amount
            ship.health += repair_amount
            print(f"{ship.name} repaired {repair_amount} health for {self._repair_cost * repair_amount} credits.")
            return True
        print(f"Insufficient credits or health is already full.")
        return False

    def upgrade_ship(self, ship, attribute: str) -> bool:
        """
        Upgrades the ship's attribute at the space station.

        Args:
            ship (Ship): The ship to upgrade.
            attribute (str): The attribute to upgrade ('health' or 'attack').

        Returns:
            bool: True if the upgrade was successful, False otherwise.
        """
        if ship.credits >= self._upgrade_cost:
            if attribute == "health":
                ship.health += 10
                ship.credits -= self._upgrade_cost
                print(f"{ship.name}'s health increased by 10. Current health: {ship.health}.")
                return True
            elif attribute == "attack":
                ship.attack += 1
                ship.credits -= self._upgrade_cost
                print(f"{ship.name}'s attack increased by 1. Current attack: {ship.attack}.")
                return True
            print(f"Invalid attribute for upgrade.")
            return False
        print(f"Not enough credits for upgrade.")
        return False
