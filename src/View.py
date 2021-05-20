from tkinter import *
class View:
    def __init__(self, root):
        self.root = root
        self.createWidgets()

    def createWidgets(self):
        self.labelTitle = Label(self.root, text="Title: ")
        self.labelTitle.grid(row=0, column=0, padx=5, pady=5)

        self.entryTitleTextVar = StringVar()
        self.entryTitle = Entry(self.root, textvariable=self.entryTitleTextVar)
        self.entryTitle.grid(row=0, column=1, padx=5, pady=5)

        self.labelAuthor = Label(self.root, text="Author: ")
        self.labelAuthor.grid(row=1, column=0, padx=5, pady=5)

        self.entryAuthorTextVar = StringVar()
        self.entryAuthor = Entry(self.root, textvariable=self.entryAuthorTextVar)
        self.entryAuthor.grid(row=1, column=1, padx=5, pady=5)

        self.buttonAdd = Button(self.root, text="Add")
        self.buttonAdd.grid(row=2, column=0, pady=5)

        self.buttonUpdate = Button(self.root, text="Update")
        self.buttonUpdate.grid(row=2, column=1, pady=5)

        self.buttonRemove = Button(self.root, text="Remove")
        self.buttonRemove.grid(row=2, column=2, pady=5)

        self.listbox = Listbox(self.root, width=60)
        self.listbox.grid(row=3, column=1, padx=5, pady=5)

    def getAuthorData(self):
        return self.entryAuthorTextVar.get()

    def getTitleData(self):
        return self.entryTitleTextVar.get()

    def getCursorID(self, event=None):
        selectedLbData = self.listbox.curselection()
        id = self.listbox.get(selectedLbData)[0]
        return id

    def getCursorTitle(self):
        selectedLbData = self.listbox.curselection()
        title = self.listbox.get(selectedLbData)[1]
        return title

    def getCursorAuthor(self):
        selectedLbData = self.listbox.curselection()
        author = self.listbox.get(selectedLbData)[2]
        return author