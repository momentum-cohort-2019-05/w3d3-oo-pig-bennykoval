from random import randint 

class Die:
    """A dice object that randomly selects a number between 1 and 6"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        roll_result = randint(1,self.sides)
        print(f"You rolled a {roll_result}.")
        
        #return value later

class Game:
    def __init__(self):
        pass

    def add_to_score(self, roll_result, score):
        temp_score = 0
        if roll_result == range(2,7):
            temp_score += roll_result
        else:
            return score
    

class StartGame: 
    """An object that asks user for permission to start the game"""

    #def __init__(self, player1, player2):
        #self.player1 = player1
        #self.player2 = player2

    def __init__(self):
        pass
        
    def player_consent(self):
        user_input_start_game = input("Would you like to play a game of Pig? Please type (Y)es or (N)o: ")
        user_input_start_game = user_input_start_game.lower()

        if user_input_start_game == "y" or "yes":
            start_game = Die()
            start_game.roll() 

        elif user_input_start_game == "n" or "not":
            print("Press any key to escape. See you next time!")

        else: 
            print("That is not a valid input! Please type (Y)es or (N)o to continue.")

if __name__ == "__main__":
    d6 = Die()
    game_start = StartGame()
    game_start.player_consent()
    

    
