"""Library function to apply business transformation rules to baseline activity."""
import pandas as pd


class business_transform_base:
    """Library functions to apply business transformation rules to baseline activity."""
    def _business_transform(
        self,
        acute_forecast: pd.DataFrame,
        community_forecast: pd.DataFrame,
        assumptions_data: pd.DataFrame,
    ) -> pd.DataFrame:
        """Calculates revised activity forecasts for acute and community activity based upon
        forecast acute hospital and community service activity and assumptions for migration
        of activity by service line. The model assumes that changes come into effect for the
        year 2025.

        Args:
            acute_forecast (pd.DataFrame): Forecast acute hospital activity
            community_forecast (pd.DataFrame): Forecast community services activity
            assumptions_data (pd.DataFrame): Percentage shift of acute activity to community by service line.

        Returns:
            pd.DataFrame: Revised and original acute hospital and community service activity.
        """

        # Rename activity columns in acute and community tables to acute_activity and community_activity;
        # Drop the domain columns which contain community and activity identifiers;
        # Merge two tables into a single table with acute_activity and community_activity columns.

        af = acute_forecast.rename(columns={"activity": "acute_activity"}).drop(
            columns=["domain"]
        )
        cf = community_forecast.rename(columns={"activity": "community_activity"}).drop(
            columns=["domain"]
        )

        MERGE_COLUMNS = [
            "hospital_name",
            "region",
            "service_line",
            "sex",
            "age_band",
            "year",
        ]
        mergedf = af.merge(cf, how="outer", on=MERGE_COLUMNS)

        # Add assumptions for activity moved to community by service_line
        df = mergedf.merge(
            assumptions_data,
            how="left",
            on="service_line",
        )

        # Calculate new activity after redistributing activity between acute and community hospitals.
        # percentage_shift_to_community from year 2025 onwards.
        df["date"] = pd.to_datetime(
            df["year"].apply(lambda x: f"{x}-01-01"), infer_datetime_format=True
        )  # type:ignore
        df["include"] = (df["date"] >= "2025-01-01").astype("int")
        df["activity_shift_to_community"] = (
            df["acute_activity"] * df["percentage_shift_to_community"] * df["include"]
        )
        df["revised_acute_activity"] = (
            df["acute_activity"] - df["activity_shift_to_community"]
        )
        df["revised_community_activity"] = (
            df["community_activity"] + df["activity_shift_to_community"]
        )

        # Remove intermediate columns to tidy up returned table.
        df.drop(
            columns=["percentage_shift_to_community", "date", "include"],
            inplace=True,
            axis=1,
        )

        return df
