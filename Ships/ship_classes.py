class Ship():
    _health: int
    _attack: int
    _defense: int
    _range: int
    _credits: int
    _cargo: dict  = {str: int} # still need to figure out what exactly the types of cargo are
    _name: str
    _current_location: str

    @property
    def health(self) -> int:
        return self._health
    @health.setter
    def health(self,value: int) -> None:
        self._health = value
    @health.deleter
    def health(self) -> None:
        del self._health
        
    @property
    def attack(self) -> int:
        return self._attack
    @attack.setter
    def attack(self,value: int) -> None:
        self._attack = value
    @attack.deleter
    def attack(self) -> None:
        del self._attack
        
    @property
    def defense(self) -> int:
        return self._defense
    @defense.setter
    def defense(self,value: int) -> None:
        self._defense = value
    @defense.deleter
    def defense(self) -> None:
        del self._defense
        
    @property
    def range(self) -> int:
        return self._range
    @range.setter
    def range(self,value: int) -> None:
        self._range = value
    @range.deleter
    def range(self) -> None:
        del self._range
        
    @property
    def credits(self) -> int:
        return self._credits
    @credits.setter
    def credits(self,value: int) -> None:
        self._credits = value
    @credits.deleter
    def credits(self) -> None:
        del self._credits
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    @name.deleter
    def name(self) -> None:
        del self._name
        
    @property
    def current_location(self) -> str:
        return self._current_location
    @current_location.setter
    def current_location(self, value: str) -> None:
        self._current_location = value
    @current_location.deleter
    def current_location(self) -> None:
        del self._current_location
        
    @property
    def cargo(self) -> dict:
        return self._cargo
    @cargo.setter
    def cargo(self, value: dict) -> None:
        self._cargo = value
    @cargo.deleter
    def cargo(self) -> None:
        del self._cargo
        
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
        print("FIGHT!")
        
    def trade(self, system):
        #trade function goes here
        print("Trade")
        
    def warp(self, system):
        # warp function goes here
        print("Warp")

            