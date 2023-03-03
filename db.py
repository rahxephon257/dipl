import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
             user_id INTEGER PRIMARY KEY AUTOINCREMENT,
             login INTEGER NOT NULL,
             password TEXT NOT NULL,
             Имя TEXT NOT NULL,
             Фамилия TEXT NOT NULL,
             Отчество TEXT NOT NULL,
             Email TEXT NOT NULL,
             Возвраст INTEGER NOT NULL,
             пол TEXT NOT NULL
             )""")

db.commit()
sql.close()
db.close()

