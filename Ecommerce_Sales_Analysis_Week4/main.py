from pathlib import Path
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_data.csv"
CHARTS = ROOT / "visualizations"
REPORT = ROOT / "report"
REQUIRED = {"Order_ID", "Date", "Category", "Quantity", "Total_Sales"}

def load_data(path):
    """Load the CSV and validate its columns and contents."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing CSV columns: {', '.join(sorted(missing))}")
    if df.empty:
        raise ValueError("The CSV file contains no data rows.")
    return df

def clean_data(df):
    """Remove duplicate orders and invalid or incomplete records."""
    data = df.copy().drop_duplicates(subset=["Order_ID"])
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for col in ["Quantity", "Total_Sales"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna(subset=["Date", "Category", "Quantity", "Total_Sales"])
    data = data[(data["Quantity"] > 0) & (data["Total_Sales"] >= 0)]
    if data.empty:
        raise ValueError("No valid records remain after cleaning.")
    return data

def analyze(df):
    """Calculate revenue, orders, units, category sales, and monthly sales."""
    category = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
    monthly = (df.assign(Month=df["Date"].dt.to_period("M").astype(str))
                 .groupby("Month")["Total_Sales"].sum().sort_index())
    orders = df["Order_ID"].nunique()
    revenue = df["Total_Sales"].sum()
    return {
        "category": category, "monthly": monthly, "orders": orders,
        "revenue": revenue, "units": int(df["Quantity"].sum()),
        "average": revenue / orders if orders else 0
    }

def make_charts(metrics):
    """Save bar, line, and pie charts in the visualizations folder."""
    CHARTS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    metrics["category"].plot(kind="bar")
    plt.title("Total Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS / "bar_chart.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    metrics["monthly"].plot(kind="line", marker="o")
    plt.title("Monthly E-commerce Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=35, ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHARTS / "line_chart.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 6))
    metrics["category"].plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Share of Sales by Product Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHARTS / "pie_chart.png", dpi=150)
    plt.close()

def write_report(df, metrics):
    """Create a Markdown report with calculated results and chart links."""
    REPORT.mkdir(parents=True, exist_ok=True)
    best_category = metrics["category"].idxmax()
    best_month = metrics["monthly"].idxmax()
    lowest_month = metrics["monthly"].idxmin()
    content = f"""# E-commerce Sales Analysis Report

## 1. Project overview
This project analyzes a sample e-commerce dataset to compare product categories
and understand monthly sales trends.

## 2. Dataset
- Valid records: **{len(df)}**
- Dataset columns: **{len(df.columns)}**
- Unique orders: **{metrics['orders']}**
- Date range: **{df['Date'].min().date()} to {df['Date'].max().date()}**

## 3. Key metrics
| Metric | Result |
|---|---:|
| Total revenue | INR {metrics['revenue']:,.2f} |
| Number of orders | {metrics['orders']} |
| Units sold | {metrics['units']} |
| Average order value | INR {metrics['average']:,.2f} |

## 4. Sales by category
{metrics['category'].to_frame('Sales (INR)').to_markdown()}

## 5. Monthly sales
{metrics['monthly'].to_frame('Sales (INR)').to_markdown()}

## 6. Visualizations
### Bar chart - sales by category
![Bar chart](../visualizations/bar_chart.png)

### Line chart - monthly sales trend
![Line chart](../visualizations/line_chart.png)

### Pie chart - share by category
![Pie chart](../visualizations/pie_chart.png)

## 7. Insights
- **{best_category}** is the highest-revenue category in this sample.
- **{best_month}** is the strongest sales month.
- **{lowest_month}** is the lowest sales month.
- The category charts compare revenue shares, while the line chart shows
  month-to-month revenue changes.

## 8. Limitations
This is synthetic practice data, not real company information. Customer,
discount, return, and cost data would be needed for deeper business conclusions.

## 9. Conclusion
The project demonstrates loading, validation, cleaning, analysis, visualization,
and communicating findings in a written report.
"""
    (REPORT / "analysis_report.md").write_text(content, encoding="utf-8")

def main():
    try:
        print("E-COMMERCE SALES ANALYSIS")
        print("=" * 32)
        raw = load_data(DATA)
        print(f"Loaded rows: {len(raw)}")
        print(f"Dataset columns: {len(raw.columns)}")
        df = clean_data(raw)
        print(f"Valid rows after cleaning: {len(df)}")
        print("\nDataset preview:")
        print(df.head().to_string(index=False))

        metrics = analyze(df)
        print("\nKEY METRICS")
        print(f"Total revenue: INR {metrics['revenue']:,.2f}")
        print(f"Orders: {metrics['orders']} | Units sold: {metrics['units']}")
        print(f"Average order value: INR {metrics['average']:,.2f}")
        print("\nSales by category:")
        print(metrics["category"].to_string())

        make_charts(metrics)
        write_report(df, metrics)
        print("\nSUCCESS: Three charts and the report have been created.")
        print(f"Charts folder: {CHARTS}")
        print(f"Report file: {REPORT / 'analysis_report.md'}")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"DATA ERROR: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"UNEXPECTED ERROR: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
