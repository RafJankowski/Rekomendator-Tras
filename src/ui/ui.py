from src.models.user_preferences import UserPreferences
from datetime import datetime

class UI:

    def get_user_preferences():

        user_preferences = UserPreferences()

        print("Uzupełnij preferencje:")
        temperature = float(input("Temperatura (°C): "))
        max_temperature_difference = float(input("Dopuszczalna różnica temperatury od preferowanej (°C): "))
        max_precipitation = float(input("Dopuszczalne szanse na opady (0-100%): "))
        max_wind_speed = float(input("Dopuszczalna prętkość wiatru (km/h): "))
        max_difficulty = int(input("Maksymalna trudność trasy (1-5): "))
        max_route_length = float(input("Maksymalna długość trasy (km): "))
        date_from = input("Data od (YYYY-MM-DD) (zostaw pustą aby wziąć dzisiejszą datę): ")
        date_to = input("Data do (YYYY-MM-DD) (zostaw pustą aby wziąć dzisiejszą datę): ")
        if date_from == "":

            date_from = datetime.now().date()

        if date_to == "":
            
            date_to = datetime.now().date()

        user_preferences.temperature = temperature
        user_preferences.max_temperature_difference = max_temperature_difference
        user_preferences.max_precipitation_propability = max_precipitation
        user_preferences.max_wind_speed = max_wind_speed
        user_preferences.max_difficulty = max_difficulty
        user_preferences.max_route_length = max_route_length
        user_preferences.date_from = date_from
        user_preferences.date_to = date_to

        return user_preferences
    
    def show_recommended_routes(recommended_routes):

        print("Zalecane trasy na dni:")
        print("od:", recommended_routes[0]['weather_data'].date_from)
        print("do:", recommended_routes[0]['weather_data'].date_to)
        print("===================================")
        i = 1
        for route in recommended_routes:

            print(f"{i}. Trasa: {route['route'].name} ({route['route'].region})")
            print(f"        Długość: {round(route['route_length'], 2)} km")
            print(f"        Trudność: {route['route'].difficulty}/5")
            print(f"        Szacowany czas: {round(route['time_to_complete'], 2)} h")
            print(f"        Komfort pogodowy: {round(route['comfort_index'])}/100")
            print(f"        Kategoria: {", ".join(route['route'].tags)}")
            print()
            i += 1
