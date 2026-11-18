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
REQUIRED = {"Order_ID", "Date", "Product", "Category", "Quantity", "Unit_Price", "Total_Sales"}

def load_data(path):
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
    data = df.copy().drop_duplicates(subset=["Order_ID"])
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for col in ["Quantity", "Unit_Price", "Total_Sales"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data = data.dropna(subset=["Date", "Product", "Category", "Quantity", "Unit_Price", "Total_Sales"])
    data = data[(data["Quantity"] > 0) & (data["Unit_Price"] >= 0) & (data["Total_Sales"] >= 0)]
    data["Total_Sales"] = (data["Quantity"] * data["Unit_Price"]).round(2)
    if data.empty:
        raise ValueError("No valid records remain after cleaning.")
    return data

def analyze(df):
    category = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
    monthly = (df.assign(Month=df["Date"].dt.to_period("M").astype(str))
                 .groupby("Month")["Total_Sales"].sum().sort_index())
    orders = df["Order_ID"].nunique()
    revenue = df["Total_Sales"].sum()
    return {"category": category, "monthly": monthly, "orders": orders,
            "revenue": revenue, "units": int(df["Quantity"].sum()),
            "average": revenue / orders if orders else 0}

def make_charts(m):
    CHARTS.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))
    m["category"].plot(kind="bar")
    plt.title("Total Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS / "bar_chart.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    m["monthly"].plot(kind="line", marker="o")
    plt.title("Monthly E-commerce Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (INR)")
    plt.xticks(rotation=35, ha="right")
    plt.grid(True, alpha=.3)
    plt.tight_layout()
    plt.savefig(CHARTS / "line_chart.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 6))
    m["category"].plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Share of Sales by Product Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHARTS / "pie_chart.png", dpi=150)
    plt.close()

def write_report(df, m):
    REPORT.mkdir(exist_ok=True)
    best_cat = m["category"].idxmax()
    best_month = m["monthly"].idxmax()
    low_month = m["monthly"].idxmin()
    report_text = f"""# E-commerce Sales Analysis Report

## Project overview
This project explores a sample online-store dataset to compare product categories
and understand monthly sales trends.

## Dataset
- Valid records: **{len(df)}**
- Unique orders: **{m['orders']}**
- Date range: **{df['Date'].min().date()} to {df['Date'].max().date()}**

## Key metrics
| Metric | Result |
|---|---:|
| Total revenue | INR {m['revenue']:,.2f} |
| Number of orders | {m['orders']} |
| Units sold | {m['units']} |
| Average order value | INR {m['average']:,.2f} |

## Sales by category
{m['category'].to_frame('Sales (INR)').to_markdown()}

## Monthly sales
{m['monthly'].to_frame('Sales (INR)').to_markdown()}

## Charts
### Bar chart - sales by category
![Bar chart](../visualizations/bar_chart.png)

### Line chart - monthly sales trend
![Line chart](../visualizations/line_chart.png)

### Pie chart - share by category
![Pie chart](../visualizations/pie_chart.png)

## Insights
- **{best_cat}** is the highest-revenue category in this sample.
- **{best_month}** is the strongest sales month.
- **{low_month}** is the lowest sales month.

## Limitations
This is synthetic practice data, not real company information.

## Conclusion
The project demonstrates loading, validation, cleaning, analysis, visualization,
and communicating results in a written report.
"""
    (REPORT / "analysis_report.md").write_text(report_text, encoding="utf-8")

def main():
    try:
        print("E-COMMERCE SALES ANALYSIS")
        print("=" * 32)
        raw = load_data(DATA)
        print(f"Loaded rows: {len(raw)}")
        df = clean_data(raw)
        print(f"Valid rows after cleaning: {len(df)}")
        print("\\nDataset preview:")
        print(df.head().to_string(index=False))
        m = analyze(df)
        print("\\nKEY METRICS")
        print(f"Total revenue: INR {m['revenue']:,.2f}")
        print(f"Orders: {m['orders']} | Units sold: {m['units']}")
        print(f"Average order value: INR {m['average']:,.2f}")
        print("\\nSales by category:")
        print(m["category"].to_string())
        make_charts(m)
        write_report(df, m)
        print("\\nSUCCESS: Three charts and the report have been created.")
        print(f"Charts folder: {CHARTS}")
        print(f"Report file: {REPORT / 'analysis_report.md'}")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as err:
        print(f"DATA ERROR: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"UNEXPECTED ERROR: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
