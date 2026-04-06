class Character:
    def __init__(self, health=0, attack=0, healMethods=""):
        self.health = health
        self.attack = attack
        self.healMethods = healMethods
    
    def get_health(self, health):
        self.health = health
        return f"Health: ${self.health}"

    def get_attack(self, attack):
        self.attack = attack
        return f"Attack: ${self.attack}"
    
    def get_heal_methods(self, healMethods):
        self.healMethods = healMethods
        return f"Heal Methods: ${self.healMethods}"
    
character = Character()
print(character.get_health(999))
print(character.get_attack(999))
print(character.get_heal_methods("Potion"))