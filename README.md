# 🌍 Renewable Energy Insights Dashboard

The **Renewable Energy Insights Dashboard** is a data analysis project focused on the **United States**, exploring how renewable energy production — including solar, wind, hydroelectric, geothermal, and biomass — has evolved from 1973 to 2024. 

---

## 🎯 Objectives

- Analyze U.S. renewable energy production by **year, energy source, and sector** (e.g., electric power, industrial)
- Identify long-term **growth trends** and **structural shifts** in energy mix
- Create **interactive visualizations** to reveal patterns and anomalies
- Deliver insights through a user-friendly **Streamlit dashboard**

---

## 🧩 Tech Stack

| Category         | Tools / Libraries                     |
|------------------|---------------------------------------|
| Programming      | Python                                |
| Data Handling    | Pandas, NumPy                         |
| Visualization    | Matplotlib, Seaborn, Plotly           |
| Dashboard        | Streamlit                             |
| Deployment       | Streamlit Cloud / Render              |
| Version Control  | Git & GitHub                          |

---

## 📊 Features

✅ Clean and aggregate monthly EIA data into **annual totals**  
✅ Visualize **historical trends (1973–2024)** by energy type  
✅ Compare contributions of **solar, wind, hydro, geothermal, biomass, and waste**  
✅ Interactive Streamlit dashboard with dynamic filtering  
✅ Modular design — ready to extend with **time-series forecasting** (e.g., Prophet, ARIMA)

---
## 📂 Project Structure

```
.
enerlytics/
├── app/
│ └── dashboard.py
├── data/
│ └── cleaned_us_renewable_energy.csv
│ └── cleaned_us_renewable_energy_no_2024.csv
│ └── us_renewable_energy_consumption.csv
├── notebooks/
│ └── 01_data_cleaning.ipynb
│ └── 02_analysis.ipynb
│ └── 03_forecasting.ipynb
├── LICENSE
├── README.md
```

---

## ⚖️ License

MIT
