def battle(self, opponent: Ship) -> None:
    print(f"Battle initiated between {self.name} and {opponent.name}!")

    while self.health > 0 and opponent.health > 0:
        print(
            f"\n{self.name}'s Health: {self.health} | {opponent.name}'s Health: {opponent.health}")
        print("Choose an action: [attack, defend, charge, escape]")
        action = input(f"{self.name}'s action: ").strip().lower()

        if action == "attack":
            damage = max(1, self.attack - opponent.defense)  # Minimum 1 damage
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        elif action == "defend":
            print(
                f"{self.name} prepares to defend. Incoming damage will be halved for the next turn.")
            self.defense *= 2  # Temporarily doubles defense

        elif action == "charge":
            print(
                f"{self.name} charges weapons, increasing attack power for the next turn!")
            self.attack += 5  # Temporarily boosts attack

        elif action == "escape":
            if self.range > opponent.range:
                print(f"{self.name} successfully escapes the battle!")
                return
            else:
                print(
                    f"{self.name} fails to escape as {opponent.name}'s range is higher.")

        else:
            print("Invalid action. You lose a turn!")

        # Opponent's turn
        if opponent.health > 0:
            opponent_damage = max(1, opponent.attack - self.defense)
            self.health -= opponent_damage
            print(
                f"{opponent.name} attacks {self.name} for {opponent_damage} damage!")

        # Reset temporary boosts
        self.defense = max(self.defense // 2, 1)
        self.attack = max(self.attack - 5, 1)

    if self.health <= 0:
        print(f"{self.name} has been defeated!")
    elif opponent.health <= 0:
        print(f"{opponent.name} has been defeated!")
