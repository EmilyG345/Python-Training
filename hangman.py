#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:33:56 2023

@author: emilygoff
"""

#Hangman game
import random
import numpy as np
import re
import sys

def hangman():
    #define the list of words and randomise it. 
    #Create a string to add the guessed letters to.
    #create a variable for the number of go's left
    #create an array that hides the letters of the random word
    
    words = ["broom","colds","yarn","apple","remote","calf"]
    random_word = random.choice(words)
    chosen_letters = ""
    remaining_tries = 10
    arr = np.array(len(random_word)*["_"])
    
    #set the game rounds limit and tell the player the details. Request the letter input
    while ("_" in arr) and (remaining_tries > 0):

            print("The word has",(len(random_word)),"letters", arr,"."," You have", remaining_tries,"round(s) left")
            sys.stdout.flush()
            letter = input("please enter a letter... ")
            
            #check only 1 letter is given
            
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter.")
                continue
            
            if letter in chosen_letters:
                print("Uh oh! Letter has already been guessed - try again!")
                continue
            
            #loop over the random word to check if the letter is present
            #if present, save the index(es) at which it is present
            #replace the index of the array with the correct letter
            #reduce no of tries remaining by 1, add letter to chosen letters string
            #update user on progress
            
            if letter in random_word:
                indices = [i.start() for i in re.finditer(letter, random_word)]
                for n in indices:
                    arr[n] = letter
                    chosen_letters = chosen_letters + letter
                    remaining_tries = remaining_tries -1
                print("correct. Your chosen letters so far are ---> ",chosen_letters)
                    
            
            
            else:
                chosen_letters = chosen_letters + letter
                remaining_tries = remaining_tries -1
                print("incorrect. Your chosen letters so far are --->",chosen_letters)
                continue
    if "_" not in arr:
        print("Congrats! You have guessed the correct word ",random_word)
    else:
        print("Out of tries! The word is ", random_word)
    

hangman()








