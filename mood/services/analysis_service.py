class AnalysisService:
    def average_mood(self, rows):
        if not rows:
            return None
        total = sum(row[2] for row in rows)
        avg = total / len(rows)
        return avg
