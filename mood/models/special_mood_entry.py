from .mood_entry import MoodEntry

class SpecialMoodEntry(MoodEntry):
    def __init__(self, tanggal, mood_level, aktivitas, catatan, event_spesial):
        super().__init__(tanggal, mood_level, aktivitas, catatan, event_spesial)
