import random

class Game:
    def __init__(self):
        self.players = {}
        self.rooms = {}
        self.running = True

    def add_room(self, room):
        self.rooms[room.name] = room

    def add_player(self, player):
        self.players[player.name] = player

    def start(self):
        print("Welcome to a Multi-User Dungeon Game!")
        while self.running:
            for player in self.players.values():
                if player.health > 0:  # Only process commands if player is alive
                    command = input(f"{player.name}, enter command: ").strip()
                    self.process_command(player, command)
                else:
                    print(f"{player.name} is dead. Game over for you.")
                    self.running = False

    def process_command(self, player, command):
        cmd_parts = command.split()
        if not cmd_parts:
            return

        if cmd_parts[0] == 'move':
            if len(cmd_parts) > 1:
                player.move(cmd_parts[1])
            else:
                print("Move where? Please specify a direction.")
        elif cmd_parts[0] == 'look':
            player.look()
        elif cmd_parts[0] == 'attack':
            if len(cmd_parts) > 1:
                player.attack(cmd_parts[1])
            else:
                print("Attack what? Please specify a target.")
        elif cmd_parts[0] == 'inventory':
            player.show_inventory()
        elif cmd_parts[0] == 'status':
            player.show_status()
        elif cmd_parts[0] == 'use':
            if len(cmd_parts) > 1:
                player.use_item(cmd_parts[1])
            else:
                print("Use what? Please specify an item.")
        elif cmd_parts[0] == 'shop':
            player.visit_shop()
        elif cmd_parts[0] == 'pickup':
            player.pickup_item()
        elif cmd_parts[0] == 'quit':
            print(f"{player.name} has left the game.")
            self.running = False
        else:
            print(f"Unknown command: {command}")

class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.health = 100
        self.inventory = []
        self.current_room = start_room
        self.attack_power = 10  # Default attack power
        self.gold = 0  # Starting gold

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction} to {self.current_room.name}.")
            self.look()
        else:
            print("You can't move in that direction.")

    def look(self):
        self.current_room.describe()

    def attack(self, target_name):
        for monster in self.current_room.monsters:
            if monster.name.lower() == target_name.lower():
                if monster.health <= 0:  # Can't attack if already defeated
                    print(f"{monster.name} has already been defeated!")
                    return
                
                print(f"You attack {monster.name}!")
                damage = self.attack_power
                monster.take_damage(damage)  # Deal damage to the monster

                # Show monster health after damage
                print(f"{monster.name} takes {damage} damage. {monster.name}'s health is now {monster.health}.")

                if monster.health > 0:
                    monster.attack(self)  # Monster counter-attacks if still alive
                else:
                    # Drop item if defeated
                    item = monster.drop_item()
                    if item:
                        self.current_room.add_item(item)
                    self.gold += monster.gold  # Add monster's gold to player's gold
                    print(f"{self.name} collects {monster.gold} gold. Total gold: {self.gold}")
                return
        print(f"No {target_name} here to attack.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Player health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory: {', '.join([item.name for item in self.inventory])}")
        else:
            print("Your inventory is empty.")

    def show_status(self):
        print(f"{self.name}'s Status: Health = {self.health}, Attack Power = {self.attack_power}, Gold = {self.gold}")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.apply_effect(self)  # Apply item effect on the player
                self.inventory.remove(item)
                return
        print(f"You don't have a {item_name} in your inventory.")

    def visit_shop(self):
        print("Welcome to the shop!")
        # Example shop items
        shop_items = [
            Item("Potion", "A health potion that restores 20 health.", {'type': 'heal', 'value': 20}),
            Item("Sword", "Increases attack power by 5.", {'type': 'boost', 'value': 5}),
            Item("Armor", "Increases defense.", {'type': 'boost', 'value': 3})
        ]
        for i, item in enumerate(shop_items, 1):
            print(f"{i}. {item.name} - {item.description} - Cost: {10} Gold")
        choice = input("Select an item to buy (number), or type 'exit' to leave: ")
        if choice.isdigit() and 1 <= int(choice) <= len(shop_items):
            selected_item = shop_items[int(choice) - 1]
            if self.gold >= 10:
                self.inventory.append(selected_item)
                self.gold -= 10
                print(f"You bought {selected_item.name}.")
            else:
                print("You don't have enough gold!")
        elif choice.lower() == 'exit':
            print("Thank you for visiting the shop!")
        else:
            print("Invalid choice.")

    def pickup_item(self):
        if self.current_room.items:
            item = self.current_room.items.pop(0)  # Pick the first item in the room
            self.inventory.append(item)
            print(f"You picked up {item.name}.")
        else:
            print("There are no items to pick up.")

