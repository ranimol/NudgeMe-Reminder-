import sqlite3
from sqlite3 import Error
class Database:

    def __init__(self,db):
        try:
            self.conn=sqlite3.connect(db)
            self.cur=self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS nudgeme(id INTEGER PRIMARY KEY,event text ,explanation text,date INTEGER, status INTEGER )")
            self.conn.commit()
        except Error as e:
            print(e)
            
        return None

    def add(self,event,explanation,date,status):
        self.cur.execute("INSERT into nudgeme VALUES (NULL,?,?,?,?)",(event,explanation,date,status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM nudgeme")
        rows=self.cur.fetchall()
        return rows
    
    def search(self,title="",description="",time="",status=""):
        self.cur.execute("SELECT * FROM reminder where title=? OR description=? OR time=? OR status=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM nudgeme where id =?",(id,))
        self.conn.commit()

    def update(self,id,event,explanation,date,status):
        self.cur.execute("UPDATE nudgeme SET event=?,explanation=?,date=?,status=? WHERE id=?",(event,explanation,date,status,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

