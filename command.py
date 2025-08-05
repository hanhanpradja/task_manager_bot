import sqlite3

class Command:
    def __init__(self, name):
        self.DB_NAME = name

    def add(self, description):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tugas (description, status) VALUES (?, 0)", (description,))
        conn.commit()
        conn.close()
        return f"Tugas berhasil ditambahkan."

    def get_all(self):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tugas")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete(self, task_id):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tugas WHERE id = ?", (task_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return "Tugas dihapus." if affected else "Tugas tidak ditemukan."

    def mark(self, task_id, status):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE tugas SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return "Status tugas diperbarui." if affected else "Tugas tidak ditemukan."
