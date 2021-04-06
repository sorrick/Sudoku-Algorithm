# This program is to solve sudokus where the user can enter the numbers in a sudoku and
# this algorithm will solve it

import pprint
import pygame

#print(pygame.font.get_fonts())



# Function is the main function that solves the sudoku. Uses backtracking
# algorithm.
def solve(board):
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


#

def valid(board, number, position):
    # Checks if the number entered works for the row
    for i in range(len(board[0])):
        if board[position[0][i]] == number and position[1] != i:
            return False

    # Checks if number entered works for the column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Here we need to check the whole square to make sure no numbers repeat
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


# finds empty board square and returns the coordinates
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


# Now we need to print out the board

def print(board):
    for i in range(len(board)):
        #Prints the outside box of the sudoku
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        #prints out the edges of the squares
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+ " ", end="")