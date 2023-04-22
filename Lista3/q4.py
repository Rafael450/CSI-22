class Food:
    def __init__(self, name):
        self.name = name
        self.eaten = False

    @classmethod
    def bestFood(cls): # Class Method
        return cls("Pamonha")
    
    @staticmethod
    def isBestFood(food_name): # Static Method
        if food_name == "Pamonha":
            return True
        return False
    
    def isFoodEaten(self): # Instance Method
        return self.eaten
    
    def eatFood(self): # Instance Method
        if not self.isFoodEaten():
            self.eaten = True
