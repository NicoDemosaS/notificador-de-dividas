import sqlite3

try:
    conn = sqlite3.connect('clientes.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    numero INTEGER NOT NULL,
    divida INTEGER NOT NULL
                   )
''')

    conn.commit()
    conn.close()
    
    #print(cursor.fetchall())
    print('DEU CERTO')
    
except sqlite3.Error as erro:
    print(f'ERRO -> {erro}')