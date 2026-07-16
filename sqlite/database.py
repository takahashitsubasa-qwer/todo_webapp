import sqlite3


def createdb():
    conn = sqlite3.connect('finally.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS finally (
        todo_id_db INTEGER PRIMARY KEY AUTOINCREMENT,
        title_content_db TEXT NOT NULL,
        priority_db TEXT NOT NULL,
        done_db INT NOT NULL DEFAULT 0
    );
    ''')

    conn.commit()
    conn.close()

def getdb():
    conn = sqlite3.connect("finally.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM finally;')
    rows = cursor.fetchall()

    conn.close()
    
    return rows


def postdb(one_of_todo):
    conn = sqlite3.connect('finally.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO finally(title_content_db,priority_db) VALUES(?,?)',one_of_todo)

    conn.commit()
    conn.close()

def putdb(list_put):
    conn = sqlite3.connect("finally.db")
    cursor = conn.cursor()

    cursor.execute('''UPDATE finally SET
    title_content_db = ?,
    priority_db = ?
    WHERE todo_id_db = ?
    ''',
    list_put
    )

    conn.commit()
    conn.close()

def deletedb(todo_delete_id):
    conn = sqlite3.connect("finally.db")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM finally WHERE todo_id_db = ?',todo_delete_id)

    conn.commit()
    conn.close()

def patchdb(todo_patch_id):
    conn = sqlite3.connect("finally.db")
    cursor = conn.cursor()

    cursor.execute('UPDATE finally SET done_db = 1 WHERE todo_id_db = ?',(todo_patch_id,))

    conn.commit()
    conn.close()