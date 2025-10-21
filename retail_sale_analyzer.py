
import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Ensures charts display on Windows
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tkinter')


class RetailSaleAnalyzer:
    def __init__(self, file_path='retail_sales.csv'):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        self.data = pd.read_csv(file_path)
        # Ensure correct data types
        if 'Date' not in self.data.columns or 'Sales' not in self.data.columns:
            raise ValueError("❌ CSV must contain at least 'Date' and 'Sales' columns.")
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        self.data['Sales'] = pd.to_numeric(self.data['Sales'], errors='coerce')

    def data_clean(self):
        before = len(self.data)
        self.data.dropna(subset=['Date', 'Sales', 'Product'], inplace=True)
        after = len(self.data)
        print(f"✅ Cleaned data: Removed {before - after} rows with missing values.")

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()

    def best_selling_product(self):
        return self.total_sales_per_product().sort_values(ascending=False).index[0]

    def average_daily_sales(self):
        return round(self.data['Sales'].mean(), 2)

    def plot_sales_trend(self):
        daily_sales = self.data.groupby('Date')['Sales'].sum().sort_index()
        plt.figure(figsize=(10,5))
        plt.plot(daily_sales.index, daily_sales.values, marker='o', color='teal', linewidth=2)
        plt.title('Sales Trend Over Time', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Total Sales', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_sales_per_product(self):
        sales_per_product = self.total_sales_per_product()
        plt.figure(figsize=(8,5))
        sales_per_product.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Sales Per Product', fontsize=14)
        plt.xlabel('Product', fontsize=12)
        plt.ylabel('Total Sales', fontsize=12)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

    def export_sales_report(self, output_file='sales_report.xlsx'):
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

        # Summary sheet
        summary_df = pd.DataFrame({
            "Metric": ["Best Selling Product", "Average Daily Sales"],
            "Value": [self.best_selling_product(), self.average_daily_sales()]
        })
        summary_df.to_excel(writer, sheet_name='Summary', index=False)

        # Sales per product sheet
        total_sales_df = self.total_sales_per_product().reset_index()
        total_sales_df.columns = ['Product', 'Total Sales']
        total_sales_df.to_excel(writer, sheet_name='Sales Per Product', index=False)

        # Daily sales trend sheet
        daily_sales_df = self.data.groupby('Date')['Sales'].sum().reset_index()
        daily_sales_df.to_excel(writer, sheet_name='Daily Sales Trend', index=False)

        writer.close()
        print(f"📁 Excel report generated successfully: {output_file}")


if __name__ == "__main__":
    print("🚀 Retail Sale Analyzer Starting...\n")

    analyzer = RetailSaleAnalyzer('retail_sales.csv')
    analyzer.data_clean()

    print("📊 Total Sales per Product:\n", analyzer.total_sales_per_product())
    print("\n🏆 Best Selling Product:", analyzer.best_selling_product())
    print("\n💵 Average Daily Sales:", analyzer.average_daily_sales())

    analyzer.plot_sales_per_product()
    analyzer.plot_sales_trend()

    analyzer.export_sales_report()

    print("\n✅ Analysis and report generation complete!")
