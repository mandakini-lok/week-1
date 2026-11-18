# Week 4 - E-commerce Sales Analysis

## Overview
A beginner Python project using pandas and Matplotlib to load, clean, analyze,
and visualize e-commerce sales data.

## Project structure
- `data/sales_data.csv` - 100 sample order records
- `main.py` - complete analysis program
- `visualizations/` - generated bar, line, and pie charts
- `report/analysis_report.md` - generated metrics and written insights
- `requirements.txt` - required Python libraries

## Setup on Windows PowerShell
1. Extract this ZIP file and open the extracted project folder in VS Code.
2. Open Terminal > New Terminal.
3. Create a virtual environment: `py -m venv .venv`
4. Activate it: `.\.venv\Scripts\Activate.ps1`
   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.
5. Install packages: `python -m pip install -r requirements.txt`
6. Run the project: `python main.py`

## Expected outputs
The program creates three PNG charts in `visualizations/` and a completed
`analysis_report.md` in `report/`.

## Technical details
pandas handles CSV loading, validation, cleaning, grouping, and calculations.
Matplotlib creates the charts. pathlib creates paths relative to the project.
The program handles missing files, missing columns, empty data, and invalid rows.

## Dataset note
The included 100-row dataset is synthetic practice data, not real business data.
