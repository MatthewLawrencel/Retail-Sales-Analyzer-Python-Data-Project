Retail Sales Data Analysis
A comprehensive data engineering project analyzing retail sales data using Python, Pandas, and data visualization techniques.

🚀 Project Overview
This project demonstrates how to:

Extract data from retail sales CSV files

Transform and clean sales data

Analyze sales performance and trends

Generate visual reports and Excel exports

🧩 Tech Stack
Python 3.8+

pandas - Data analysis

matplotlib - Data visualization

xlsxwriter - Excel reports

⚙️ How It Works
1️⃣ Extract
Reads sales data from retail_sales.csv file

2️⃣ Transform
Cleans and processes the data:

Handles missing values

Converts data types

Validates data quality

3️⃣ Analyze
Performs sales analysis:

Product performance ranking

Sales trend analysis

Daily sales metrics

4️⃣ Report
Generates Excel reports and visual charts

Run the Pipeline
bash
# Install dependencies
pip install pandas matplotlib xlsxwriter openpyxl

# Run the analysis
python retail_sale_analyzer.py
Example Output
text
🚀 Retail Sale Analyzer Starting...

✅ Cleaned data: Removed 2 rows with missing values.

📊 Total Sales per Product:
 Product_A    12500.00
Product_B     8900.50
Product_C     7200.25

🏆 Best Selling Product: Product_A

💵 Average Daily Sales: 1250.75

📁 Excel report generated successfully: sales_report.xlsx

✅ Analysis complete!
Analysis Summary:
📦 Total sales entries: 150

📊 Product Performance:

text
 Product_A: $12,500
 
 Product_B: $8,900
 
 Product_C: $7,200
🏆 Best Seller: Product_A

💵 Average Daily Sales: $1,250

Project Structure
text
Retail-Sales-Analyzer/
│
├── retail_sale_analyzer.py    # Main analysis script
├── retail_sales.csv           # Sample data
├── sales_report.xlsx          # Generated report
└── README.md
Data Format
Create retail_sales.csv with these columns:

Date (YYYY-MM-DD)

Sales (numeric)

Product (text)

Example:

csv
Date,Sales,Product
2024-01-01,150.00,Product_A
2024-01-01,89.99,Product_B
Author
Matthew Lawrence L
Bengaluru, Karnataka

lawrence82773824@gmail.com

