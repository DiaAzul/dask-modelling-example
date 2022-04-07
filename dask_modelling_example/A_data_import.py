"""
Import the following files from the import folder.

+ Assumptions
+ Population forecast
+ Acute Hospital activity
+ Community activity
"""
from dask import delayed
from dask.delayed import Delayed

from dask_modelling_example.Ab_data_loader import loader


class assumptions_data(loader):
    """Assumptions driving the model.

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    @property
    def data(self) -> Delayed:
        """Assumptions."""
        return delayed(self.delayed_load_data)(
            file_name="assumptions.csv", dask_key_name="Assumptions"
        )


class population_data(loader):
    """Forecast for the annual rate of population growth by five year age band.

    Population forecasts are mid-year estimates by 5-year age band (up to 85+).

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    @property
    def data(self) -> Delayed:
        """Population growth."""
        return delayed(self.delayed_load_data_na0)(
            file_name="population_growth.csv",
            dask_key_name="Population_growth_data",
        )


class acute_data(loader):
    """Acute hospital activity within the base year of the forecast. Includes the following
    dimensions:

    + Year
    + Hospital name
    + Service line
    + Age band
    + Sex
    + Activity

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    @property
    def data(self) -> Delayed:
        """Acute hospital activity."""
        return delayed(self.delayed_load_data_na0)(
            file_name="acute_hospital_activity.csv",
            dask_key_name="Acute_hospital_data",
        )


class community_data(loader):
    """Community activity within the base year of the forecast. Includes the following
    dimensions:

    + Year
    + Community provider name
    + Service line
    + Age band
    + Sex
    + Activity

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    @property
    def data(self) -> Delayed:
        """Community activity."""
        return delayed(self.delayed_load_data_na0)(
            file_name="community_activity.csv",
            dask_key_name="Community_data",
        )
