import random
from tkinter import *
import tkinter.messagebox
import Modes
import Constants

def drawBoard(board, root):
    for _ in range(9): # Create 9 buttons
        Button(root, height=10, width=10,text="", command=lambda: Modes.ComputerMode.getComputerMove(board, Constants.COMPUTER_LETTER)).pack(pady=10, padx=10, side=LEFT)

def whoGoesFirst():
    pass

def getPlayerInput(board, move):
    if not validateInput(board, move):
        return None

    move = -1
    while move > 0 and move < 10:
        move = input()
    return move

def placeFigure(board, letter, move):
    # Get the correct button from the board
    # Place the figure
    pass

def isWinner(board, letter):
  return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[7] == letter and board[4] == letter and board[1] == letter) or 
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter))

def validateInput(board, move) -> bool:
    def isSpaceFree(board, move) -> bool:
        return board[move] == " "

    if not isSpaceFree(board, move):
        raise AttributeError("This space is not free.")

    return True