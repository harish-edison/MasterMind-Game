#Importing class MasterMind
from gameContent import MasterMind as mm 
#Importing Libraries
import random

#Input based Welcome Message to greet with name
print("\n ~~~ Welcome to Mastermind Game ~~~ \n Hi gamer, welcome to the Mastermind game \n What is your name?")
Player=input("Enter your name:")
PLAYER_WELCOME = "Hello, "+ Player +", Please follow the given instructions to play the game \n"
print(PLAYER_WELCOME,'\n')

#Loop to play game again
again=1
while again>=1:
    if __name__ == '__main__':

        mm.disp() #Display instructions
        global chosen_num
        chosen_num=mm.guessCode() #Generate 3 digit random number
        mm.game(chosen_num) #Generate game code
        mm.dispResult(again) #Display summary result
        onemore=input("Play Again, Yes or No?")

        #Conditioning for selecting to play again
        if onemore[0] in ['Y','y']:
            again+=1
        else:
            again=0
        
        