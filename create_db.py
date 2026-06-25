import sqlite3


def create_database():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, course_name TEXT, duration TEXT, charges TEXT, description TEXT)")
    con.commit()


create_database()
