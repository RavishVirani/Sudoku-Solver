import math
import random
import queue
from Cell import Cell

#Define Global Variables
FILENAME = "soduku.txt"
DEFAULT = [1,2,3,4,5,6,7,8,9]
ROWXCOL = 9
ALPHA = "ABCDEFGHI"


# Generate the Puzzle
def getPuzzle(input_puzzle):
    assert type(input_puzzle) == str
    puzzle = []
    temp = []
    cnt = 0

    for i in input_puzzle:
        if cnt >= 9:
            puzzle.append(temp)
            temp = []
            cnt = 0

        temp.append(i)
        cnt+=1
        
    return puzzle

# Prints the puzzle
def printPuzzle(puzzle):
    assert type(puzzle) == list
    i = 0
    j = 0
    row = 0
    col = 0
    srow = ""
    while row < 13:
        if row in [0, 4, 8, 12]:
            print("-"*25)
            row+=1
        elif (col > 25):
            print(srow)
            col = 0
            row+=1
            i+=1
            j = 0
            srow = ""
        elif col % 2 == 0 and col not in [0, 8, 16, 24]:
            srow += "" +  str(puzzle[i][j]) + " "
            j+=1
            col +=2
        else:
            srow += "| "
            col += 2

# This prints the board in its current state. The way it
# works is that if an index has a list as a value and its length
# is only 1 then it prints the value in the list, otherwise it
# prints a period. Ex. A3 has the values [1,2,3,4,5,6,7,8,9] so
# it prints a period. If it just had [4] it would print 4
def printBoard(board):
    assert type(board) == dict
    i = 0
    j = 0
    row = 0
    col = 0
    srow = ""
    
    temp_str = ""
    cnt = 0
    puzzle = []
    temp = []
    for val in board.values():

        if len(val.domain) == 1:
            temp_str = str(val.domain[0])
        else:
            temp_str = "."
                
        if cnt >= 9:
            puzzle.append(temp)
            temp = []
            cnt = 0
        
        temp.append(temp_str)
        cnt+=1
        temp_str = ""
    puzzle.append(temp)
    
    while row < 13:
        if row in [0, 4, 8, 12]:
            print("-"*25)
            row+=1
        elif (col > 25):
            print(srow)
            col = 0
            row+=1
            i+=1
            j = 0
            srow = ""
        elif col % 2 == 0 and col not in [0, 8, 16, 24]:
            srow += "" +  str(puzzle[i][j]) + " "
            j+=1
            col +=2
        else:
            srow += "| "
            col += 2


# A3 Algorithm
def a3Algorithm(board ,csp):
    
    return

# Gets the all ARCs for soduku puzzle
def generateCSP():
    
    return

# This defines the actual board with all possible values where the periods are 
def generate_A3_board(puzzle):
    board = dict()

    for i in range(9):
        for j in range(9):
            ind = ALPHA[i]+str(j+1)
            if puzzle[i][j] != ".":
                cell = Cell(ind, str(puzzle[i][j]))
                board[ind] = cell
            else:
                cell = Cell(ind, ".")
                board[ind] = cell
    return board


# EACH PUZZLE MUST BE FOLLOWED WITH AN EMPTY LINE AFTERWARDS
def main():
    fh = open(FILENAME, "r")
    for i in fh:
        if i != "\n":
            puzzle = getPuzzle(i)
            print("Original Puzzle")
            printPuzzle(puzzle)
            board = generate_A3_board(puzzle)
            print("Test board Puzzle")
            printBoard(board)
            print()

main()
