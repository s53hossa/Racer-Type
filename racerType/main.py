import racerType as rt
import board as b
import text as t
import os
# Type 'pip install getch' into the console to make the code work
# if it doesnt work the first time try it again
# I also fixed the file bug, if it doesn't work however just delete all
# the contents of leaderBoard.txt and try again

'''
RacerType!
This module runs the game. It combines functions from all the other modules to fully work.
Created by: Sahel Hossain
Date Created: June 20, 2022
Last Editted: June 23, 2022
'''

# for convenience, it just clears the console
def clear():
    os.system('clear')

# for convenience, it just prompts the user to leave
def leave():
    print('\n'*5)
    input("Press 'enter' to continue.")
    clear()    



''' THIS IS RACERTYPE!!! this function runs all components of racerType at once, running the game.'''
def main():
    start = ''
    while start != "leave now pls":
        start = t.menu()
        
        # PLAY
        if start.lower() == 'a':
            clear()

            # name ----------------------
            name = b.takeName("Please type your name here: ")
            leave()
            
            # time setting --------------
            mode = t.mode()
            leave()

            # start game ------------------
            ansTracker, ansCounter, words = rt.racerType(mode)

            # board management ----------------------
            points = b.ansCheck(words, ansTracker, ansCounter)
            speed, acc = b.scoreCalc(points, ansCounter, mode)  
            b.addToBoard(name, speed, acc)
            
            # end screen  ----------------------
            print(f"Congrats {name}, you achieved a score of {speed} WMP, at {acc}% accuracy!")
            
            leave()

        # INSTRUCTIONS
        if start.lower() == 'b':
            clear()
            t.instructions()
            leave()

        # LEADERBOARD
        if start.lower() == 'c':
            clear()
            # sets up leaderBoard.txt
            b.clearAllReps()
            b.sortBoard()

            inp = t.boardOptions()     
            # search score by user
            if inp.lower() == 'a':
                clear()
                b.searchBoard()
                clear()          
            # see all scores
            if inp.lower() == 'b':
                clear()  
                b.printBoard()
                leave()              

        # QUIT
        if start.lower() == 'd':
            clear()
            t.exitScreen()
            quit()
        
main()





# OMG NO NOT AGAIN!!!













# WATCH OUT IT--



#    ||
#    OO
#   (\/)
#  /    \
# ||    ||
#  \    /
#   |/\|
#  /|  |\


# ITS THE BONUS CHICKEN!!!

# Special Ability - Gamble for bonus mark 

# import random
#
# def bonus(): 
#   bonus = 0
#   mark = random.randint(0,100)
#   if mark > 50:
#       bonus += 1
#   else:
#       pass
#
#   print(mark)
# 
# bonus()
