"""Library function to forecast activity given historic activity and demographic growth.

The base year for historic activity is fixed to the year 2020.
"""
import pandas as pd


class forecast_base:
    """Library of functions for forecasting activity based upon demographic growth."""
    def _forecast_calculation(
        self, historic_activity: pd.DataFrame, population_growth: pd.DataFrame
    ) -> pd.DataFrame:
        """Projects historics activity forward according to growth in population by five-year age group.

        + Column containing age band description is age_band in both tables.
        + Historic activity is for year 2020.
        + Historic activity is in 'activity'
        + Forecast years are sequential columns from year after historic activity year (2021, 2022, ...).

        Args:
            historic_activity (pd.DataFrame): Historics activity by five-year age group.
            population_growth (pd.DataFrame): Annual change in population by five year age group.

        Returns:
            pd.DataFrame: Historic plus forecast activity by year and five-year age group.
        """

        BASE_ACTIVITY = "activity"
        BASE_YEAR = "2020"
        AGE_BAND_ACTIVITY = "age_band"
        AGE_BAND_GROWTH = "age_band"

        # Join annual growth rates to historic data on age bands.
        df = historic_activity.merge(
            population_growth,
            left_on=AGE_BAND_ACTIVITY,
            right_on=AGE_BAND_GROWTH,
            how="left",
        ).fillna(0)

        # Calculate the new activity by iterating over forecast years and increasing activity on prior year
        # by growth percentage.
        forecast_years = list(population_growth.columns[1:])
        prior_years = [BASE_ACTIVITY] + forecast_years
        for prior_year, year in zip(prior_years, forecast_years):
            df[year] = df.apply(lambda row: row[prior_year] * (1 + row[year]), axis=1)

        # Rename the historic activity column "activity" to the base year "2020";
        # Drop the existing year column;
        # Then unpivot activity data creating a new column for years and activity.
        df.rename(columns={BASE_ACTIVITY: BASE_YEAR}, inplace=True)
        df.drop(["year"], inplace=True, axis=1)
        id_vars = [
            "domain",
            "hospital_name",
            "region",
            "service_line",
            "sex",
            "age_band",
        ]
        df = df.melt(
            id_vars=id_vars, var_name="year", value_name="activity", ignore_index=True
        )

        return df
