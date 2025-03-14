from sqlite3 import connect

con = connect("app.db")
cur = con.cursor()
cur.execute("CREATE table if not exists person(birth_year INT, name CHAR(50)), family")
# Dans l'idée, la colonne family s'apellerait family_id et serait une clé étrangère vers la table family

cur.execute("CREATE table if not exists family(name CHAR(50))")
# Ces tables ne sont utilisées nulle part ?