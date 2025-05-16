from datetime import datetime

class UserPreferences:
    
    def __init__(self, 
                 temperature: float = 0.0,
                 max_temperature_difference: float = 0.0,
                 max_precipitation_propability: float = 0.0,
                 max_wind_speed: float = 0.0,
                 max_difficulty: int = 0,
                 max_route_length: float = 0.0,
                 date_from: datetime = None,
                 date_to: datetime = None):
        self._temperature = temperature
        self._max_temperature_difference = max_temperature_difference
        self._max_precipitation_propability = max_precipitation_propability
        self._max_wind_speed = max_wind_speed
        self._max_difficulty = max_difficulty
        self._max_route_length = max_route_length
        self._date_from = date_from
        self._date_to = date_to

    @property
    def date_from(self):
        return self._date_from

    @date_from.setter
    def date_from(self, value: datetime):
        self._date_from = value

    @property
    def date_to(self):
        return self._date_to

    @date_to.setter
    def date_to(self, value: datetime):
        self._date_to = value

    @property
    def temperature(self):

        return self._temperature

    @temperature.setter
    def temperature(self, value: float):

        self._temperature = value

    @property
    def max_precipitation_propability(self):

        return self._max_precipitation_propability

    @max_precipitation_propability.setter
    def max_precipitation_propability(self, value: float):

        if value < 0.0 or value > 100.0:

            raise ValueError("Maksymalna prawdopodobieństwo opadów musi być w przedziale 0-100%")
        
        self._max_precipitation_propability = value

    @property
    def max_difficulty(self):

        return self._max_difficulty

    @max_difficulty.setter
    def max_difficulty(self, value: int):

        if value < 1 or value > 5:

            raise ValueError("Maksymalna trudność musi być w przedziale 1-5")
        
        self._max_difficulty = value

    @property
    def max_route_length(self):

        return self._max_route_length

    @max_route_length.setter
    def max_route_length(self, value: float):
        
        self._max_route_length = value

    @property
    def max_temperature_difference(self):
        return self._max_temperature_difference

    @max_temperature_difference.setter
    def max_temperature_difference(self, value: float):

        if value < 0.0:

            raise ValueError("Maksymalna różnica temperatur musi być nieujemna")
        
        self._max_temperature_difference = value