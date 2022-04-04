from C_business_transform import business_transform

# Executes the model and outputs the results to a csv file.


def main() -> None:
    bt = business_transform().data.compute()
    bt.to_csv("results.csv")


if __name__ == "__main__":
    # execute only if run as a script
    main()
