import random

from tkinter import *
import tkinter.messagebox

import Utils

class ComputerMode():
    @staticmethod
    def chooseRandomMoveFromList(board, moveList):
        possibleMoves = []
        for i in moveList:
            if Utils.validateInput(board, i):
                possibleMoves.append(i)
        
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
    
    # HOMEWORK
    @staticmethod
    def getComputerMove(board, computerLetter):
        # Get move
        move = ComputerMode.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Verify
        try:
            Utils.validateInput(board, move)
            Utils.placeFigure(board, computerLetter, move)
        except AttributeError:
            print("This location is not free.")

        # Check if computer wins
        if Utils.isWinner(board, computerLetter):
            tkinter.messagebox.showinfo("Congratulations!", "'" + computerLetter + "' won!")
    
    @staticmethod
    def getPlayerMove(board, playerLetter, move, root):
        # Validate it
        try:
            # Check if the text of the button is ''
            Utils.validateInput(board, move)
            Utils.placeFigure(board, playerLetter, move)
        except AttributeError:
            print("This location is not free.")

        # Check if player wins
        if Utils.isWinner(board, playerLetter):
            tkinter.messagebox.showinfo("Congratulations!", "'" + playerLetter + "' won!")
            