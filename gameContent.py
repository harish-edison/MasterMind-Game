#Importing libraries
import random

#Creating class 
class MasterMind:
    global  max_number_of_guesses, number_of_digits #Global class variables
    number_of_digits=3
    max_number_of_guesses=10
    
    #To check for color output
    def guessFlagColor(guess, answer):
        SQUARES = {'correct_place': 'Green ','correct_number': 'Yellow ','incorrect_number': 'Red '}

        guessed = []
        pattern = []
        for i, number in enumerate(guess):
            if answer[i] == guess[i]:
                guessed += 'Green '
                pattern.append(SQUARES['correct_place'])
            elif number in answer:
                guessed += 'Yellow '
                pattern.append(SQUARES['correct_number'])
            else:
                guessed += 'Red '
                pattern.append(SQUARES['incorrect_number'])
        return ''.join(guessed), ''.join(pattern)


    #Displaying instructions
    def disp():
        PLAYER_INSTRUCTIONS2 = " ~~~GAME INSTRUCTION~~~\n I am thinking of a 3-digit number. Try to guess what it is. \n Here are some clues: \n When I say:\t That means:\n Yellow\t\t One digit is correct but in the wrong position.\n Green\t\t One digit is correct and in the right position.\n  Red\t\t No digit is correct. \n  For example, if the secret number was 346 and your guess was 843, the clues would be Green Yellow. "
        print(PLAYER_INSTRUCTIONS2)

    #Generating 3 digit random number
    def guessCode():
        lst = [0,1,2,3,4,5,6,7,8,9]
        lst_without_dups = list(set(lst))
        n=random.choices(lst_without_dups,k=3)
        n_str = list(map(str, n))
        #convert the list to string
        str1 = ""
        # traverse in the string
        for element in n_str:
            str1 += element
        return str1
        
    #Game Code
    def game(chosen_num):
       
      
        end_of_game = False
        global already_guessed 
        already_guessed = []
        full_pattern = []
        all_words_guessed = []
        

        while not end_of_game:
            guess = (input("Guess:"))
            while len(guess) != number_of_digits or guess in already_guessed:
                if guess in already_guessed:
                    print("[red]You've already guessed this word!!\n")
                else:
                    print('[red]Please enter a 3 digit number!!\n')
                guess = (input("Guess:"))
            already_guessed.append(guess)
            guessed, pattern = MasterMind.guessFlagColor(guess, chosen_num)
            all_words_guessed.append(guessed)
            full_pattern.append(pattern)

            print(guessed, sep="\n")
            if guess == chosen_num or len(already_guessed) == max_number_of_guesses:
                end_of_game = True
        if len(already_guessed) == max_number_of_guesses and guess != chosen_num:
            print(f'\n[green]Correct Number: {chosen_num}')

    #To find average we append past guesses to a list and then take a sum
    global sumguess
    sumguess=[]

    #To display Summary of game result
    def dispResult(again):
        total_played=again
        no_of_guesses=len(already_guessed)
        print("Total Games Played: ", total_played)
        print("Number of guesses: ", no_of_guesses)
        sumguess.append(no_of_guesses)
        average_guesses=(sum(sumguess)/total_played)
        print("Average Guess per game: ", average_guesses)

  


 

 



