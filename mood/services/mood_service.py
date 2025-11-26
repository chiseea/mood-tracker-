from rich.console import Console

console = Console()

class MoodService:
    def __init__(self, db):
        self.db = db

    def add_mood(self, user, entry):
        sql = """
            INSERT INTO mood_entries (user, tanggal, mood_level, aktivitas, catatan, event_spesial)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute(sql, (user, entry.tanggal, entry.mood_level, entry.aktivitas, entry.catatan, entry.event_spesial))
        console.print("[green]Data mood berhasil ditambahkan ke database.[/green]")

    def list_moods(self, user):
        sql = "SELECT id, tanggal, mood_level, aktivitas, catatan, event_spesial FROM mood_entries WHERE user = ? ORDER BY tanggal DESC"
        return self.db.fetchall(sql, (user,))

    def delete_mood(self, mood_id):
        sql = "DELETE FROM mood_entries WHERE id = ?"
        self.db.execute(sql, (mood_id,))
        console.print(f"[red]Data dengan ID {mood_id} dihapus.[/red]")
