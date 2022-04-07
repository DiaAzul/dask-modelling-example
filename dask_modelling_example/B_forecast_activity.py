"""Forecasts baseline activity using historic activity and demographic growth for
acute hospitals and community services.
"""

from dask import delayed
from dask.delayed import Delayed

from .A_data_import import acute_data, community_data, population_data
from .Bb_forecast_base import forecast_base


class acute_forecast(forecast_base):
    """Calculates the forecast activity at acute hospitals given historic activity and
    demographic population growth."""

    @property
    def data(self) -> Delayed:
        """Acute Hospital forecast."""
        return delayed(self._forecast_calculation)(
            historic_activity=acute_data().data,
            population_growth=population_data().data,
            # Prefix dask key name with fa_ to avoid clashing with name of this class
            dask_key_name="fa_acute_forecast",
        )


class community_forecast(forecast_base):
    """Calculates the forecast activity in community services given historic activity and
    demographic population growth."""

    @property
    def data(self) -> Delayed:
        """Community services forecast."""
        return delayed(self._forecast_calculation)(
            historic_activity=community_data().data,
            population_growth=population_data().data,
            # Prefix dask key name with fa_ to avoid clashing with name of this class
            dask_key_name="fa_community_forecast",
        )
