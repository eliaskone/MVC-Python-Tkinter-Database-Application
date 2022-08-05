from tkinter import *

from src import Controller
from src import Model
from src import View

if __name__ == '__main__':
    root = Tk()
    view = View.View(root)
    model = Model.Model()
    controller = Controller.Controller(model, view)
    root.mainloop()
