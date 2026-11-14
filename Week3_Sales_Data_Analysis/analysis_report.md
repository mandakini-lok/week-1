# Sales Data Analysis Report

## 1. Project Overview
This project uses Python and Pandas to explore, clean, and analyze a sample sales dataset.

## 2. Objectives
- Load sales data from a CSV file.
- Inspect rows, columns, data types, and missing values.
- Clean missing or invalid values and remove duplicate records.
- Calculate sales performance metrics.

## 3. Tools Used
- Python
- Pandas
- CSV
- Visual Studio Code (VS Code)

## 4. Data Cleaning
- Missing product names were replaced with `Unknown`.
- Missing or invalid quantity and price values were replaced with `0`.
- `Total_Sales` was recalculated as `Quantity × Price`.
- Duplicate records removed: **1**.
- Missing values remaining after cleaning: **0**.

## 5. Analysis Results
| Metric | Result |
|---|---:|
| Records analyzed | 99 |
| Total revenue | Rs. 4,430,100.00 |
| Best-selling product (by quantity) | Monitor |
| Quantity of best-selling product | 54 |
| Product with highest revenue | Laptop |
| Average sale per record | Rs. 44,748.48 |
| Highest single sale | Rs. 315,000.00 |
| Lowest single sale | Rs. 0.00 |

## 6. Conclusion
The analysis summarizes overall revenue and identifies products performing well by quantity and revenue.
The report is generated automatically by running `sales_analysis.py`.

## 7. How to Run
1. Install the required library using `python -m pip install -r requirements.txt`.
2. Keep `sales_analysis.py` and `sales_data.csv` in the same folder.
3. Run `python sales_analysis.py`.
