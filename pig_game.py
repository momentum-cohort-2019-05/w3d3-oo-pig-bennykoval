from random import randint 

#class PermissionStartGame: 
    #"""An object that asks user for permission to start the game"""
    #user_input_start_game = ("Would you like to play a game of Pig? Please type (Y)es or (N)o: ").lower()

    #def __init__(self):
        #self.player1 = Player("B")
        #self.player2 = Player("Z")
        
    #if user_input_start_game == "Y" or "yes":
        #return 


#class StartGame: 

#class Player:
    #def __init__(self, name)
        #self.name = name
        #self.score = 0

class Dice:
    """A dice object that randomly selects a number between 1 and 6"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return(print(randint(1,6), self.sides))


    

