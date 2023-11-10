import sqlite3

class SqliteOperation:

    def __init__(self) -> None:
        self.___connection  = sqlite3.connect("./src/ismaylindo.db")

        self.___cursor = self.___connection.cursor()

    def execute(self, command : str):
        try:
            self.___cursor.execute(command)
            return False
        except sqlite3.IntegrityError as error:
            return error.__str__()

            


    def commit(self):
        try:
            self.___connection.commit()
            return False
        except sqlite3.IntegrityError as error:
            return True

    def fetchall(self):
        try:
            return self.___cursor.fetchall()
        except sqlite3.IntegrityError as error:
            return []

    def __del__(self):
        self.___cursor.close()
        self.___connection.close()