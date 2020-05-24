#define constants, get words and difficulty lists
import random
file = open("words.txt")
text = file.read()
file.close()
upper_case = text.upper()
all_words = upper_case.split()
easy_words = []
normal_words = []
hard_words = []
for each in all_words:
    if 3 < len(each) <= 6:
        easy_words.append(each)
    elif 6 < len(each) <= 8:
        normal_words.append(each)
    elif len(each) > 8:
        hard_words.append(each)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]


#def instructions()
"""print instructions"""
def set_up_game ():
    #select a difficulty, quit, or get instructions. 
    print ("")
    print ("Mystery Word Guessing Game")
    print ("")
    print ("Would you like to start a new game?")
    print ("Enter (E)asy, (N)ormal, (H)ard or (Q)uit")
    #print ("Enter I for Instructions")
    entry = False
    valid_entries = ["E", "N", "H", "Q"]
    while entry != True:
        difficulty = input ("Make your selection: ")
        difficulty = (difficulty.upper())
        if difficulty not in valid_entries:
            print ("Invalid Entry")
        else:
            entry = True
    return difficulty

def get_word (difficulty):
    if difficulty == "E":
        word = random.choice(easy_words)
    elif difficulty == "N":
        word = random.choice(normal_words)
    elif difficulty == "H":
        word = random.choice(hard_words)
    elif difficulty == "Q":
        exit()
    #elif difficulty == "I":
        #call instructions, then call begin_game again
    return word

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

def count_letters (word):
    word_letters = []
    for letter in word:
        if letter not in word_letters:
            word_letters.append(letter)
    letter_total = len(word_letters)
    return letter_total

def begin_game ():
    difficulty = (set_up_game())
    word = (get_word(difficulty))
    guesses_remaining = 8
    correct_guesses = 0
    current_guesses =[]
    composition = ["_"]
    word_length = len(word)
    letter_total = (count_letters(word))
    print ("Your word is", word_length, "letters long.")
    while correct_guesses != letter_total:
        #print (composition)
        if guesses_remaining == 0:
            print ("I'm sorry.  You are out of guesses.  The word was: ", word)
            begin_game()
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
                new_guess = (new_guess.upper())
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
    composition =[]
    for letter in word:
        composition.append(add_letter(letter, current_guesses))
    display_word(word, current_guesses)
    print ("Congratulations!  You win!")
    print ("")

    begin_game()





#play_game ()

#if __name__=="__main__":

begin_game()
