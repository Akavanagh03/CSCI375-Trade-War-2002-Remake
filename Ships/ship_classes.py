import typing
class Ship():
    _health: int # How much health a ship has
    _attack: int # How much damage a ship does per attack
    _defense: int # How much the damage recieved is reduced
    _range: int # distance the ship can travel in a single warp
    _credits: int # amount of currency owned (used for trade and repairs, maybe upgrades(?))
    _cargo: dict  = {str: int} # still need to figure out what exactly the types of cargo are
    _max_cargo: int # maximum quantity a ship can hold in terms of cargo
    _name: str # what the ship is called
    _current_location: str # where the ship is in the universe

# Health Property
    @property
    def health(self) -> int:
        return self._health
    @health.setter
    def health(self,value: int) -> None:
        self._health = value
    @health.deleter
    def health(self) -> None:
        del self._health
# Attack Property
    @property
    def attack(self) -> int:
        return self._attack
    @attack.setter
    def attack(self,value: int) -> None:
        self._attack = value
    @attack.deleter
    def attack(self) -> None:
        del self._attack
# Defense Property  
    @property
    def defense(self) -> int:
        return self._defense
    @defense.setter
    def defense(self,value: int) -> None:
        self._defense = value
    @defense.deleter
    def defense(self) -> None:
        del self._defense
# Warp Range Property   
    @property
    def range(self) -> int:
        return self._range
    @range.setter
    def range(self,value: int) -> None:
        self._range = value
    @range.deleter
    def range(self) -> None:
        del self._range
# Credits Property
    @property
    def credits(self) -> int:
        return self._credits
    @credits.setter
    def credits(self,value: int) -> None:
        self._credits = value
    @credits.deleter
    def credits(self) -> None:
        del self._credits
# Name Property
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    @name.deleter
    def name(self) -> None:
        del self._name
# Location Property
    @property
    def current_location(self) -> str:
        return self._current_location
    @current_location.setter
    def current_location(self, value: str) -> None:
        self._current_location = value
    @current_location.deleter
    def current_location(self) -> None:
        del self._current_location
# Cargo Property
    @property
    def cargo(self) -> dict:
        return self._cargo
    @cargo.setter
    def cargo(self, value: dict) -> None:
        self._cargo = value
    @cargo.deleter
    def cargo(self) -> None:
        del self._cargo
# Max_Cargo Property
    @property
    def max_cargo(self) -> int:
        return self._max_cargo
    @max_cargo.setter
    def max_cargo(self, value: int) -> None:
        self._max_cargo = value
    @max_cargo.deleter
    def max_cargo(self) -> None:
        del self._max_cargo


