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

