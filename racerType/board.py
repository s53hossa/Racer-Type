import ast
import os

'''
This module contains all the components surrounding the leaderboard
part of racerType
Date created: Jun. 16, 2022
Last editted: Jun. 23, 2022
Created by: Sahel Hossain
'''

# functions 3 spaces apart are unrelated
# functions 1 space apart fall in the same sub-category


# NAME ----------------------------------------------------------------------------


''' This function takes an appropriate user name '''
def takeName(string):
    name = input(string)
    exclude = "\n\"\/',:;{}[]()1234567890" #pls i tried, dont break my code

    # hopes to prevent all inputs that may cause errors
    while any(char in exclude for char in name) or name == "" or name.lower()  == 'exit': 
        os.system('clear')
        # clarifies to the user what they did wrong
        if " " in name:
            print("Woops! You can't have spaces in there...")
        elif name == "" or name.lower() == 'exit':
            print("Woops! Please input a proper name...")
        else:
            print("Woops! You can't have that symbol in there...")

        # loops back
        name = input(string)
        
    return name

    
# SCORE MANAGEMENT ---------------------------------------------------------------------


''' this function compares the words list to the answers and
returns how many were written correctly '''
def ansCheck(words, ansTracker, ansCounter):
    points = 0
    for (w,a) in zip(words[:ansCounter], ansTracker):
        if w.lower() == a.lower():
            points += 1
    return points

''' this function returns the users WPM and accuracy '''
def scoreCalc(points, ansCounter, time):
    ratio = 60/time # this number scales their WPM accordingly

    acc = round((points)/(ansCounter)*100, 2)
    speed = round((ansCounter)*ratio, 2)

    if points == 0:
        speed = 0
        acc = 0

    return speed, acc

''' This function calculates the users real score. This allows the score to be 
compared to other scores '''
def realScore(numList):
    score = numList[0]*numList[1]
    return score

''' This function adds the users score to leaderBoard.txt in dictionary format '''
def addToBoard(name, speed, acc):
    score = {name: [speed, acc]}
    score = str(score)
    score = score[1:-1]
    score = score +',\n'
    with open('leaderBoard.txt','a') as board:
        board.write(score)


# FILE MANAGEMENT -----------------------------------------------------------------


''' This function seperates the users name from their score '''
# intended to be used in a loop
def readScore(strInDictForm):
    # eg, 'test': [100, 100],
    strInDictForm = strInDictForm.split(':')
    strInDictForm = strInDictForm[-1]
    strInDictForm = strInDictForm[1:-2] 
    strInDictForm = ast.literal_eval(strInDictForm)
    return strInDictForm

''' like readScore() this just seperates the score from the name '''
# intended to be used in a loop
def readName(strInDictForm):
    # eg, 'test': [100, 100],
    name = strInDictForm.split("'")
    name = name[1]
    name = name[0:]
    return name

''' This function shows all names in leaderBoard.txt '''
def allUsers():
    with open('leaderBoard.txt') as board:
        content = board.readlines()
    names = []

    for i in content: # this loop creates a list of just names from leaderBoard.txt
        name = readName(i)
        names.append(name)
    return names

def allScores():
    with open('leaderBoard.txt') as board:
        content = board.readlines()
    scores = []  

    for i in content:
        score = readScore(i) 
        scores.append(score)
    return scores
           
''' This function turns the contents of leaderBoard.txt into a string in dictionary format'''
def dictBoard():
    with open('leaderBoard.txt') as board:
        cont = board.read()
    cont = '{' + cont + '}'
    return cont



''' This function returns a list of numbers. These numbers represent scores, by the same
user, with lesser value. This list is used to remove these scores from the txt file '''
def removeList(name):
    removeList = []
    name = name.lower()
    with open('leaderBoard.txt','r') as board:
        content = board.readlines()
    
    filled = False # this is to indicate whether or not a comparator value is filled
    for line, contents in enumerate(content):
        
        # this fills the comparator value
        if name in contents and filled == False:
            score = readScore(contents)
            comparator = realScore(score)
            comparatorLine = line
            filled = True
        
        # this fills the compared value
        elif name in contents and filled == True:
            score = readScore(contents)
            compared = realScore(score)
            comparedLine = line

            # Comparing
            if comparator > compared: # removes compared line
                removeList.append(comparedLine)
            elif comparator < compared: # removes comparator line, and swaps comparator position
                removeList.append(comparatorLine)
                comparator = compared
                comparatorLine = comparedLine
            elif comparator == compared: # removes compared line
                removeList.append(comparedLine)

    # the list is organised this way to avoid index errors when later removing these lines
    removeList.sort()
    removeList.reverse()
    return removeList

