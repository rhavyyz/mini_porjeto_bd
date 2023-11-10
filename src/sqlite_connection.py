import sqlite3

class SqliteOperation:

    def __init__(self) -> None:
        self.___connection  = sqlite3.connect("./src/ismaylindo.db")

        self.___cursor = self.___connection.cursor()

    def execute(self, command : str):
        self.___cursor.execute(command)

    def commit(self):
        self.___connection.commit()

    def fetchall(self):
        return self.___cursor.fetchall()


    def __del__(self):
        self.___cursor.close()
        self.___connection.close()