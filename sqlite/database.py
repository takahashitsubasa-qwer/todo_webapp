import sqlite3


def createdb():
    conn = sqlite3.connect('todossecond.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS todossecond (
        todo_id_db INTEGER PRIMARY KEY AUTOINCREMENT,
        title_content_db TEXT NOT NULL,
        priority_db TEXT NOT NULL,
        done_db BOOLEAN NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def getdb():
    conn = sqlite3.connect("todossecond.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM todossecond;')
    rows = cursor.fetchall()

    conn.close()
    
    return rows


def postdb(one_of_todo):
    conn = sqlite3.connect('todossecond.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO todossecond(title_content_db,priority_db,done_db) VALUES(?,?,?)',one_of_todo)

    conn.commit()
    conn.close()

def putdb(list_put):
    conn = sqlite3.connect("todossecond.db")
    cursor = conn.cursor()

    cursor.execute('''UPDATE todossecond SET
    title_content_db = ?,
    priority_db = ?
    WHERE todo_id_db = ?
    ''',
    list_put
    )

    conn.commit()
    conn.close()
