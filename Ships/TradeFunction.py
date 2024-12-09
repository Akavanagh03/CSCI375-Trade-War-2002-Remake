def trade(self, system: dict) -> None:
    print(f"\nWelcome to the trade center at {self.current_location}.")
    print("Options: [buy, sell, repair, upgrade, exit]")

    while True:
        action = input("Choose an action: ").strip().lower()

        if action == "buy":
            print("Available items for purchase:")
            for i, (item, price) in enumerate(
                    system.get("items", {}).items(), start=1):
                print(f"{i}. {item} - {price} credits")
            choice = input(
                "Select an item to buy (number) or type 'exit': ").strip()

            if choice.isdigit() and 1 <= int(choice) <= len(system["items"]):
                item_name = list(system["items"].keys())[int(choice) - 1]
                price = system["items"][item_name]
                if self.credits >= price:
                    self.credits -= price
                    self.cargo[item_name] = self.cargo.get(item_name, 0) + 1
                    print(
                        f"Bought {item_name}. Remaining credits: {self.credits}")
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
            choice = input(
                "Select an item to sell (number) or type 'exit': ").strip()

            if choice.isdigit() and 1 <= int(choice) <= len(self.cargo):
                item_name = list(self.cargo.keys())[int(choice) - 1]
                price = system["items"].get(
                    item_name, 0) // 2  # Sell price is half
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
                print(
                    f"Repaired {repair_amount} health. Current health: {self.health}, Credits: {self.credits}")
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
                print(
                    f"Upgraded {stat}. Current stats: Attack={self.attack}, Defense={self.defense}, Range={self.range}, Health={self.health}")
            else:
                print("Not enough credits for an upgrade.")

        elif action == "exit":
            print("Exiting the trade center.")
            break

        else:
            print("Invalid action.")
