from typing import List, Dict

class Planet:
    def __init__(self, name: str, resources: Dict[str, int], connections: List[str]):
        """
        Initializes a planet.

        Args:
            name (str): The name of the planet.
            resources (Dict[str, int]): A dictionary of resources available on the planet.
            connections (List[str]): Names of other planets or spaces connected to this one.
        """
        self._name = name
        self._resources = resources
        self._connections = connections

    @property
    def name(self) -> str:
        """Gets the planet's name."""
        return self._name

    @property
    def resources(self) -> Dict[str, int]:
        """Gets the resources on the planet."""
        return self._resources

    @property
    def connections(self) -> List[str]:
        """Gets the list of connected planets or spaces."""
        return self._connections

    def collect_resources(self, ship, item: str, amount: int) -> bool:
        """
        Allows a ship to collect resources from the planet.

        Args:
            ship (Ship): The ship collecting the resources.
            item (str): The type of resource to collect.
            amount (int): The amount of the resource to collect.

        Returns:
            bool: True if the resources were successfully collected, False otherwise.
        """
        if item in self._resources and self._resources[item] >= amount:
            self._resources[item] -= amount
            ship.cargo[item] = ship.cargo.get(item, 0) + amount
            print(f"{ship.name} collected {amount} units of {item} from {self._name}.")
            return True
        else:
            print(f"Insufficient {item} on {self._name} or invalid resource.")
            return False

    def interactive_resource_collection(self, ship) -> None:
        """
        Allows interactive collection of resources through user input.

        Args:
            ship (Ship): The ship collecting resources.
        """
        print(f"\nResources available on {self._name}:")
        for resource, quantity in self._resources.items():
            print(f"- {resource}: {quantity}")

        while True:
            print("\nChoose a resource to collect or type 'exit':")
            choice = input("Resource: ").strip().lower()

            if choice == 'exit':
                print("Exiting resource collection.")
                break

            if choice in self._resources:
                amount = int(input(f"How much {choice} would you like to collect? "))
                if self.collect_resources(ship, choice, amount):
                    print(f"Successfully collected {amount} {choice}.")
                else:
                    print("Failed to collect resources.")
            else:
                print("Invalid resource selected.")

    def is_connected_to(self, planet_name: str) -> bool:
        """
        Checks if this planet is connected to another planet.

        Args:
            planet_name (str): The name of the planet to check.

        Returns:
            bool: True if connected, False otherwise.
        """
        return planet_name in self._connections

    def add_connection(self, planet_name: str) -> None:
        """
        Adds a connection to another planet.

        Args:
            planet_name (str): The name of the planet to connect to.
        """
        if planet_name not in self._connections:
            self._connections.append(planet_name)
            print(f"{self._name} is now connected to {planet_name}.")

    def display_connections(self) -> None:
        """
        Displays all connections of the planet.
        """
        print(f"{self._name} is connected to: {', '.join(self._connections)}")
