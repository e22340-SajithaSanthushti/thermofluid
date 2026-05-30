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
├── .gitignore              # Ignores environment trackers
├── __init__.py             # Package initialization mapping
├── core.py                 # Numerical interpolation engine
├── main.py                 # Interactive execution terminal interface
├── README.md               # User documentation
├── air_ideal_gas.csv       # Dataset tables
├── co2_ideal_gas.csv       
└── ...


==============================================
    THERMOFLUID PROPERTIES LOOKUP ENGINE      
==============================================
Available Tables:
 1. Saturated Water   (water_sat_T.csv)
 2. Air Ideal Gas      (air_ideal_gas.csv)
 3. Nitrogen (N2)      (n2_ideal_gas.csv)
 ...
Select a table number (1-10): 2
Enter target temperature (K): 350

[+] Calculation Complete! Interpolated Properties:
----------------------------------------------
  Temperature    : 350.0000
  h              : 350.4900
  P_r            : 2.3790
  u              : 250.0200
  v_r            : 422.2000
  s_deg          : 1.8575
----------------------------------------------
