from rich.prompt import Prompt, IntPrompt
from mood.models.mood_entry import MoodEntry as ModelMoodEntry
from mood.models.mood_entry import MoodEntry
from mood.models.special_mood_entry import SpecialMoodEntry

class MoodController:
    def __init__(self, mood_service, mood_view):
        self.service = mood_service
        self.view = mood_view

    def add_mood_interactive(self, user):
        tanggal = Prompt.ask("Masukkan tanggal (YYYY-MM-DD)")
        mood_level = IntPrompt.ask("Nilai mood (1–10)")
        aktivitas = Prompt.ask("Aktivitas")
        catatan = Prompt.ask("Catatan")
        event = Prompt.ask("Event Spesial (optional)", default="-")

        if event and event != "-":
            entry = SpecialMoodEntry(tanggal, mood_level, aktivitas, catatan, event)
        else:
            entry = MoodEntry(tanggal, mood_level, aktivitas, catatan)

        self.service.add_mood(user, entry)
        self.view.show_added(tanggal)

    def list_moods(self, user):
        rows = self.service.list_moods(user)
        self.view.show_list(rows, user)

    def delete_mood(self, user):
        rows = self.service.list_moods(user)
        self.view.show_list(rows, user)
        mood_id = Prompt.ask("\nMasukkan ID yang ingin dihapus", default="")
        if mood_id and mood_id.isdigit():
            self.service.delete_mood(int(mood_id))
            self.view.show_deleted(mood_id)
        else:
            from rich.console import Console
            Console().print("[yellow]ID tidak valid atau dibatalkan.[/yellow]")
