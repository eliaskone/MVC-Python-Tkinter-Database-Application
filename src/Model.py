import sqlite3

class Model:
    def __init__(self):
        self.con = sqlite3.connect('books.db')
        self.cur = self.con.cursor()

    def addToTable(self, title, author):
        self.values = (str(title), str(author))
        self.cur.execute("INSERT INTO Books (title, author) values (?,?)", self.values)
        print(self.cur.fetchall())
        self.con.commit()


    def updateTable(self, id, title, author):
        self.values = (str(title), str(author), int(id))
        self.cur.execute("UPDATE Books SET title = ?, author= ? WHERE id = ?", self.values)
        print("Updated: ", self.cur.fetchall())
        self.con.commit()

    def deleteDataFromTable(self, id):
        self.values = (int(id),)
        print("TYPE: ", type(int(id)), "value: ", int(id))
        self.cur.execute("DELETE FROM Books WHERE id = ?", self.values)
        print(self.cur.fetchall())
        self.con.commit()

    def getAllData(self):
        self.cur.execute("SELECT * FROM Books")
        result = self.cur.fetchall()
        print(result)
        self.con.commit()
        return result