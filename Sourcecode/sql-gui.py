import sqlite3
from tkinter import *
from tkinter import ttk

class LibraryDB:

        # Class Fields
        db_conn = 0
        cursor = 0
        curr_Libr = 0

        def __init__(self, root):
            root.title("Library Database")
            root.geometry("500x550")

            title_label = Label(root, text="Title")
            title_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
            self.ttl_entry_vl = StringVar(root, value="")
            self.ttl_entry = ttk.Entry(root, textvariable=self.ttl_entry_vl)
            self.ttl_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

            pub_label = Label(root, text="Publisher")
            pub_label.grid(row=0, column=2, padx=10, pady=10)
            self.pub_entry_vl = StringVar(root, value="")
            self.pub_entry = ttk.Entry(root, textvariable=self.pub_entry_vl)
            self.pub_entry.grid(row=0, column=3, padx=10, pady=10)

            author_label = Label(root, text="Author")
            author_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
            self.author_entry_vl = StringVar(root, value="")
            self.author_entry = ttk.Entry(root, textvariable=self.author_entry_vl)
            self.author_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

            self.submit_button = ttk.Button(root, text="Submit", command=lambda: self.libr_submit())
            self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
            self.update_button = ttk.Button(root, text="Update", command=lambda: self.update_libr())
            self.update_button.grid(row=2, column=1, padx=10, pady=10)

            self.list_box = Listbox(root)
            self.list_box.bind("<<ListboxSelect>>", self.load_library)
            self.list_box.insert(1, "Books")
            self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)
            self.setup_db()
            self.update_listbox()

        def setup_db(self):
            # Open Database
            self.db_conn = sqlite3.connect("Library.db")
            self.cursor = self.db_conn.cursor()
            try:
                self.db_conn.execute("CREATE TABLE Library(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT NOT NULL, publisher TEXT NOT NULL, author TEXT NOT NULL);")
                self.db_conn.commit()
            except sqlite3.OperationalError:
                print("Setup: SQL ERROR")

        def libr_submit(self):
            # Insert Book into Database
            self.db_conn.execute("INSERT INTO Library(title, publisher, author)"+
                                 "VALUES('" +
                                    self.ttl_entry_vl.get()+"', '" +
                                    self.pub_entry_vl.get()+"', '" +
                                    self.author_entry_vl.get() + "');")
            self.db_conn.commit()
            self.ttl_entry.delete(0, "end")
            self.pub_entry.delete(0, "end")
            self.author_entry.delete(0, "end")
            self.update_listbox()

        def update_listbox(self):
            self.list_box.delete(0, END)
            try:
                result = self.cursor.execute("SELECT ID, title, publisher, author FROM Library")
                for row in result:
                    bk_id = row[0]
                    bk_ttl = row[1]
                    bk_pub = row[2]
                    bk_athr = row[3]
                # Put Books in ListBox
                    self.list_box.insert(bk_id,
                                         bk_ttl + " " +
                                         bk_pub +" " +
                                         bk_athr)

            except sqlite3.OperationalError:
                print("Update LB SQL ERROR")

            except:
                print("ERROR")

        def load_library(self, event=None):

            lb_widget = event.widget
            deselectcheck = lb_widget.curselection()
            if len(deselectcheck)>0:
                index = str(lb_widget.curselection()[0] + 1)
                self.curr_Libr = index
            else:
                return
            try:
                result = self.cursor.execute("Select ID, title, publisher, author From "
                                             "Library where ID=" + index)
                for row in result:
                    bk_id = row[0]
                    bk_ttl = row[1]
                    bk_pub = row[2]
                    bk_athr = row[3]

                    self.ttl_entry_vl.set(bk_ttl)
                    self.pub_entry_vl.set(bk_pub)
                    self.author_entry_vl.set(bk_athr)

            except sqlite3.OperationalError:
                print("Load Libr SQL ERROR")

            except:
                print("ERROR")

        def update_libr(self):
            try:
                self.db_conn.execute("Update Library SET title='"+
                                     self.ttl_entry_vl.get()+
                                     "', publisher='" +
                                     self.pub_entry_vl.get()+
                                     "', author='"+
                                     self.author_entry_vl.get()+
                                     "' WHERE ID=" +
                                     self.curr_Libr)
                self.db_conn.commit()

            except sqlite3.OperationalError:
                print("Update DB SQL ERROR")

            except:
                print("ERROR")

            self.ttl_entry.delete(0, "end")
            self.pub_entry.delete(0, "end")
            self.author_entry.delete(0, "end")

            self.update_listbox()


root = Tk()
librDB = LibraryDB(root)
root.mainloop()
