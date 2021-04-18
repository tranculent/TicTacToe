from tkinter import *
import Constants
import tkinter.messagebox #popup
from Utils import drawBoard

class App(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack()
        self.root = root
        
        Button(self, text="Versus Computer", font="SegoeUI 30 bold", command=self.vsComputer, bg="lightgreen").pack(pady=10, padx=10)
        Button(self, text="Versus Player", font="SegoeUI 30 bold", command=self.vsPlayer, bg="lightgreen").pack(pady=10, padx=10)
        Button(self, text="Quit", font="SegoeU 30 bold", command=self.quit, bg="lightgreen").pack(pady=10, padx=10)
        self.configure(background="lightblue")
        
    def vsComputer(self):
        temp_root = Toplevel(self.root)
        temp_root.title("Versus Computer")
        temp_root.geometry(str(Constants.HEIGHT) + "x" + str(Constants.WIDTH))
        temp_root.configure(background="darkblue")

        Constants.BOARD = []
        drawBoard(Constants.BOARD, temp_root)
    
    def vsPlayer(self):
        temp_root = Toplevel(self.root)
        temp_root.title("Versus Player")
        temp_root.geometry(str(Constants.HEIGHT) + "x" + str(Constants.WIDTH))
        temp_root.configure(background="darkblue")

        Constants.BOARD = []
        drawBoard(Constants.BOARD, temp_root)
