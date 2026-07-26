# Inventory Reorder Alert System

A simple Python script that reads inventory data from a CSV file, identifies items that need restocking, and generates a restock report.

## Features
- Reads inventory data from a CSV file
- Checks stock against reorder thresholds
- Classifies items as **Low** or **Critical**
- Suggests reorder quantities
- Exports a `restock_report.csv`
- Prints a simulated email alert

## Files
- `inventory_reorder.py` – Main Python script
- `inventory.csv` – Sample inventory data
- `restock_report.csv` – Generated report

## Run

```bash
python inventory_reorder.py
```

## Tech Stack
- Python
- CSV (`csv` module)
