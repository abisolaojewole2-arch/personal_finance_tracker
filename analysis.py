
class Analysis:
    def __init__(self, data):
        self.data = data

    def spending_by_category(self):
        print(self.data.groupby('category')['amount'].sum())

    def average_monthly_spending(self):
        self.data['month'] = self.data['date'].dt.to_period('M')
        print(self.data.groupby('month')['amount'].sum().mean())

    def top_spending_category(self):
        total = self.data.groupby('category')['amount'].sum()
        top = total.idxmax()
        print(f"Top spending category: {top} - Amount: {total[top]}")
