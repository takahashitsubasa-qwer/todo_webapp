import sqlite3


def createdb():
    conn = sqlite3.connect('last.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS last (
        todo_id_db INTEGER PRIMARY KEY AUTOINCREMENT,
        title_content_db TEXT NOT NULL,
        priority_db TEXT NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def createdb_completion():
    conn = sqlite3.connect('last_completion.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS last_completion (
        todo_id_db INTEGER PRIMARY KEY AUTOINCREMENT,
        title_content_db TEXT NOT NULL,
        priority_db TEXT NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def getdb():
    conn = sqlite3.connect("last.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM last;')
    rows = cursor.fetchall()

    conn.close()
    
    return rows


def postdb(one_of_todo):
    conn = sqlite3.connect('last.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO last(title_content_db,priority_db) VALUES(?,?)',one_of_todo)

    conn.commit()
    conn.close()

def putdb(list_put):
    conn = sqlite3.connect("last.db")
    cursor = conn.cursor()

    cursor.execute('''UPDATE last SET
    title_content_db = ?,
    priority_db = ?
    WHERE todo_id_db = ?
    ''',
    list_put
    )

    conn.commit()
    conn.close()

def deletedb(todo_delete_id):
    conn = sqlite3.connect("last.db")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM last WHERE todo_id_db = ?',todo_delete_id)

    conn.commit()
    conn.close()

def patchdb(todo_patch_id,dict_patch):
    conn = sqlite3.connect("last.db")
    cursor = conn.cursor()

    for tmp in dict_patch:
        if tmp["todo_id"] == todo_patch_id:
                cursor.execute('''INSERT INTO last_completion(title_content_db,priority_db) VALUES(?,?)''',(tmp["title_content"],tmp["priority"]))
                cursor.execute('DELETE FROM last WHERE todo_id_db = ?', (todo_patch_id,))

    conn.commit()
    conn.close()