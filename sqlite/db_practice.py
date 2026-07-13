import sqlite3

conn = sqlite3.connect('practice.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
''')

cursor.execute("INSERT INTO users(name) VALUES('jiro');")

cursor.execute("INSERT INTO users(name) VALUES('taro');")


cursor.execute('SELECT * FROM users')

imp = cursor.fetchall()
for n in imp:
    print(f"ID: {n[0]} name: {n[1]}")

conn.commit()

conn.close()