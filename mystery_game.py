


"""
The computer must select a word at random from the list of words in the file `words.txt` from this repository.
"""

# read the file words.txt.  refer to the open, read, and close commands in the word frequency program.  Refer to the random import for deets on selecting a word at random.  

"""
1. Let the user choose a level of difficulty at the beginning of the program.  Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
"""
# refer to the input section of the house-hunting exercise to get input for difficulty and for guesses.  You will need a function to sort out all words with fewer than 4 characters, and then to select from words with 4-6 characters for easy, 6-8 for normal, and 8 or more for hard.

"""
2. At the start of the game, let the user know how many letters the computer's word contains.
"""
# build a string that has enough _ to represent each letter in the word.  Notes on this are in one of the python notebooks.
"""
3. Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
"""
# explain the rules: one guess per round.  case should not matter.  more than one letter should trigger an "invalid entry" notice.
"""
4. Let the user know if their guess appears in the computer's word.
5. Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:
```
B _ _ B A _ D
```
"""
# let the user know if their guess was correct by making that letter appear in the string of blanks.

# the player is allowed 8 incorrect guesses.  display the number of remaining guesses.  If the user guesses the same letter twice, do not take away one of those guesses.  instead, message that they have already guessed that letter

# end game when one of two conditions are met: all letters are revealed or all guesses are exhausted.  If a win, grats.  If a loss, reveal the word.

# ask if they would like to play again.
"""Code structure as follows"""



# function to open file, read text, close file
# function to identify the game and explain the rules



""" 

"""
# function to allow user to choose difficulty level

# create variables for the word, the letters guessed, and the guesses remaining.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
word = "magnitude"
current_guesses = ['a']
guesses_remaining = 8
correct_guesses = 0


def get_input(guesses_remaining, correct_guesses, word_length):
    valid = "false"
    print (guesses_remaining, correct_guesses, word_length)
    while valid == "false":
        new_guess = input ("Which letter do you guess? ")
        new_guess = (new_guess.lower())
        print (new_guess)
        if new_guess in current_guesses:
            print ("You have guessed that letter already.  Try again!")
        elif len(new_guess) > 1:
            print ("One guess at a time, please!")
        elif (new_guess) in numbers:
            print ("Numbers are not a valid input")
        else:
            current_guesses.append(new_guess)
            print (current_guesses)
            valid = "true"
            if new_guess in word:
                print ("Correct!")
                correct_guesses += 1
            else:
                print ("Sorry!")
                guesses_remaining = guesses_remaining - 1
                print (guesses_remaining)


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


# function to randomly select a word of the proper difficulty
# function to run the game
    # function to display remaining chances
    # function to print letters guessed
    # function to display word
    # function to get the player's guess
    # functioun to validate player's guess
        #is it a letter
        #is it a letter that they already guessed
    # function to evaluate game state: win, lose, or continue

    # function to update chances, letters guessed, and word
def play_game():
    print ("")
    print ("Mystery Word Guessing Game")
    print ("")
    word_length = len(word)
    print ("Your word is", word_length, "letters long.")
    while word_length != correct_guesses:
        if guesses_remaining == 0:
            print ("I'm sorry.  You are out of guesses.  The word was ", word)
            #run a new game question function here
        else:
            print ("Guesses remaining: ", guesses_remaining)
            print ("")
            composition =[]
            for letter in word:
                composition.append(add_letter(letter, current_guesses))
            display_word(word, current_guesses)
            print("")
            get_input(guesses_remaining, correct_guesses, word_length)
        #print ("Congratulations!  You win!")
    #run the new game question function here



# function to end game
# function to start new game

play_game ()

#if __name__=="__main__":
#    play_game