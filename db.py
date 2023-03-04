import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
             user_id INTEGER PRIMARY KEY AUTOINCREMENT,
             login INTEGER NOT NULL,
             password TEXT NOT NULL
             first_name TEXT NOT NULL,
             last_name TEXT NOT NULL,
             middle_name TEXT NOT NULL,
             Email TEXT NOT NULL,
             age INTEGER NOT NULL,
             gender TEXT NOT NULL
             )""")
db.commit()

# sql.execute("SELECT login FROM users")
# if sql.fetchone() is None:
#     sql.execute(f"INSERT INTO users VALUES ('?)", phone_entry)
#     print('Зарегистрировано!')
# else:
#     print('Запись есть')
#     command = warrning1
#     db.commit()
# db.execute("""INSERT INTO users VALUES (?,?)""", (login, password))
# db.commit()
