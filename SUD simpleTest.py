import random


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def connect_room(self, other_room, direction):
        self.exits[direction] = other_room

    def get_description(self):
        return f"{self.name}\n{self.description}\nExits: {', '.join(self.exits.keys())}"

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.health = 100  # Player starts with 100 HP
        self.alive = True

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction}.\n")
        else:
            print("You can't go that way!")

    def look(self):
        print(self.current_room.get_description())

    def attack(self, monster):
        damage = random.randint(10, 20)
        print(f"You attack the {monster.name} and deal {damage} damage!")
        monster.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"The monster attacks you and deals {damage} damage! You have {self.health} HP left.")
        if self.health <= 0:
            self.alive = False
            print("You have been defeated... Game over.")

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"The {self.name} has {self.health} HP left.")
        else:
            print(f"The {self.name} has been defeated!")

    def attack(self, player):
        damage = random.randint(5, 15)
        player.take_damage(damage)

def create_dungeon():
    # Create rooms
    entrance = Room("Dungeon Entrance", "You stand at the entrance of a dark and foreboding dungeon.")
    hallway = Room("Dark Hallway", "A long, narrow hallway dimly lit by torches.")
    treasure_room = Room("Treasure Room", "A small room filled with treasure chests!")
    pit = Room("Bottomless Pit", "A deep, dark pit that you do not want to fall into.")

    # Connect rooms
    entrance.connect_room(hallway, "north")
    hallway.connect_room(entrance, "south")
    hallway.connect_room(treasure_room, "east")  # Treasure room guarded
    hallway.connect_room(pit, "west")
    pit.connect_room(hallway, "east")
    
    # Add an exit from the treasure room back to the hallway
    treasure_room.connect_room(hallway, "west")

    return entrance, treasure_room

def combat(player, monster):
    print(f"A {monster.name} appears! Prepare for battle!")
    while monster.health > 0 and player.alive:
        command = input("\nDo you want to 'attack' or 'run'?\n").strip().lower()
        if command == "attack":
            player.attack(monster)
            if monster.health > 0:
                monster.attack(player)
            if not player.alive:
                print("You died in battle.")
                break
        elif command == "run":
            print("You flee back to the hallway!")
            return False
        else:
            print("Invalid command. Type 'attack' or 'run'.")
    return monster.health <= 0

def main():
    print("Welcome to the dungeon!")
    
    # Create dungeon and player
    start_room, treasure_room = create_dungeon()
    player = Player(start_room)
    monster = Monster("Goblin", 50)  # Monster guarding treasure room
    
    # Main game loop
    while player.alive:
        player.look()
        command = input("\nWhat do you want to do? (e.g., 'go north', 'look', 'quit')\n").strip().lower()
        
        if command == "quit":
            print("Goodbye!")
            break
        elif command.startswith("go "):
            direction = command.split()[1]
            if direction == "east" and player.current_room.exits.get(direction) == treasure_room:
                # Combat before entering treasure room
                if combat(player, monster):
                    print("You have defeated the goblin and can now enter the Treasure Room!")
                    player.move(direction)
                else:
                    print("You run back to the hallway.")
            else:
                player.move(direction)
        elif command == "look":
            player.look()
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()
