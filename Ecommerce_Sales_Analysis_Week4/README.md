# Week 4 - E-commerce Sales Analysis

## Project overview
A beginner Python project using pandas and Matplotlib to load, clean, analyze,
and visualize e-commerce sales data.

## Project structure
- `data/sales_data.csv` - 100 rows and 5 columns of sample data
- `main.py` - complete analysis program
- `visualizations/` - generated bar, line, and pie charts
- `report/analysis_report.md` - generated metrics and written insights
- `requirements.txt` - required Python libraries
- `TEST_CASES.md` - validation and testing checklist

## Setup on Windows PowerShell
1. Extract this ZIP and open the extracted folder in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment: `py -m venv .venv`
4. Activate it: `.\.venv\Scripts\Activate.ps1`
   If activation is blocked, use Command Prompt: `.venv\Scripts\activate.bat`
5. Install packages: `python -m pip install -r requirements.txt`
6. Run the project: `python main.py`

## Expected outputs
Three PNG charts are saved in `visualizations/`; the completed report is saved
as `report/analysis_report.md`.

## Technical details
pandas performs CSV loading, validation, cleaning, grouping, and calculations.
Matplotlib creates the charts. pathlib creates paths relative to this project.
Error handling checks missing files, missing columns, empty data, and invalid rows.

## Dataset note
The included 100-row, 5-column dataset is synthetic practice data, not real business data.
