"""Runs the healthcare systems model and outputs the result to a csv file.

This file may be uploaded to an online dashboard for presentation of the results.
"""
from dask_modelling_example.C_business_transform import business_transform


def main() -> None:
    """Calculate the model and save the results to a CSV file."""
    model_results = business_transform().data.compute()
    model_results.to_csv("results.csv")


if __name__ == "__main__":
    # execute only if run as a script
    main()
