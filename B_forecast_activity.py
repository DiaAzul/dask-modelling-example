from Bb_forecast_base import forecast_base
from A_data_import import acute_data, community_data, population_data


class acute_forecast(forecast_base):
    def __init__(self) -> None:
        self.data = self._forecast_calculation(
            historic_activity=acute_data().data,
            population_growth=population_data().data,
        )


class community_forecast(forecast_base):
    def __init__(self) -> None:
        self.data = self._forecast_calculation(
            historic_activity=community_data().data,
            population_growth=population_data().data,
        )
