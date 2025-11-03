
from preprocess import Preprocess
from data_manager import DataManager
from analysis import Analysis
from plot_my_data import PlotMyData

print("Welcome to the Personal Finance Tracker App!")

# Step 1: Import CSV
pre = Preprocess()
data = pre.import_my_data()

if data is not None:
    manager = DataManager(data)
    analysis = Analysis(manager.data)
    plotter = PlotMyData(manager.data)

    while True:
        print("\nSelect an option:")
        print("1. View transactions by date range")
        print("2. Add a transaction")
        print("3. Edit a transaction")
        print("4. Delete a transaction")
        print("5. Spending by category")
        print("6. Average monthly spending")
        print("7. Top spending category")
        print("8. Line chart: Monthly spending trend")
        print("9. Bar chart: Spending by category")
        print("10. Pie chart: Spending distribution")
        print("11. Save to CSV")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            manager.view_by_date_range()
        elif choice == '2':
            manager.add_transaction()
        elif choice == '3':
            manager.edit_transaction()
        elif choice == '4':
            manager.delete_transaction()
        elif choice == '5':
            analysis.spending_by_category()
        elif choice == '6':
            analysis.average_monthly_spending()
        elif choice == '7':
            analysis.top_spending_category()
        elif choice == '8':
            plotter.plot_monthly_trend()
        elif choice == '9':
            plotter.plot_by_category()
        elif choice == '10':
            plotter.plot_pie_distribution()
        elif choice == '11':
            manager.save_to_csv()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
else:
    print("Failed to load data.")
