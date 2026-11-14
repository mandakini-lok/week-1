"""
Week 3 Project: Sales Data Analysis
Loads a CSV file, explores and cleans the data, calculates sales metrics,
and creates analysis_report.md.
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("sales_data.csv")
REPORT_FILE = Path(__file__).with_name("analysis_report.md")


def load_data(file_path):
    """Load the sales CSV file."""
    return pd.read_csv(file_path)


def explore_data(df):
    """Print basic information about the original dataset."""
    print("\n========== DATASET EXPLORATION ==========")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nFirst five rows:")
    print(df.head())
    print("=========================================")


def clean_data(df):
    """Clean missing values, correct data types, and remove duplicates."""
    cleaned = df.copy()

    # Treat blank text cells as missing values.
    cleaned = cleaned.replace(r"^\s*$", pd.NA, regex=True)

    # Convert numerical columns; invalid values become missing.
    numeric_columns = ["Quantity", "Price", "Total_Sales"]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    # Replace missing product names with a clear label.
    cleaned["Product"] = cleaned["Product"].fillna("Unknown")

    # Fill missing quantity and price with zero for this practice dataset.
    cleaned["Quantity"] = cleaned["Quantity"].fillna(0)
    cleaned["Price"] = cleaned["Price"].fillna(0)

    # Recalculate sales so the value always matches quantity multiplied by price.
    cleaned["Total_Sales"] = cleaned["Quantity"] * cleaned["Price"]

    # Remove repeated records.
    before = len(cleaned)
    cleaned = cleaned.drop_duplicates().copy()
    removed_duplicates = before - len(cleaned)

    return cleaned, removed_duplicates


def analyze_sales(df):
    """Calculate key sales metrics."""
    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()

    product_quantity = df.groupby("Product")["Quantity"].sum()
    best_selling_product = product_quantity.idxmax() if not product_quantity.empty else "N/A"
    best_selling_quantity = product_quantity.max() if not product_quantity.empty else 0

    product_revenue = df.groupby("Product")["Total_Sales"].sum()
    highest_revenue_product = product_revenue.idxmax() if not product_revenue.empty else "N/A"

    return {
        "total_revenue": total_revenue,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "best_selling_product": best_selling_product,
        "best_selling_quantity": best_selling_quantity,
        "highest_revenue_product": highest_revenue_product,
        "records_analyzed": len(df),
    }


def create_report(metrics, removed_duplicates, missing_after_cleaning):
    """Write a formatted Markdown report with the calculated results."""
    report = f"""# Sales Data Analysis Report

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
- Duplicate records removed: **{removed_duplicates}**.
- Missing values remaining after cleaning: **{missing_after_cleaning}**.

## 5. Analysis Results
| Metric | Result |
|---|---:|
| Records analyzed | {metrics['records_analyzed']} |
| Total revenue | Rs. {metrics['total_revenue']:,.2f} |
| Best-selling product (by quantity) | {metrics['best_selling_product']} |
| Quantity of best-selling product | {metrics['best_selling_quantity']:,.0f} |
| Product with highest revenue | {metrics['highest_revenue_product']} |
| Average sale per record | Rs. {metrics['average_sale']:,.2f} |
| Highest single sale | Rs. {metrics['highest_sale']:,.2f} |
| Lowest single sale | Rs. {metrics['lowest_sale']:,.2f} |

## 6. Conclusion
The analysis summarizes overall revenue and identifies products performing well by quantity and revenue.
The report is generated automatically by running `sales_analysis.py`.

## 7. How to Run
1. Install the required library using `python -m pip install -r requirements.txt`.
2. Keep `sales_analysis.py` and `sales_data.csv` in the same folder.
3. Run `python sales_analysis.py`.
"""
    REPORT_FILE.write_text(report, encoding="utf-8")


def main():
    """Run the complete sales analysis workflow."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {{DATA_FILE.name}}. Keep it in the same folder as this script."
        )

    df = load_data(DATA_FILE)
    explore_data(df)

    cleaned_df, removed_duplicates = clean_data(df)
    missing_after_cleaning = int(cleaned_df.isnull().sum().sum())
    metrics = analyze_sales(cleaned_df)

    print("\n========== CLEANING SUMMARY ==========")
    print(f"Duplicate rows removed: {removed_duplicates}")
    print(f"Missing values after cleaning: {missing_after_cleaning}")

    print("\n========== SALES ANALYSIS ==========")
    print(f"Total Revenue: Rs. {metrics['total_revenue']:,.2f}")
    print(f"Best Selling Product: {metrics['best_selling_product']}")
    print(f"Quantity Sold: {metrics['best_selling_quantity']:,.0f}")
    print(f"Highest Revenue Product: {metrics['highest_revenue_product']}")
    print(f"Average Sales: Rs. {metrics['average_sale']:,.2f}")
    print(f"Highest Sale: Rs. {metrics['highest_sale']:,.2f}")
    print(f"Lowest Sale: Rs. {metrics['lowest_sale']:,.2f}")

    create_report(metrics, removed_duplicates, missing_after_cleaning)
    print(f"\nReport created successfully: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
