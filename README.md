# Sudoku-Solver
CP-468 Group 15 Assignment 2

# Introduction
In a standard Sudoku puzzle (9x9 grid), there are 81 variables/tiles in total. Each variable is named by its row and its column, and must be assigned a value from 1 to 9, subject to the constraint that no two cells in the same row, column, or box may contain the same value. The initial configuration of sudoku is a partially filled board. The objective is to solve the puzzle such that all the constraints are satisfied. As the given problem has a list of constraints to be satisfied, CSP solutions work efficiently for the sudoku problem as well.

# Representation
We chose to represent the sudoku puzzle as a dictionary of values in python. Each position of the board is represented by an alphanumeric situating list. The row are represented by the letters A-I and the columns are represented to by the numbers 1-9. The positions are constantly composed with the row represented first followed by the column. Ex. "A2". At each position, there is a cell object that contains the lists of cells that it is identified with just as the current area of qualities that the cell can hold. This is the way the sudoku board is spoken to as a CSP.

# Code Description
A3_algo : Implemets the AC3 algorithm, Gets the all ARCs for soduku puzzle, prints the Sudoku puzzle and formats the output.
Cell : Defines the cells of the Sudoku puzzle
backtrack : Implementation of Backtracking through Minimum Remaining Values and the Degree heuristic

# Environment
Language : Python-3

# How to run?
Input the sudoku puzzle in sudoku.txt with "." for empty spaces.

Run python A3_algo.py

The output will display the unsolved puzzle, length of queue and finally the solved puzzle.

# Sample Runs
A note about inputs. Must have 81 characters on a line and the file MUST end with a new line

Sample input 1
In sodoku.txt
13........57......8.6.............2..89..7..5....9538..7...3..15..1.29.3...5.67..

Sample output 1
(PUZZLE 1)
Original Puzzle


| 1 3 . | . . . | . . . |<br/>
| . 5 7 | . . . | . . . |<br/>
| 8 . 6 | . . . | . . . |<br/>

| . . . | . . . | . 2 . |<br/>
| . 8 9 | . . 7 | . . 5 |<br/>
| . . . | . 9 5 | 3 8 . |<br/>

| . 7 . | . . 3 | . . 1 |<br/>
| 5 . . | 1 . 2 | 9 . 3 |<br/>
| . . . | 5 . 6 | 7 . . |<br/>


Length of Queue at each steps:
1620 -> 1619 -> 1618 -> 1617 -> 1616 -> 1615 -> 1614 -> 1613 -> 1612 -> 1611 -> 1610 ->
 ...   	<- Many lines were redacted here for the sample output
14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0

AC3 solved the puzzle!!!
After AC3 Algorithm Puzzle

| 1 3 4 | 2 6 9 | 5 7 8 |<br/>
| 2 5 7 | 8 3 4 | 1 9 6 |<br/>
| 8 9 6 | 7 5 1 | 2 3 4 |<br/>

| 7 6 5 | 3 1 8 | 4 2 9 |<br/>
| 3 8 9 | 4 2 7 | 6 1 5 |<br/>
| 4 2 1 | 6 9 5 | 3 8 7 |<br/>

| 6 7 2 | 9 4 3 | 8 5 1 |<br/>
| 5 4 8 | 1 7 2 | 9 6 3 |<br/>
| 9 1 3 | 5 8 6 | 7 4 2 |<br/>


Sample input 2
In sodoku.txt
2..4.78........9276....8.....2....9.987...512.4....6.....8....5831........43.2..8
   	 
Sample output 2
(PUZZLE 1)
Original Puzzle

| 2 . . | 4 . 7 | 8 . . |<br/>
| . . . | . . . | 9 2 7 |<br/>
| 6 . . | . . 8 | . . . |<br/>

| . . 2 | . . . | . 9 . |<br/>
| 9 8 7 | . . . | 5 1 2 |<br/>
| . 4 . | . . . | 6 . . |<br/>

| . . . | 8 . . | . . 5 |<br/>
| 8 3 1 | . . . | . . . |<br/>
| . . 4 | 3 . 2 | . . 8 |<br/>


Length of Queue at each steps:
1620 -> 1619 -> 1618 -> 1617 -> 1616 -> 1615 -> 1614 -> 1613 -> 1612 -> 1611 -> 1610 ->
…      	<- Many lines were redacted here for the sample output
17 -> 16 -> 15 -> 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0

AC3 couldn't solve the puzzle
After AC3 Algorithm Puzzle

| 2 . . | 4 . 7 | 8 . 6 |<br/>
| 4 . . | . . . | 9 2 7 |<br/>
| 6 . . | . . 8 | . . 1 |<br/>

| 3 6 2 | . . . | 7 9 4 |<br/>
| 9 8 7 | 6 . . | 5 1 2 |<br/>
| 1 4 5 | . . 9 | 6 8 3 |<br/>

| 7 2 6 | 8 . . | . . 5 |<br/>
| 8 3 1 | . . . | . . 9 |<br/>
| 5 9 4 | 3 . 2 | 1 . 8 |<br/>

After the Backtracking Algorithm

| 2 5 9 | 4 1 7 | 8 3 6 |<br/>
| 4 1 8 | 5 3 6 | 9 2 7 |<br/>
| 6 7 3 | 9 2 8 | 4 5 1 |<br/>

| 3 6 2 | 1 8 5 | 7 9 4 |<br/>
| 9 8 7 | 6 4 3 | 5 1 2 |<br/>
| 1 4 5 | 2 7 9 | 6 8 3 |<br/>

| 7 2 6 | 8 9 1 | 3 4 5 |<br/>
| 8 3 1 | 7 5 4 | 2 6 9 |<br/>
| 5 9 4 | 3 6 2 | 1 7 8 |<br/>



Sample Input 3
In soduku.txt
1.......1........................................................................


Sample Output 3
(PUZZLE 1)
Original Puzzle

| 1 . . | . . . | . . 1 |<br/>
| . . . | . . . | . . . |<br/>
| . . . | . . . | . . . |<br/>

| . . . | . . . | . . . |<br/>
| . . . | . . . | . . . |<br/>
| . . . | . . . | . . . |<br/>

| . . . | . . . | . . . |<br/>
| . . . | . . . | . . . |<br/>
| . . . | . . . | . . . |<br/>


Length of Queue at each steps:
1620 -> 1619 -> 1618 -> 1617 -> 1616 -> 1615 -> 1614 -> 1613 -> 1612 -> 1611 -> 1610 -> 1609 -> 1608 -> 1607 -> 1606 -> 1605 -> 1604 -> 1603 -> 1602 -> 1601 -> 1600

Invalid Puzzle!!!
