import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
	def __init__(self, name, starting_health=100):
		self.abilities = list()
		self.armors = list()
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
	
	def add_ability(self, ability):
		self.abilities.append(ability)
	
	def attack(self):
		total_damage = 0
		for ability in self.abilities:
			total_damage += ability.attack()
		return total_damage

	def add_armor(self, armor):
		self.armors.append(armor)

	def defend(self):
		total_block = 0
		for armor in self.armors:
			total_block += armor.block()
		return total_block

	def take_damage(self, damage):
		defense = self.defend()
		net_damage = damage - defense
		net_damage = max(net_damage, 0)
		self.current_health -= net_damage
		if self.current_health <= 0:
			print(f"{self.name} has been defeated.")

	def is_alive(self):
		return self.current_health > 0

	def fight(self, opponent):
		# Check if at least one hero has abilities
		if not self.abilities and not opponent.abilities:
			print("Draw!")
			return
		# else, start the fighting loop until a hero has won
		while self.is_alive() and opponent.is_alive():
			opponent_damage = self.attack()
			self_damage = opponent.attack()
			opponent.take_damage(opponent_damage)
			self.take_damage(self_damage)
			# after each attack, check if either the hero (self) or the opponent is alive
			if not self.is_alive() and not opponent.is_alive():
				print("Draw")
				break
			elif not self.is_alive():
				print(f"{opponent.name} won!")
				break
			elif not opponent.is_alive():
				print(f"{self.name} won!")
				break
		
	def add_weapon(self, weapon):
		self.abilities.append(weapon)


# Test add_ability()
if __name__ == "__main__":
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities)

  ability2 = Ability("Amazing Debugging", 50)
  hero2 = Hero("Rocko Taco", 500)
  hero2.add_ability(ability2)
  print(hero2.abilities)

# Test attack()
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

# Test defend()
if __name__ == "__main__":
	ability = Ability("Great Debugging", 50)
	armor1 = Armor("Debugging Shield", 10)
	armor2 = Armor("Exception Suit", 5)

	hero = Hero("Debugger", 100)
	hero.add_ability(ability)
	hero.add_armor(armor1)
	hero.add_armor(armor2)

	defense = hero.defend()
	print(f"Hero's defense: {defense}")

# Test Take Damage
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)

# Test is_alive()
if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())  # Expected output: True
    hero.take_damage(15000)
    print(hero.is_alive())  # Expected output: False

# Test Fight!
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

# Test Weapon
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

# # Test Hero Class
# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman", 800)
#     hero2 = Hero("Dumbledore", 500)
#     # Simulate 10 battles
#     for i in range(10):
#         print(f"Battle {i + 1}:")
#         hero1.fight(hero2)


# if __name__ == "__main__":
#   my_hero = Hero("Grace Hopper", 200)
#   print(my_hero.name)
#   print(my_hero.current_health)

# if __name__ == "__main__":
#  hero1 = Hero("Wonder Woman")
#  hero2 = Hero("Dumbledore")

#  hero1.fight(hero2)


