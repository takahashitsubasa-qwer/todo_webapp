import sqlite3



def createdb():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_content TEXT NOT NULL,
        priority TEXT NOT NULL,
        done BOOLEAN NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def getdb():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM todos;')
    rows = cursor.fetchall()

    conn.close()

    return rows


def postdb(one_of_todo):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO todos(title_content,priority,done) VALUES(?,?,?)',one_of_todo)

    conn.commit()
    conn.close()
