from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    self.team_one = Team("Team One")
    self.team_two = Team("Team Two")
  
  def create_ability(self):
    name = input("What is the ability name? ")
    max_damage = input("What is the max damage of the ability? ")
    return Ability(name, max_damage)

  def create_weapon(self):
    name = input("What is the weapon name? ")
    max_damage = int(input("What is the max damage of the weapon? "))
    return Weapon(name, max_damage)
  
  def create_armor(self):
    name = input("What is the armor name? ")
    max_defense = int(input("What is the max defense of the armor? "))
    return Armor(name, max_defense)
  
  def create_hero(self):
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        ability = self.create_ability()
        hero.add_ability(ability)
      elif add_item == "2":
        weapon = self.create_weapon()
        hero.add_weapon(weapon)
      elif add_item == "3":
        armor = self.create_armor()
        hero.add_armor(armor)
    return hero
  
  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)
  
  def build_team_two(self):
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_two.add_hero(hero)
  
  def team_battles(self):
    self.team_one.attack(self.team_two)
  
  def show_stats(self):
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # Team One Stats
    team_one_kills = 0
    team_one_deaths = 0
    for hero in self.team_one.heroes:
        team_one_kills += hero.kills
        team_one_deaths += hero.deaths
    if team_one_deaths == 0:
        team_one_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_one_kills/team_one_deaths)) 

    # Team Two Stats
    team_two_kills = 0
    team_two_deaths = 0
    for hero in self.team_two.heroes:
        team_two_kills += hero.kills
        team_two_deaths += hero.deaths
    if team_two_deaths == 0:
        team_two_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team_two_kills/team_two_deaths)) 

    # Survivors from Team One
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("Survived from " + self.team_one.name + ": " + hero.name)

    # Survivors from Team Two
    for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("Survived from " + self.team_two.name + ": " + hero.name)

# Testing Arena
# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()          

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battles()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()   