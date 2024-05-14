import _sqlite3
conn=_sqlite3.connect('formulaire_dinscription.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER PRIMARY KEY,
    Nom TEXT NOT NULL,
    Prenom TEXT NOT NULL,
    Email TEXT NOT NULL,
    DateNaissance DATE,
    Telephone INTEGER)''')

cursor.execute("INSERT INTO Users(Nom, Prenom, Email, DateNaissance, Telephone) VALUES(?,?,?,?,?)",('Cheoua','André','cheouabosco@gmail.com','2000-10-17','659307850'))
conn.commit()
conn.close()