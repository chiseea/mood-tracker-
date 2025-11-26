import sqlite3
from rich.console import Console

console = Console()

class Database:
    def __init__(self, db_name="mood_tracker.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS mood_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT,
                tanggal TEXT,
                mood_level INTEGER,
                aktivitas TEXT,
                catatan TEXT,
                event_spesial TEXT
            )
        """)
        self.conn.commit()

    def execute(self, sql, params=()):
        cur = self.conn.execute(sql, params)
        self.conn.commit()
        return cur

    def fetchall(self, sql, params=()):
        cur = self.conn.execute(sql, params)
        return cur.fetchall()

    def close(self):
        self.conn.close()
        console.print("[dim]Database connection closed.[/dim]")
