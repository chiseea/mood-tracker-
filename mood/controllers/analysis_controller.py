class AnalysisController:
    def __init__(self, analysis_service, analysis_view, mood_service):
        self.analysis_service = analysis_service
        self.analysis_view = analysis_view
        self.mood_service = mood_service

    def analyze(self, user):
        rows = self.mood_service.list_moods(user)
        avg = self.analysis_service.average_mood(rows)
        self.analysis_view.show_analysis(rows, avg if avg is not None else 0)
