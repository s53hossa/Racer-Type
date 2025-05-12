import random
import os
import threading
import concurrent.futures
import time
import sys
import getch as g

'''
This module contains all the main components to run the game
component of racerType
Date created: Jun. 6, 2022
Last editted: Jun. 23, 2022
Created by: Sahel Hossain
'''

# functions 3 spaces apart are unrelated
# functions 1 space apart fall in the same sub-category

# RANDOM GENERATION -------------------------------------------------


''' this function creates a list of 500 different numbers in the range of 1000. Each number
represents a line number in words.txt so it is important that numbers do not repeat.'''
def randNumGen():
    # this avoids syntax error for the repition prevention
    lineNums = [0,0,0]

    for i in range(503):
        num = random.randint(1,1001)

        # this prevents lines from repeating
        while lineNums[-1] == num or lineNums[-2] == num or lineNums[-3] == num:
            num = random.randint(1,1000)
        lineNums.append(num)

    lineNums = lineNums[3:] # this removes the first three filler items in the list
    return lineNums

''' this function takes a list of line numbers and converts them into words
this works because every word on words.txt is on a different line '''
def lineReader(lineNums):
    words = []
    for i in lineNums:
        # words.txt is opened every repition to have readline() read from line 1 again
        txt = open('words.txt')
        lineCounter = 0

        for x in range(1,1001):
            lineCounter += 1
            # this holds the word for the coresponding line number
            content = txt.readline()
            content = content.strip()
            
            # once the counter hits the correct line number, it adds the coresponding 
            # word to the list
            if lineCounter == i:
                words.append(content)
                continue 
        txt.close()
    
    return words


# COMPONENTS --------------------------------------------------------------------


''' this function holds the value of the backspace key '''
# this was my last resort btw :c, i had to manually input the backspace key
# into this file using getch()
def backSpace():
    with open('backSpace.txt', 'r') as key:
        backSpace = key.read()
    return backSpace

''' this function acts as a global timer
paired with threading, this can be used as a stopper for other functions '''
def timer(secs):
    global alarm # this allows for it to work alongside other functions

    alarm = True
    time.sleep(secs)
    alarm = False
    return

''' this unreasonably long function acts like the input function, however this time
pressing 'space' acts like it submitted the input :D'''
def takeInput():
    word = ''
    userInp = ''
    # this loop ends when the user presses space indicating a new word
    while userInp != " ":

        # gives the illusion of pressing backspace
        if userInp == backSpace():
            word = word[:-1] 
            print('\r' + ' '*25) # clears the line
            print('\033[F\r'+ word, end="") # goes back up on the line that was cleared

        else: 
            word += userInp
            word = word.strip()
        userInp = g.getche()

    # erases final output 
    print("\r", end="") 
    sys.stdout.write("\033[K")
    return word

''' this function, acts like a word conveyor belt. It feeds the user words
while also taking their input. It reads a list of words. '''
def wordBelt(words):
    # alarm variable is used for the time limit
    global alarm

    belt = [] # this stores the words that are being displayed
    ansTracker = [] # this holds all the inputted answers
    ansCounter = 0 # this counts the number of entries

    index = -1
    while alarm:
        # this acts as a for loop going through every word in words
        index += 1
        i = words[index]

        # prepares the belt to show the user the next 10 words that they will have to type
        belt.append(i)
        if len(belt) == 10: 
            for x in belt:
                print(x, end=" ")
            print()

            # stores answer
            ans = takeInput()
            ansTracker.append(ans)
            ansCounter += 1

            belt.pop(0) # removes first word in the belt
            os.system('clear')

    return ansTracker, ansCounter


# FINAL PRODUCT -----------------------------------------------


''' This function combines all the previous functions to fully run the game '''
def racerType(seconds):

    lineNums = randNumGen()
    words = lineReader(lineNums)

    # count down
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
        os.system('clear')

    # runs the game
    with concurrent.futures.ThreadPoolExecutor() as executor:
        alarm = executor.submit(timer, seconds) # runs timer
        belt = executor.submit(wordBelt, words) # runs wordBelt

        ansTracker, ansCounter = belt.result() # stores return values

    # this is used for the leaderboard
    return ansTracker, ansCounter, words




