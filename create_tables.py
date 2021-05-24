import sqlite3

con = sqlite3.connect("./phones.db")
cur = con.cursor()
sql = f"""CREATE TABLE IF NOT EXISTS phones
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
value INTEGER);
"""
cur.execute(sql)
con.close()