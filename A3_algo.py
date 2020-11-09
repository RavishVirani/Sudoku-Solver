import math
import random
from queue import Queue
from Cell import Cell, Constraint
from backtrack import *

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


# AC3 Algorithm
def ac3Algorithm(board, csp, arcs):
    
    while len(csp) > 0:
        vals = csp.pop(0)

        val1 = board[vals[0]]
        val2 = board[vals[1]]

        temp = val1.domain.copy()
        const = Constraint(val1, val2)
        const.arc_consist()
        if len(val2.domain) == 0:
            return None, None 
        if (val1.domain != temp):
            for i in range(len(arcs)):
                if arcs[i][1] == vals[0] and (arcs[i] not in csp):
                    csp.append(arcs[i])
        print(len(csp))
    return board, csp

# Gets the all ARCs for soduku puzzle
def generateCSP(board):
    csp = []
    arcs = []
    for start, val in board.items():
        for i in range(len(val.relations)):
            csp.append((start, val.relations[i]))
            arcs.append((start, val.relations[i]))
            
    
    return csp, arcs

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

# This is purely a testing function. Has no real use in the actual program
# This is used to test what spaces have multiple values left over
def test_domain(board):
    for i,j in board.items():
        if len(j.domain) > 1:
            return False
    
    return True


# EACH PUZZLE MUST BE FOLLOWED WITH AN EMPTY LINE AFTERWARDS
def main():
    invalid = False
    fh = open(FILENAME, "r")
    for i in fh:
        if i != "\n":
            puzzle = getPuzzle(i)
            print("Original Puzzle")
            printPuzzle(puzzle)
            print()

            board = generate_A3_board(puzzle)
            csp, arcs = generateCSP(board)
            board, csp = ac3Algorithm(board, csp, arcs)

            if (board == None and csp == None):
                print("Invalid Puzzle")
                invalid = True

            if not invalid:
                val = test_domain(board)
                if val == False:
                    print("AC3 couldn't solve the puzzle")
                    printBoard(board)
                    #assignment = backtracking_search(csp, board)
                    print("After the Backtracking Algorithm")                                        
                    print(assignment)
                else:
                    print("AC3 solved the puzzle")
                    print()
                    printBoard(board)
            print()

main()
