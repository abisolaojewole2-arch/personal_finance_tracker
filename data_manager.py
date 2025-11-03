
import pandas as pd

class DataManager:
    def __init__(self, data):
        self.data = data

    def view_by_date_range(self):
        start = input("Enter start date (YYYY-MM-DD): ")
        end = input("Enter end date (YYYY-MM-DD): ")
        mask = (self.data['date'] >= start) & (self.data['date'] <= end)
        print(self.data.loc[mask])

    def add_transaction(self):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = input("Enter amount: ")
        new_txn = {
            'date': pd.to_datetime(date),
            'category': category,
            'description': description,
            'amount': float(amount)
        }
        self.data = self.data.append(new_txn, ignore_index=True)
        print("Transaction added.")

    def edit_transaction(self):
        idx = int(input("Enter index to edit: "))
        if 0 <= idx < len(self.data):
            for col in ['date', 'category', 'description', 'amount']:
                val = input(f"New {col} (leave blank to keep '{self.data.at[idx, col]}'): ")
                if val:
                    self.data.at[idx, col] = pd.to_datetime(val) if col == 'date' else float(val) if col == 'amount' else val
            print("Transaction updated.")
        else:
            print("Invalid index.")

    def delete_transaction(self):
        idx = int(input("Enter index to delete: "))
        if 0 <= idx < len(self.data):
            self.data = self.data.drop(idx).reset_index(drop=True)
            print("Transaction deleted.")
        else:
            print("Invalid index.")

    def save_to_csv(self):
        filename = input("Enter filename to save as (e.g., updated_data.csv): ")
        self.data.to_csv(filename, index=False)
        print(f"Data saved to {filename}.")
