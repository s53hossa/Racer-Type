'''
This module contains all the HEAVILY text based inputs or pieces of code
Date created: Jun. 15, 2022
Last editted: Jun. 23, 2022
Created by: Sahel Hossain
'''

''' This prints out all the start menu options, and returns a valid input'''
def menu():
    print(title())
    print('\nWelcome to racerType!')
    print('Enter the corresponding key below to proceed')
    print('\n'*3)
    print('A: Play')
    print('B: Instructions')
    print('C: Leaderboard')
    print('D: Quit\n')

    # takes valid input
    inp = input("Your answer here: ")
    while inp.lower() != 'a' and inp.lower() != 'b' and inp.lower() != 'c' and inp.lower() != 'd':
        inp = input("Invalid input! Try again: ")
    return inp.lower()



''' This function asks the user which mode they would like to play on, 
and returns their answer '''
def mode():
    time = 0
    print("Select which mode you would like to play on.")
    print()
    print("A: 15 seconds - Super Duper Fast")
    print("B: 30 seconds - Not as Super Fast")
    print("C: 45 seconds - Not as Duper Fast")
    print("D: 60 seconds - Not Fast\n")
    
    # takes valid input
    ans = input("Your answer here: ")
    while ans.lower() != 'a' and ans.lower() != 'b' and ans.lower() != 'c' and ans.lower() != 'd' and ans.lower() != 'dev':
        ans = input("Inavlid input! Try again: ")

    # converts answer to time
    if ans.lower() == 'a':
        time = 15
    elif ans.lower() == 'b':
        time = 30
    elif ans.lower() == 'c':
        time = 45
    elif ans.lower() == 'd':
        time = 60
    elif ans.lower() == 'dev':
        time = 3

    return time



''' This just prints out all the instructions '''
def instructions():
    print("Welcome to the instructions screen!")
    print()
    print("To play all you need to know is how to type.")
    print()
    print("1. To start, input 'A' on the start menu")
    print("2. Enter your username")
    print("3. Select which mode you would like to play on")
    print("4. A short countdown will begin, and your time will start immediately")
    print("5. Type away!")
    print()
    print("The goal of the game is to type as many words possible in the allotted amount of time.")
    print("Now make sure to have fun and type away!")



''' this function displays the leaderboard options, and returns a valid input '''
def boardOptions():
    print("Welcome to the leaderboard. This is where you can see the scores of all players!")
    print()
    print("A: Search score by user")
    print("B: See all scores")
    
    # takes valid input
    ans = input("Your answer here: ")
    while ans.lower() != 'a' and ans.lower() != 'b':
        ans = input("Inavlid input! Try again: ")
    return ans



# ACSII --------------------------------------

def exitScreen():
    print(""" Thanks for playing!

  ______
 /|_||_\`.__
(   _    _ _|
=`-(_)--(_)-'  """)

''' this is just the title art '''
def title():
    title = """   
     ______                                    _____                        ______         
 __ /|_||_\`.__  ___        _ _ __ _ __ ___ _ |_   _|  _ _ __  ___      __ /|_||_\`.__  ___   
 _ (   _    _ _\ ___       | '_/ _` / _/ -_) '_|| || || | '_ \/ -_)     _ (   _    _ _\ ___ 
   =`-(_)--(_)-' _______   |_| \__,_\__\___|_|  |_| \_, | .__/\___|       =`-(_)--(_)-' _______  
__   _____   _____   _____  ____   ____   ___       |__/|_|   ______   _____   ____ _____  _____""" 
    return title