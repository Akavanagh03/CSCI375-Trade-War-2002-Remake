class Ship():
    _health: int # How much health a ship has
    _attack: int # How much damage a ship does per attack
    _defense: int # How much the damage recieved is reduced
    _range: int # distance the ship can travel in a single warp
    _credits: int # amount of currency owned (used for trade and repairs, maybe upgrades(?))
    _cargo: dict  = {str: int} # still need to figure out what exactly the types of cargo are
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

# Initiate a ship
    def __init__(self, nm: str, locate: str, hp: int, atk: int, defe: int, rng: int, cdts: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = hp
        self.attack = atk
        self.defense = defe
        self.range = rng
        self.credits = cdts
        self.cargo = crgo
        
    def battle(self, opponent: Ship) -> None:
        # combat loop goes here
        '''
        Basic combat loop:
            while both ships are still alive:
                take action:
                    attack - (roll (rand() % attack)+1 damage)
                    charge - (take a turn to charge weapons, rolling an extra damage die)
                    defend - based on defense (doubles defense)
                    escape - run away (based on warp range) 
                             if escapee has a higher range, they can escape
        '''
        print("FIGHT!")
        
    def trade(self, system):
        #trade function goes here
        '''
        buy, sell, repair, and upgrade
            buy - cargo available system dependent
            sell - same as buy, price varies on system
            repair - repair ship at a certain cost per hp
            upgrade - +1 to a chosen stat (attack, defense, range, hp)
        '''
        print("Trade")
        
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
    def __init__(self, nm: str, locate: str, hp: int, atk: int, defe: int, rng: int, cdts: int, crgo: dict):
        self.name = nm
        self.current_location = locate
        self.health = hp
        self.attack = atk
        self.defense = defe
        self.range = rng