# Thermofluid Properties Lookup Engine

A lightweight, robust command-line interface (CLI) tool designed to replace manual textbook appendix lookups for mechanical and aerospace engineering applications. This package dynamically loads fluid and gas property tables and applies mathematically accurate linear interpolation models to find properties at intermediate states.

## 🚀 Features
- **Dynamic File Parsing**: Auto-detects and structures multi-column thermodynamic property metrics from independent variables.
- **Linear Interpolation Core**: Uses `scipy.interpolate` structures to compute precise fractional intermediate state points.
- **Extensible Database Design**: Add any custom gas or liquid chart effortlessly by placing an organized CSV file directly into the internal dataset directory.
- **Interactive CLI Menu**: Simple terminal selection matrix showing all available textbook references.

## 📂 Repository Structure
```text
thermofluid/
├── .venv/                  # Isolated Python environment
├── thermofluid/            # Main source package
│   ├── data/               # CSV database (Tables A-17 to A-25, Saturated Water)
│   ├── __init__.py         # Package initialization mapping
│   └── core.py             # Numerical interpolation engine
├── .gitignore              # Ignores environment and cache trackers
├── main.py                 # Interactive execution terminal interface
├── README.md               # User documentation
└── requirements.txt        # Engine dependency tracking definitions
# Thermofluid Properties Lookup Engine
An interactive CLI engine for linear interpolation of fluid and gas properties.