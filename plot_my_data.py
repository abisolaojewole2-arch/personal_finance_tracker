
import matplotlib.pyplot as plt

class PlotMyData:
    def __init__(self, data):
        self.data = data

    def plot_monthly_trend(self):
        self.data['month'] = self.data['date'].dt.to_period('M')
        monthly = self.data.groupby('month')['amount'].sum()
        monthly.plot(kind='line', title='Monthly Spending Trend')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.show()

    def plot_by_category(self):
        category_totals = self.data.groupby('category')['amount'].sum()
        category_totals.plot(kind='bar', title='Spending by Category')
        plt.ylabel('Amount')
        plt.show()

    def plot_pie_distribution(self):
        category_totals = self.data.groupby('category')['amount'].sum()
        category_totals.plot(kind='pie', autopct='%1.1f%%', title='Spending Distribution')
        plt.ylabel('')
        plt.show()
