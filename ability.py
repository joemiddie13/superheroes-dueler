import random

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    return random.randint(0, int(self.max_damage))





# Test Ability Class

if __name__ == "__main__":
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())