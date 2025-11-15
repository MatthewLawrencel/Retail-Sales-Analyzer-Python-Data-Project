import pandas as pd
import matplotlib.pyplot as plt
import os

class RetailSaleAnalyzer:
    def __init__(self, file_path='retail_sales.csv'):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        self.data = pd.read_csv(file_path)
        # Ensure correct data types
        if 'Date' not in self.data.columns or 'Sales' not in self.data.columns:
            raise ValueError("CSV must contain at least 'Date' and 'Sales' columns.")
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        self.data['Sales'] = pd.to_numeric(self.data['Sales'], errors='coerce')

    def data_clean(self):
        before = len(self.data)
        self.data.dropna(subset=['Date', 'Sales', 'Product'], inplace=True)
        after = len(self.data)
        print(f"Cleaned data: Removed {before - after} rows with missing values.")

    def total_sales_per_product(self):
        return self.data.groupby('Product')['Sales'].sum()
    
    def best_selling_product(self):
        total_sales = self.total_sales_per_product()
        self.best_selling_product = total_sales.sort_values(ascending=False).index[0]
        return self.best_selling_product

    def average_daily_sales(self):
        return self.data['Sales'].mean()
    
    def plot_sales_trend(self):
        daily_sales = self.data.groupby('Date')['Sales'].sum()
        plt.figure(figsize=(12, 6))
        daily_sales.plot(kind='line')
        plt.title('Sales Trend over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_sales_per_product(self):
        product_sales = self.total_sales_per_product()
        plt.figure(figsize=(10, 6))
        product_sales.plot(kind='bar')
        plt.title('Sales Per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def export_sales_report(self, output_file='sales_report.xlsx'):
        try:
            # Create summary dataframe
            summary_data = {
                'Metric': ['Total Sales', 'Average Daily Sales', 'Best Selling Product'],
                'Value': [self.data['Sales'].sum(), self.data['Sales'].mean(), self.best_selling_product]
            }
            summary_df = pd.DataFrame(summary_data)
            
            # Create product sales summary
            product_sales = self.total_sales_per_product().reset_index()
            product_sales.columns = ['Product', 'Total Sales']
            
            # Create daily sales trend
            daily_sales = self.data.groupby('Date')['Sales'].sum().reset_index()
            daily_sales.columns = ['Date', 'Total Sales']
            
            # Try different Excel engines
            try:
                writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
            except ImportError:
                try:
                    writer = pd.ExcelWriter(output_file, engine='openpyxl')
                except ImportError:
                    print("No Excel writer available. Using CSV format instead.")
                    summary_df.to_csv('sales_summary.csv', index=False)
                    product_sales.to_csv('product_sales.csv', index=False)
                    daily_sales.to_csv('daily_sales.csv', index=False)
                    print("CSV reports generated successfully")
                    return
            
            # Write to Excel
            summary_df.to_excel(writer, sheet_name='Sales Summary', index=False)
            product_sales.to_excel(writer, sheet_name='Product Sales', index=False)
            daily_sales.to_excel(writer, sheet_name='Daily Sales Trend', index=False)

            writer.close()
            print(f"Excel report generated successfully: {output_file}")

        except Exception as e:
            print(f"Error exporting report: {e}")


if __name__ == "__main__":
    print("Retail Sale Analyzer Starting...\n")

    analyzer = RetailSaleAnalyzer('retail_sales.csv')
    analyzer.data_clean()

    print("Total Sales per Product:\n", analyzer.total_sales_per_product())
    print("\nBest Selling Product:", analyzer.best_selling_product())
    print("\nAverage Daily Sales:", analyzer.average_daily_sales())

    analyzer.plot_sales_per_product()
    analyzer.plot_sales_trend()

    analyzer.export_sales_report()

    print("\nAnalysis and report generation complete!")
