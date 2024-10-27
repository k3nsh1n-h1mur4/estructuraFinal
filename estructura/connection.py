import sqlite3

class Connection:
    def __init__(self):
        pass
    
    def getConnection():
        try:
            with sqlite3.connect('db.sqlite3') as cnx:
                if not cnx:
                    return
                else:
                    return cnx
        except sqlite3.Error as e:
            print(e)