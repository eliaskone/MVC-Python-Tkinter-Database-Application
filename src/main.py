from tkinter import *

import Controller
import Model
import View

if __name__ == '__main__':
    root = Tk()
    view = View.View(root)
    model = Model.Model()
    controller = Controller.Controller(model, view)
    root.mainloop()
