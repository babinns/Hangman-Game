#hangman
import random
from words import *
import string

decorator = "================================="
category = ""  
lives = 6

def choose_category():
    global category

    while True:
        category = input("Choose a category: 'verbs', 'colors', 'adjectives' or 'fruits' \n").lower()
        if category in words.keys():
            break    
        
        print("Please choose a valid category")
            
def get_word():
    global category

    word = random.choice(words[category])
    return word.upper()

def hangman():
    global lives
    word = get_word()
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used

        print(f"You have {lives} lives left. You have already used these letters: " + ' '.join(used_letters))

        #current word in dashes 

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: "+ ' '.join(word_list))
        

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Letter is not in word. Try again")
                lives = lives - 1 # Takes away life

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again: ")


        else: 
            print("Invalid character. Please try again: ")
            

    if lives == 0:
        print(f"Game over! the word was {word}")
        lives = 6
    else:
        print(f"the word was {word}")
        lives = 6

#main game loop
while True:  
    play = input("Do you want to play? type 'p' to play or 'q' to exit. ")

    #quit game
    if play == "q":
        break

    choose_category()
    
    hangman()
   





    


