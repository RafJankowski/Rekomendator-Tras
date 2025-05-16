from src.models.user_preferences import UserPreferences
from src.data_managers.routes_data_manager import RoutesDataManager
from src.data_managers.weather_data_manager import WeatherDataManager
from datetime import datetime

class RouteRecomender:

    def get_by_preferences(user_preferences: UserPreferences):

        data = []
        routes = RoutesDataManager.get_all(max_difficulty=user_preferences.max_difficulty)
        for route in routes.values():

            length = route.get_route_length()
            if length > user_preferences.max_route_length:

                continue

            time_to_complete = route.get_time_to_complete()
            route_mid_point = route.calculate_mid_point()
            weather_data = WeatherDataManager.get_weather_data(
                position=route_mid_point,
                date_from=user_preferences.date_from,
                date_to=user_preferences.date_to
            )
            temperature_score = max(0, 100 - abs(weather_data.temperature_avg - user_preferences.temperature) * 100 / user_preferences.max_temperature_difference) # jeżeli przekroczy maksymalną różnice temperatur to score wydchodzi 0
            # jeżeli opady są mniejsze niż dopuszczalne to 100 a gdzy większe odpowiednio mniejszy wynik, do 0 przy 100%
            if weather_data.precipitation_propability < user_preferences.max_precipitation_propability:

                rain_score = 100

            else:

                proportion = 100 / (100 - user_preferences.max_precipitation_propability) # dzieli 100 przez każdy punkt ponad preferencję, w ten sposób uzyskuję prawidłową wage gdy użytkownik zgodzi się na większe opady
                rain_score = max(0, 100 - (weather_data.precipitation_propability - user_preferences.max_precipitation_propability) * proportion)

            if weather_data.wind_speed_avg < user_preferences.max_wind_speed:

                wind_score = 100

            else:

                proportion = 100 / (100 - user_preferences.max_wind_speed)
                wind_score = max(0, 100 - (weather_data.wind_speed_avg - user_preferences.max_wind_speed) * proportion)

            comfort_index = (temperature_score * 0.5) + (rain_score * 0.3) + (wind_score * 0.2)
            route_data = {
                "route": route,
                "weather_data": weather_data,
                "route_length": length, 
                "time_to_complete": time_to_complete,
                "comfort_index": comfort_index,
            }
            data.append(route_data)

        data.sort(key=lambda x: x["comfort_index"], reverse=True)
        return data
