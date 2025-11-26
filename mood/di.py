from mood.database import Database
from mood.services.mood_service import MoodService
from mood.services.analysis_service import AnalysisService
from mood.views.menu_view import MenuView
from mood.views.mood_view import MoodView
from mood.views.analysis_view import AnalysisView
from mood.controllers.menu_controller import MenuController
from mood.controllers.mood_controller import MoodController
from mood.controllers.analysis_controller import AnalysisController

def create_container():
    db = Database()  # single DB instance
    mood_service = MoodService(db)
    analysis_service = AnalysisService()

    # views
    menu_view = MenuView()
    mood_view = MoodView()
    analysis_view = AnalysisView()

    # controllers
    mood_ctrl = MoodController(mood_service, mood_view)
    analysis_ctrl = AnalysisController(analysis_service, analysis_view, mood_service)
    menu_ctrl = MenuController(menu_view, mood_ctrl, analysis_ctrl)

    return {
        "db": db,
        "mood_service": mood_service,
        "analysis_service": analysis_service,
        "menu_view": menu_view,
        "mood_view": mood_view,
        "analysis_view": analysis_view,
        "mood_controller": mood_ctrl,
        "analysis_controller": analysis_ctrl,
        "menu_controller": menu_ctrl
    }
