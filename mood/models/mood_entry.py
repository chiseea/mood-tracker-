class MoodEntry:
    def __init__(self, tanggal, mood_level, aktivitas, catatan, event_spesial="-"):
        self.tanggal = tanggal
        self.mood_level = int(mood_level)
        self.aktivitas = aktivitas
        self.catatan = catatan
        self.event_spesial = event_spesial
