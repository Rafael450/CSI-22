
class Character:
    def __init__(self, strength):
        self.health = 100
        self.strength = strength
        self.dead = False

    def checkDeath(self):
        if self.health <= 0:
            self.dead = True
            return True
        return False

    def takeDamage(self, damage):
        self.health -= damage
        return self.checkDeath()

    def attack(self, enemy): # returns True if the attack killed the enemy
        return enemy.takeDamage(self.strength)

class Ultra(Character):   
    def takeDamage(self, damage): # only takes half of the damage
        return super().takeDamage(damage/2)
    
    def superAttack(self, enemy): # attacks the enemy multiple times until its dead
        while not super().attack(enemy):
            pass
        return True

class Immortal(Character):
    def checkDeath(self):
        if super().checkDeath():
            self.health = 100
            self.dead = False
        return False
    
class Paladin(Character):
    def heal(self, target):
        if not target.checkDeath():
            target.health += 10
    
    def revive(self, target):
        if target.checkDeath():
            target.health = 10
            target.dead = False
    
class UltraImmortal(Immortal, Ultra):
    pass

class UltraPaladin(Paladin, Ultra):
    pass

class ImmortalPaladin(Immortal, Paladin):
    pass

class UltraImmortalPaladin(Ultra, Immortal, Paladin):
    pass