''' This function takes a list of numbers, that represent lines, and removes them from
leaderBoard.txt. This is used to remove repeat scores by the same user with lesser values. '''
def clearRepName(removeList):
    text = "" 
    # this is used to remove all the 'bad' lines from the contents
    with open('leaderBoard.txt', 'r') as board:
        content = board.readlines()
        for i in removeList:
            content.pop(i)
    with open('leaderBoard.txt', 'w') as board:
        # this then adds the new contents without the 'bad' lines to the text
        for i in content:
            text += i
        board.write(text)

''' this function returns a list of numbers that represents the each line in leaderBoard.txt.
The line numbers are in order of highest - lowest score. '''
def boardOrder():
    with open('leaderBoard.txt') as board:
        content = board.readlines()
    
    # creates a list representing each index in content
    indexList = []
    for i in range(0,len(content)):
        indexList.append(i)

    # creates a parrallel list, representing the real scores of each user
    scoreList = []
    for i in content:
        score = readScore(i)
        score = realScore(score)
        scoreList.append(score)

    # Loops for every number
    for i in range(len(scoreList)):
        # compares number to every other number
        for i in range(len(scoreList)):

            if i+1 == len(scoreList):
                continue
            elif scoreList[i] > scoreList[i+1]:
                pass
            elif scoreList[i] < scoreList[i+1]:
                # makes changes to the scores
                placeHolder = scoreList[i]
                scoreList[i] = scoreList[i+1]
                scoreList[i+1] = placeHolder            

                # makes the same changes to the index list
                placeHolder = indexList[i]
                indexList[i] = indexList[i+1]
                indexList[i+1] = placeHolder

    return indexList

''' this function rearranges the lines in leaderBoard.txt according to the index list given '''
def arrangeBoard(indexList):
    with open('leaderBoard.txt') as board:
        content = board.readlines()

    # creates the new contents of the board
    newBoard = []
    for i in indexList:
        for index, contents in enumerate(content):   
            if i == index:
                newBoard.append(contents)
    
    # rewrites the board
    with open('leaderBoard.txt', 'w') as board:
        board.writelines(newBoard)


# FINAL PRODUCTS -----------------------------------------------------------------


''' This function allows the user to search for their score by name. It takes
advantage of the fact that leaderBoard.txt was written in a dictionary format. '''
def searchBoard():
    # converts leaderBoard.txt into a dictionary
    board = dictBoard()
    board = ast.literal_eval(board)

    name = ""
    while name != 'exit':
        print("Input 'exit' to leave.")
        name = input('Input the name you would like to seach here: ')
        os.system('clear')

        # formats place holder name string
        if name in board:
            fName = str(name)
            while len(fName) != 30:
                fName += " "
 
            # Header
            print("Name"+" "*26 + "[Speed, Accuracy]")
            print("—"*50)
            # Score
            print(fName, str(board[name]) +"\n"*10) # i used a dictionary here :D
        
        else:
            print("This user does not exist." +"\n"*10)

''' this function clears all repeats of every name in leaderBoard.txt. It only keeps the highest
score for each user. '''
def clearAllReps():
    names = allUsers()

    for name in names:
        remList = removeList(name)
        clearRepName(remList)

''' this function sorts leaderBoard.txt depending on scores from highest to lowest '''
def sortBoard():
    order = boardOrder()
    arrangeBoard(order)

''' this function prints the contents of leaderBoard.txt. It prints it 
in the form of a table so it is easier to read '''
def printBoard():
    names = allUsers()
    scores = allScores()

    # this seperates the speed and accuracy for each score
    speeds = []
    accs = []
    for s,a in scores:
        speeds.append(str(s))
        accs.append(str(a))

    # Header
    print("Name"+" "*26 + "Speed" + " "*3 + "Accuracy")
    print("—"*50)

    # Table
    for n,s,a in zip(names,speeds,accs):
        # these while loops add empty spaces to the string so when it prints
        # out in the console all items are in neat columns :D
        while len(n) != 30:
            n += " "
        while len(s) != 8:
            s += " "      
        while len(a) != 8:
            a += " "        
        
        print(n,s,a)





