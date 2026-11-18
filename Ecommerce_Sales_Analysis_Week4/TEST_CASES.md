# Test cases

| Test | Action | Expected result |
|---|---|---|
| 1 | Run `python main.py` with the supplied CSV | Metrics, three charts, and report are generated |
| 2 | Temporarily rename the CSV and run | A clear missing-file error appears |
| 3 | Remove a required CSV column and run | A missing-columns error appears |
| 4 | Use an empty CSV and run | An empty-data or CSV parsing error appears |
| 5 | Open generated PNG files | Charts show titles and labels |
