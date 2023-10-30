import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        total_power = self.current_health + opponent.current_health

        self_win_probability = self.current_health / total_power
        opponent_win_probability = opponent.current_health / total_power

        random_chance = random.random()

        if random_chance <= self_win_probability:
            winner = self
            loser = opponent
        elif random_chance > self_win_probability and random_chance <= self_win_probability + opponent_win_probability:
            winner = opponent
            loser = self

        print(f"{winner.name} defeats {loser.name}!")

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 800)
    hero2 = Hero("Dumbledore", 500)
    # Simulate 10 battles
    for i in range(10):
        print(f"Battle {i + 1}:")
        hero1.fight(hero2)


# if __name__ == "__main__":
#   my_hero = Hero("Grace Hopper", 200)
#   print(my_hero.name)
#   print(my_hero.current_health)

# if __name__ == "__main__":
#  hero1 = Hero("Wonder Woman")
#  hero2 = Hero("Dumbledore")

#  hero1.fight(hero2)


