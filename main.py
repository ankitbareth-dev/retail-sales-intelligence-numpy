def main():

    while True:
        print("\n========== RETAIL SALES INTELLIGENCE SYSTEM ==========")
        print("1. Generate new sales dataset")
        print("2. Load saved dataset")
        print("3. Display sales data")
        print("4. Analyze units sold")
        print("5. Analyze revenue")
        print("6. Compare stores and products")
        print("7. Update sales data")
        print("8. Handle missing values")
        print("9. Save dataset")
        print("10. Export reports to CSV")
        print("11. Compare Python and NumPy performance")
        print("12. Exit")

        try:
            choice = int(input("\nEnter your choice (1-12): ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                print("Generate new sales dataset selected")
            case 2:
                print("Load saved dataset selected")
            case 3:
                print("Display sales data selected")
            case 4:
                print("Analyze units sold selected")
            case 5:
                print("Analyze revenue selected")
            case 6:
                print("Compare stores and products selected")
            case 7:
                print("Update sales data selected")
            case 8:
                print("Handle missing values selected")
            case 9:
                print("Save dataset selected")
            case 10:
                print("Export reports to CSV selected")
            case 11:
                print("Compare Python and NumPy performance selected")
            case 12:
                print("Exiting Retail Sales Intelligence System.")
                break
            case _:
                print("Invalid option.")
main()