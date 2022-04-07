import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = ROOT_DIR + "/Import_data/"


class loader:
    """Load data from CSV files using a Dask delayed function."""

    def delayed_load_data(self, file_name: str) -> pd.DataFrame:
        """Delayed function to load a CSV file into a Pandas DataFrame from the defined data directory.

        Args:
            file_name (str): File name (including extension)

        Returns:
            pd.DataFrame: Data loaded from file
        """
        return pd.read_csv(DATA_DIR + file_name)

    def delayed_load_data_na0(self, file_name: str) -> pd.DataFrame:
        """Delayed function to load a CSV file into a Pandas DataFrame from the defined data directory
        replacing missing data with zero.

        Args:
            file_name (str): File name (including extension)

        Returns:
            pd.DataFrame: Data loaded from file with missing data replaced by zero.
        """
        return pd.read_csv(DATA_DIR + file_name).fillna(0)

    def delayed_load_data_na_blank(self, file_name: str) -> pd.DataFrame:
        """Delayed function to load a CSV file into a Pandas DataFrame from the defined data directory
        replacing missing data with an empty string.

        Args:
            file_name (str): File name (including extension)

        Returns:
            pd.DataFrame: Data loaded from file with missing data replaced by an empty string.
        """
        return pd.read_csv(DATA_DIR + file_name).fillna("")
