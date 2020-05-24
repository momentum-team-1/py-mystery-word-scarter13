"""
The computer must select a word at random from the list of words in the file `words.txt` from this repository.
"""


# read the file words.txt.  refer to the open, read, and close commands in the word frequency program.  Refer to the random import for deets on selecting a word at random.  

"""
1. Let the user choose a level of difficulty at the beginning of the program.  Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
"""
# refer to the input section of the house-hunting exercise to get input for difficulty and for guesses.  You will need a function to sort out all words with fewer than 4 characters, and then to select from words with 4-6 characters for easy, 6-8 for normal, and 8 or more for hard.



"""Code structure as follows"""



# function to open file, read text, close file
# function to identify the game and explain the rules
# function to allow user to choose difficulty level
# build a list of words already guessed to prevent duplication?


import random
import string
file = open("words.txt")
text = file.read()
file.close()


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
word = "magnitude"


def add_letter (letter, guesses):
#Determines if a letter or a blank will be shown
    if letter in guesses:
        return letter
    else:
        return "_"

def display_word (word, guesses):
#Make a display of current letters and blanks on the cpommand line 
    output_letters = [add_letter(letter, guesses)
                      for letter in word]
    print(" ".join(output_letters))

def new_game():
    x = input ("Would you like to play again? y or n? ")
    if x == "y":
        #current_guesses = []
        #composition = []
        #output_letters = []
        play_game()
    elif x == "n":
        exit()
# function to randomly select a word of the proper difficulty

def play_game():
    print ("file loaded")
    guesses_remaining = 8
    correct_guesses = 0
    current_guesses =[]
    word_length = len(word)
    print ("")
    print ("Mystery Word Guessing Game")
    print ("")
    print ("Your word is", word_length, "letters long.")
    while word_length != correct_guesses:
        if guesses_remaining == 0:
            print ("I'm sorry.  You are out of guesses.  The word was: ", word)
            new_game()
        else:
            print ("Guesses remaining: ", guesses_remaining)
            print ("")
            composition =[]
            for letter in word:
                composition.append(add_letter(letter, current_guesses))
            display_word(word, current_guesses)
            print("")
            valid = "false"
            while valid == "false":
                new_guess = input ("Which letter do you guess? ")
                new_guess = (new_guess.lower())
                if new_guess in current_guesses:
                    print ("You have guessed that letter already.  Try again!")
                elif len(new_guess) > 1:
                    print ("One guess at a time, please!")
                elif (new_guess) in numbers:
                    print ("Numbers are not a valid input")
                else:
                    current_guesses.append(new_guess)
                    valid = "true"
                    if new_guess in word:
                        print ("Correct!")
                        correct_guesses += 1
                    else:
                        print ("Sorry!")
                        guesses_remaining = guesses_remaining - 1
    print ("Congratulations!  You win!")
    new_game()
    #run the new game question function here



# function to end game
# function to start new game

play_game ()

#if __name__=="__main__":