# Initiate a ship
    def __init__(self, nm: str, locate: str, hp: int, atk: int, defe: int, rng: int, cdts: int, max_crgo: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = hp
        self.attack = atk
        self.defense = defe
        self.range = rng
        self.credits = cdts
        self.max_cargo = max_crgo
        self.cargo = crgo
        
    def battle(self, opponent: typing.Any) -> None:
        print(f"Battle initiated between {self.name} and {opponent.name}!")
        
        while self.health > 0 and opponent.health > 0:
            print(f"\n{self.name}'s Health: {self.health} | {opponent.name}'s Health: {opponent.health}")
            print("Choose an action: [attack, defend, charge, escape]")
            action = input(f"{self.name}'s action: ").strip().lower()

            if action == "attack":
                damage = max(1, self.attack - opponent.defense)  # Minimum 1 damage
                opponent.health -= damage
                print(f"{self.name} attacks {opponent.name} for {damage} damage!")

            elif action == "defend":
                print(f"{self.name} prepares to defend. Incoming damage will be halved for the next turn.")
                self.defense *= 2  # Temporarily doubles defense

            elif action == "charge":
                print(f"{self.name} charges weapons, increasing attack power for the next turn!")
                self.attack += 5  # Temporarily boosts attack

            elif action == "escape":
                if self.range > opponent.range:
                    print(f"{self.name} successfully escapes the battle!")
                    return
                else:
                    print(f"{self.name} fails to escape as {opponent.name}'s range is higher.")
            
            else:
                print("Invalid action. You lose a turn!")

            # Opponent's turn
            if opponent.health > 0:
                opponent_damage = max(1, opponent.attack - self.defense)
                self.health -= opponent_damage
                print(f"{opponent.name} attacks {self.name} for {opponent_damage} damage!")

            # Reset temporary boosts
            self.defense = max(self.defense // 2, 1)
            self.attack = max(self.attack - 5, 1)

        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        elif opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def trade(self, system: dict) -> None:
        print(f"\nWelcome to the trade center at {self.current_location}.")
        print("Options: [buy, sell, repair, upgrade, exit]")
        
        while True:
            action = input("Choose an action: ").strip().lower()

            if action == "buy":
                print("Available items for purchase:")
                for i, (item, price) in enumerate(system.get("items", {}).items(), start=1):
                    print(f"{i}. {item} - {price} credits")
                choice = input("Select an item to buy (number) or type 'exit': ").strip()
                
                if choice.isdigit() and 1 <= int(choice) <= len(system["items"]):
                    item_name = list(system["items"].keys())[int(choice) - 1]
                    price = system["items"][item_name]
                    if self.credits >= price:
                        self.credits -= price
                        self.cargo[item_name] = self.cargo.get(item_name, 0) + 1
                        print(f"Bought {item_name}. Remaining credits: {self.credits}")
                    else:
                        print("Not enough credits.")
                elif choice.lower() == "exit":
                    continue
                else:
                    print("Invalid choice.")

            elif action == "sell":
                print("Your cargo:")
                for i, (item, quantity) in enumerate(self.cargo.items(), start=1):
                    print(f"{i}. {item} x{quantity}")
                choice = input("Select an item to sell (number) or type 'exit': ").strip()

                if choice.isdigit() and 1 <= int(choice) <= len(self.cargo):
                    item_name = list(self.cargo.keys())[int(choice) - 1]
                    price = system["items"].get(item_name, 0) // 2  # Sell price is half
                    self.credits += price
                    self.cargo[item_name] -= 1
                    if self.cargo[item_name] == 0:
                        del self.cargo[item_name]
                    print(f"Sold {item_name}. Current credits: {self.credits}")
                elif choice.lower() == "exit":
                    continue
                else:
                    print("Invalid choice.")

            elif action == "repair":
                cost_per_hp = system.get("repair_cost", 5)
                repair_amount = min(100 - self.health, self.credits // cost_per_hp)
                if repair_amount > 0:
                    self.credits -= repair_amount * cost_per_hp
                    self.health += repair_amount
                    print(f"Repaired {repair_amount} health. Current health: {self.health}, Credits: {self.credits}")
                else:
                    print("Not enough credits or health is already full.")

            elif action == "upgrade":
                print("Upgrade options: [attack, defense, range, health]")
                stat = input("Choose a stat to upgrade: ").strip().lower()
                upgrade_cost = system.get("upgrade_cost", 20)

                if self.credits >= upgrade_cost:
                    if stat == "attack":
                        self.attack += 1
                    elif stat == "defense":
                        self.defense += 1
                    elif stat == "range":
                        self.range += 1
                    elif stat == "health":
                        self.health += 10
                    else:
                        print("Invalid stat.")
                        continue
                    self.credits -= upgrade_cost
                    print(f"Upgraded {stat}. Current stats: Attack={self.attack}, Defense={self.defense}, Range={self.range}, Health={self.health}")
                else:
                    print("Not enough credits for an upgrade.")

            elif action == "exit":
                print("Exiting the trade center.")
                break

            else:
                print("Invalid action.")


    
    def warp(self, system):
        # warp function goes here
        '''
        based on warp range, allows ship to reach a certain distance per warp
            ex. 
                range of 3
                can warp the same in 1 turn
                as a range of 1
                can warp in 3 turns
        '''
        print("Warp")

class Fighter(Ship):
    def __init__(self, nm: str, locate: str, cdts: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = 90
        self.attack = 60
        self.defense = 10
        self.range = 2
        self.cargo = crgo
        self.max_cargo = 100
        self.credits = cdts
    
class Freighter(Ship):
    def __init__(self, nm: str, locate: str, cdts: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = 110
        self.attack = 40
        self.defense = 20
        self.range = 3
        self.cargo = crgo
        self.max_cargo = 200
        self.credits = cdts

class Defender(Ship):
    def __init__(self, nm: str, locate: str, cdts: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = 130
        self.attack = 30
        self.defense = 30
        self.range = 3
        self.cargo = crgo
        self.max_cargo = 100
        self.credits = cdts

class Explorer(Ship):
        def __init__(self, nm: str, locate: str, cdts: int, crgo: dict):
            self.name = nm
            self.current_location = locate
            self.health = 100
            self.attack = 50
            self.defense = 25
            self.range = 5
            self.cargo = crgo
            self.max_cargo = 150
            self.credits = cdts

if __name__ == "__main__":
    cargo: dict = {
        "salt": 12,
        "scrap": 3
    }
    ship1: Explorer = Explorer("test-1","home",1000,cargo)
    ship2: Freighter = Freighter("test-2","home",1000,cargo)
    
    ship1.battle(ship2)