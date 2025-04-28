# Water Distribution Analytics Dashboard

🚰 **Analyzing sewer pipeline infrastructure data using Python (Pandas, Matplotlib) and QGIS mapping.**

---

## 📋 Project Overview

This project analyzes a city's sewer pipeline network using historical construction data.  
It calculates important asset management metrics like **pipe age** and **pipe size category**,  
visualizes material distributions, and prepares data for GIS spatial mapping.

The goal is to help prioritize **infrastructure maintenance**, **identify high-risk pipes**, and **support urban planning**.

---

## 🛠️ Technologies Used

- Python 3.9
- Pandas
- Matplotlib
- QGIS 3.x (for map overlays and joins)
- Microsoft Excel / CSV files

---

## 📈 Features and Analysis Performed

- **Load and Clean Data:**
  - Import raw sewer pipe attribute data (`Sewer_Pipes.csv`) into Pandas.
  - Safely convert `ConstructionDate` into usable datetime format.

- **Pipeline Aging Analysis:**
  - Calculate **Pipe Age** = `2025 - Construction Year`.

- **Pipeline Capacity Categorization:**
  - Classify pipes as **Small (<300mm)**, **Medium (300–600mm)**, or **Large (>600mm)** diameter.

- **Visualization Dashboards:**
  - Histogram of Pipe Age distribution.
  - Bar Chart of Pipe Material distribution.
  - Pie Chart of Pipe Size Category proportions.

- **Enhanced Data Export:**
  - Save processed analytical data to `processed_sewer_pipes.csv` for GIS mapping.

- **Spatial Join in QGIS:**
  - Join enhanced attributes to original sewer shapefile.
  - Create custom maps showing pipe age, material, and size conditions.

---

## 🚀 How to Run the Project

1. Clone or download the repository.
2. Install dependencies:

pip install pandas matplotlib

Run the analysis script:
python dashboard.py
