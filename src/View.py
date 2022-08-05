import tkinter as tk
import tkinter.ttk as ttk
from src import Constants


class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Database")
        self.root.geometry('900x500+0+0')
        self.createWidgets()

    def createWidgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

        self.labelTitle = ttk.Label(self.root, text="Title: ")
        self.labelTitle.grid(row=0, column=0, padx=5, pady=5)

        self.entryTitleTextVar = tk.StringVar()
        self.entryTitle = ttk.Entry(self.root)
        self.entryTitle.configure(textvariable=self.entryTitleTextVar)
        self.entryTitle.configure(font='Geogia 16 normal')
        self.entryTitle.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        self.labelAuthor = ttk.Label(self.root, text="Author: ")
        self.labelAuthor.grid(row=1, column=0, padx=5, pady=5)

        self.entryAuthorTextVar = tk.StringVar()
        self.entryAuthor = ttk.Entry(self.root)
        self.entryAuthor.configure(textvariable=self.entryAuthorTextVar)
        self.entryAuthor.configure(font='Geogia 16 normal')
        self.entryAuthor.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='ew')
        
        self.addPicure = tk.PhotoImage(file=Constants.ADD_PICTURE)
        self.buttonAdd = ttk.Button(self.root)
        self.buttonAdd.configure(text="Add")
        self.buttonAdd.configure(image=self.addPicure)
        self.buttonAdd.configure(compound='left')
        self.buttonAdd.grid(row=2, column=0, pady=5, sticky='ew')
        
        self.updatePicture = tk.PhotoImage(file=Constants.UPDATE_PICTURE)
        self.buttonUpdate = ttk.Button(self.root)
        self.buttonUpdate.configure(text="Update")
        self.buttonUpdate.configure(image=self.updatePicture)
        self.buttonUpdate.configure(compound='left')
        self.buttonUpdate.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        
        self.deletePicture = tk.PhotoImage(file=Constants.DELETE_PICTURE)
        self.buttonRemove = ttk.Button(self.root)
        self.buttonRemove.configure(text="Remove")
        self.buttonRemove.configure(image=self.deletePicture)
        self.buttonRemove.configure(compound='left')
        self.buttonRemove.grid(row=2, column=2, pady=5, sticky='ew')
        
        # treeview stuffs
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(show='headings')
        self.treeview.configure(columns=('id', 'title', 'author'))
        self.treeview.heading('id', text='Id')
        self.treeview.heading('title', text='Title')
        self.treeview.heading('author', text='Author')
        self.treeview.column('id', width=70, minwidth=70, stretch=False)
        self.treeview.column('title', minwidth=70)
        self.treeview.column('author', minwidth=70)
        self.treeview.grid(row=3, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.root)
        self.scrollbar.grid(row=3, column=3, sticky='ns')

        self.scrollbar.configure(command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        
        # style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('.', font='Georgia 16 normal')
        style.configure('Treeview', rowheight=40)
        style.configure('Treeview.Heading', font='Georgia 16 normal')

    def getTitleData(self):
        return self.entryTitleTextVar.get()

    def getAuthorData(self):
        return self.entryAuthorTextVar.get()

    def setTitle(self, title):
        self.entryTitleTextVar.set(title)

    def setAuthor(self, author):
        self.entryAuthorTextVar.set(author)

    def getTreeviewSelection(self):
        selections = self.treeview.selection()
        if selections:
            selection = selections[0]
            values = self.treeview.item(selection)['values']
            return values

        return None

    def getCursorID(self, event=None):
        selectedData = self.getTreeviewSelection()
        if selectedData:
            return selectedData[0]

        return None

    def getCursorTitle(self):
        selectedData = self.getTreeviewSelection()
        if selectedData:
            return selectedData[1]

        return None

    def getCursorAuthor(self):
        selectedData = self.getTreeviewSelection()
        if selectedData:
            return selectedData[2]

        return None

    def setListbox(self, data):
        self.treeview.delete(*self.treeview.get_children())
        for values in data:
            self.treeview.insert('', 'end', values=(values))

