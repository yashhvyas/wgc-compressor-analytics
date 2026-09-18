# wgc-compressor-analytics
"Data analysis project on an FCC Wet Gas Compressor — cleaning, EDA, outlier detection, and correlation analysis on real-style operating parameters (pressure, temperature, vibration, RPM)."
# WGC Data Cleaning & Trend Analysis

Basic data cleaning + visualization on Wet Gas Compressor (WGC) operating data — suction/discharge pressure, temperature (both stages), vibration, RPM, seal gas pressure, lube oil pressure/temp, and anti-surge valve position.

This is a practice project for my data analyst transition — real plant-style sensor data, cleaned up and plotted to look for correlations (here, vibration vs seal gas pressure trend).

## Files

- `wgc_raw_data_2.csv` — raw compressor data (15-min interval readings)
- `WGC.py` — cleaning script: loads raw CSV, checks shape/nulls/dtypes, drops duplicates, converts timestamp to datetime, exports cleaned CSV
- `visu.py` — plots Vibration vs Seal Gas Pressure on a dual-axis line chart

## How to run

```bash
python WGC.py      # cleans raw data -> wgc_numeric_data.csv
python visu.py      # generates vibration_vs_sealgas.png
```

Needs `pandas`, `numpy`, `matplotlib`.

## Notes

- Raw values come with units baked into the string (e.g. `1.18 kg`, `35.18 C`) — cleaning strips these where needed before plotting.
- `WGC.py` currently points to a local path (`/Users/macbook/Desktop/wgc_raw_data 2.csv`) — update this to `wgc_raw_data_2.csv` before running on another machine.
- Next step: extend cleaning to strip units from all pressure/temp columns (not just vibration/seal gas), then build a fuller dashboard.

## Background

Working as a Field Executive in FCCU at Reliance Jamnagar, so this dataset is modeled on the kind of compressor parameters I actually monitor on shift. Using it to build up my Python/pandas skills for data analytics.
