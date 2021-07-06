from Ab_data_loader import loader

"""
Import the following files from the import folder.

+ Assumptions
+ Population forecast
+ Acute Hospital activity
+ Community activity
"""


class assumptions_data(loader):
    """Assumptions driving the model.

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    def __init__(self):
        """Assumptions."""
        self.data = self.delayed_load_data(
            file_name="assumptions.csv",
            dask_key_name="Assumptions",
        )


class population_data(loader):
    """Forecast for the annual rate of population growth by five year age band.
    Population forecasts are mid-year estimates by sex and 5-year age band (up to 85+).

    Inherits from base class loader

    Attributes:
        data (pd.DataFrame): Forecast of population by locality, age and service line.
    """

    def __init__(self):
        """Population growth."""
        self.data = self.delayed_load_data_na0(
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

    def __init__(self):
        """Acute hospital activity."""
        self.data = self.delayed_load_data_na0(
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

    def __init__(self):
        """Community activity."""
        self.data = self.delayed_load_data_na0(
            file_name="community_activity.csv",
            dask_key_name="Community_data",
        )
