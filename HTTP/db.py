from sqlite3 import connect

con = connect("app.db")
cur = con.cursor()
cur.execute("CREATE table if not exists person(birth_year INT, name CHAR(50)), family")

cur.execute("CREATE table if not exists family(name CHAR(50))")