import random
from tkinter import *
import tkinter.messagebox

from Modes import ComputerMode
import Constants

import Application
import Utils
from Utils import drawBoard

root = Tk()
root.geometry(str(Constants.HEIGHT) + "x" + str(Constants.WIDTH))
root.title("App")
root.configure(background='lightblue')

app = Application.App(root)
app.mainloop()
