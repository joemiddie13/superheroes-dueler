import random

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()
  
  def remove_hero(self, name):
    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
      # if we find them, remove them from the list
      if hero.name == name:
        self.heroes.remove(hero)
        # set our indicator to True
        foundHero = True
    # if we looped through our list and did not found our hero,
    # the indicator would have never changed, so return 0
    if not foundHero:
      return 0
  
  def view_all_heroes(self):
    for hero in self.heroes:
      print(hero.name)
  
  def add_hero(self, hero):
    self.heroes.append(hero)

  def stats(self):
    for hero in self.heroes:
        if hero.deaths == 0:
            kd = hero.kills
        else:
            kd = hero.kills / hero.deaths
  
  def revive_heroes(self, health=100):
    for hero in self.heroes:
      hero.current_health = hero.starting_health
  
  def attack(self, other_team):
    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)
    
    while len(living_heroes) > 0 and len(living_opponents)> 0:
      # Randomly select a living hero from each team
      hero = random.choice(living_heroes)
      opponent = random.choice(living_opponents)
      # Have the heroes fight each other
      hero.fight(opponent)
      # Update the list of living_heroes and living_opponents
      living_heroes = [hero for hero in living_heroes if hero.current_health > 0]
      living_opponents = [hero for hero in living_opponents if hero.current_health > 0]