from src.services.route_recomender import RouteRecomender
from src.ui.ui import UI

def main():

    user_preferences = UI.get_user_preferences()
    recommended_routes = RouteRecomender.get_by_preferences(user_preferences)
    
    UI.show_recommended_routes(recommended_routes)

if __name__ == "__main__":

    main()