class Monster:
    def __init__(self, name, health, attack_power, items=None, gold=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.items = items if items else []
        self.gold = gold  # Gold dropped by the monster

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")
        damage = self.attack_power
        player.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def drop_item(self):
        if self.items:
            dropped_item = self.items.pop(0)  # Drop the first item
            print(f"{self.name} dropped {dropped_item.name}.")
            return dropped_item
        return None

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.monsters = []
        self.exits = {}

    def describe(self):
        print(f"You are in {self.name}. {self.description}")
        if self.items:
            print(f"Items: {', '.join([item.name for item in self.items])}")
        if self.monsters:
            print(f"Monsters: {', '.join([monster.name for monster in self.monsters])}")

        if self.exits:
            exits = ', '.join(self.exits.keys())
            print(f"Available routes: {exits}")
        else:
            print("There are no exits from this room.")

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_monster(self, monster):
        self.monsters.append(monster)

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def apply_effect(self, player):
        if self.effect['type'] == 'heal':
            player.health = min(100, player.health + self.effect['value'])
            print(f"{player.name} uses {self.name} and restores {self.effect['value']} health.")
        elif self.effect['type'] == 'boost':
            player.attack_power += self.effect['value']
            print(f"{player.name} uses {self.name} and increases attack power by {self.effect['value']}.")

def main():
    # Create rooms
    entrance = Room("Entrance", "The entrance of the dungeon. A dark path leads in.")
    hall = Room("Hall", "A large hall with stone walls.")
    treasury = Room("Treasury", "A room filled with glittering treasures.")
    armory = Room("Armory", "A room filled with various weapons and armor.")
    shop_room = Room("Shop Room", "A small room with a shopkeeper ready to sell you items.")
    warning_room = Room("Warning Room", "A room that gives ominous warnings of danger ahead.")
    boss_room = Room("Boss Room", "A dark chamber where the final boss awaits.")

    # Define exits
    entrance.add_exit("north", hall)
    hall.add_exit("south", entrance)
    hall.add_exit("east", treasury)
    hall.add_exit("west", armory)
    treasury.add_exit("west", hall)
    armory.add_exit("east", hall)
    armory.add_exit("north", shop_room)
    shop_room.add_exit("south", armory)
    shop_room.add_exit("east", warning_room)  # Exit to warning room
    warning_room.add_exit("east", boss_room)  # Exit to boss room

    # Create items
    potion = Item("Potion", "Restores 20 health.", {'type': 'heal', 'value': 20})
    sword = Item("Sword", "A sharp sword.", {'type': 'boost', 'value': 5})
    armor = Item("Armor", "A protective armor.", {'type': 'boost', 'value': 3})

    # Create monsters with appropriate drops
    hall_monster = Monster("Goblin", 30, 5, [potion], random.randint(10, 15))
    treasury_monster = Monster("Skeleton", 25, 7, [sword], random.randint(10, 15))
    armory_monster = Monster("Zombie", 20, 6, [armor], random.randint(10, 15))

    # Add monsters to rooms
    hall.add_monster(hall_monster)
    treasury.add_monster(treasury_monster)
    armory.add_monster(armory_monster)

    # Create boss monster
    dragon = Monster("Dragon", 150, 20, [], random.randint(10, 15))  # Dragon does not drop items

    # Add dragon to the boss room
    boss_room.add_monster(dragon)

    # Create game instance
    game = Game()

    # Add rooms to the game
    game.add_room(entrance)
    game.add_room(hall)
    game.add_room(treasury)
    game.add_room(armory)
    game.add_room(shop_room)
    game.add_room(warning_room)
    game.add_room(boss_room)

    # Create players
    player1 = Player("Hero", entrance)
    game.add_player(player1)

    # Start the game
    game.start()

if __name__ == "__main__":
    main()
