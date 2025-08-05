import sqlite3

def create_database(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tugas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description VARCHAR(255) NOT NULL,
            status BINARY NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_table_info(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute('PRAGMA table_info(tugas)')
    columns = cursor.fetchall()
    conn.close()
    return columns

if __name__ == "__main__":
    DB_NAME = "tugas.db"
    create_database(DB_NAME)
    print("Database and table created.")
    print("Table info:", get_table_info(DB_NAME))