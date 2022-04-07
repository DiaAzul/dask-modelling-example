"""Test that loader correctly imports data into the model.

Schema validation is performed using pandera.
"""
import pandas as pd
import pandera as pa

import pytest
import unittest

from dask_modelling_example.Ab_data_loader import loader


class model_dimensions:
    """Permissible categories in model dimensions."""

    age_bands = [
        "A.000-004",
        "B.005-009",
        "C.010-014",
        "D.015-019",
        "E.020-024",
        "F.025-029",
        "G.030-034",
        "H.035-039",
        "I.040-044",
        "J.045-049",
        "K.050-054",
        "L.055-059",
        "M.060-064",
        "N.065-069",
        "O.070-074",
        "P.075-079",
        "Q.080-084",
        "R.085+",
    ]
    domains = ["community"]
    hospitals = ["Hospital one", "Hospital two", "Hospital three"]
    regions = ["East", "North", "South", "West"]
    service_lines = [
        "Cardiology",
        "Dermatology",
        "Diabetes",
        "Respiratory",
        "Rheumatology",
        "Urology",
    ]
    sexes = ["Female", "Male"]


class test_assumptions_loader(unittest.TestCase, model_dimensions):
    """Test the assumptions data matches the defined schema for the model."""

    schema = pa.DataFrameSchema(
        {
            "service_line": pa.Column(str),
            "percentage_shift_to_community": pa.Column(
                float,
                pa.Check(lambda percentage: (percentage >= 0) & (percentage <= 1)),
            ),
        }
    )

    def test_schema(self):
        """Test that loaded data is a DataFrame and matches schema."""
        test_file = "assumptions.csv"
        loaded_data = loader().delayed_load_data(file_name=test_file)
        self.assertIsInstance(loaded_data, pd.DataFrame)
        try:
            self.schema.validate(loaded_data)
        except pa.errors.SchemaError as error:
            pytest.fail(str(error))


class test_population_growth_loader(unittest.TestCase):
    """Test the population growth data matches the defined schema for the model."""

    schema = pa.DataFrameSchema(
        {
            "age_band": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.age_bands)
            ),
        }
    )

    def test_schema(self):
        """Test that loaded data is a DataFrame and matches schema."""
        test_file = "population_growth.csv"
        loaded_data = loader().delayed_load_data_na0(file_name=test_file)
        self.assertIsInstance(loaded_data, pd.DataFrame)
        try:
            self.schema.validate(loaded_data)
        except pa.errors.SchemaError as error:
            pytest.fail(str(error))


class test_community_activity_loader(unittest.TestCase):
    """Test the community activity data matches the defined schema for the model."""

    schema = pa.DataFrameSchema(
        {
            "domain": pa.Column(str, checks=pa.Check.isin(["community"])),
            "year": pa.Column(int),
            "hospital_name": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.hospitals)
            ),
            "region": pa.Column(str, checks=pa.Check.isin(model_dimensions.regions)),
            "service_line": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.service_lines)
            ),
            "sex": pa.Column(str, checks=pa.Check.isin(model_dimensions.sexes)),
            "age_band": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.age_bands)
            ),
            "activity": pa.Column(int),
        }
    )

    def test_schema(self):
        """Test that loaded data is a DataFrame and matches schema."""
        test_file = "community_activity.csv"
        loaded_data = loader().delayed_load_data_na0(file_name=test_file)
        self.assertIsInstance(loaded_data, pd.DataFrame)
        try:
            self.schema.validate(loaded_data)
        except pa.errors.SchemaError as error:
            pytest.fail(str(error))


class test_hospital_activity_loader(unittest.TestCase):
    """Test the acute hospital activity data matches the defined schema for the model."""

    schema = pa.DataFrameSchema(
        {
            "domain": pa.Column(str, checks=pa.Check.isin(["acute"])),
            "year": pa.Column(int),
            "hospital_name": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.hospitals)
            ),
            "region": pa.Column(str, checks=pa.Check.isin(model_dimensions.regions)),
            "service_line": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.service_lines)
            ),
            "sex": pa.Column(str, checks=pa.Check.isin(model_dimensions.sexes)),
            "age_band": pa.Column(
                str, checks=pa.Check.isin(model_dimensions.age_bands)
            ),
            "activity": pa.Column(int),
        }
    )

    def test_schema(self):
        """Test that loaded data is a DataFrame and matches schema."""
        test_file = "acute_hospital_activity.csv"
        loaded_data = loader().delayed_load_data_na0(file_name=test_file)
        self.assertIsInstance(loaded_data, pd.DataFrame)
        try:
            self.schema.validate(loaded_data)
        except pa.errors.SchemaError as error:
            pytest.fail(str(error))
