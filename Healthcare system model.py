from C_business_transform import business_transform


def main() -> None:
    bt = business_transform().data.compute()
    result = bt.head().round(0)

if __name__ == "__main__":
    # execute only if run as a script
    main()