# 🌍 Renewable Energy Insights Dashboard

The **Renewable Energy Insights Dashboard** is a data analysis project focused on the **United States**, exploring how renewable energy production — including solar, wind, hydroelectric, geothermal, and biomass — has evolved from 1973 to 2024. 

---

## 🎯 Objectives

- Analyze U.S. renewable energy consumption by **year, energy source, and sector** (Electric Power, Industrial, Residential, etc.)
- Identify long-term **growth trends** and **structural shifts** (e.g., solar/wind surpassing hydro)
- Detect and explain **anomalies** (e.g., incomplete 2024 data)
- Forecast future consumption using **time-series models**
- Deliver interactive insights via a **Streamlit dashboard**

---

## 🧠 Key Findings

- **Wind and solar** show exponential growth post-2010, now rivaling hydroelectric power.
- **Electric Power** sector accounts for **~40%** of total renewable consumption (2023).
- **2024 data is incomplete** (only Jan–May available), so all analyses use data **through 2023**.
- **Holt-Winters outperforms Prophet** in forecasting accuracy:
  - Holt-Winters MAE: **19.22**
  - Prophet MAE: **34.48**

---

## 🧩 Tech Stack

| Category         | Tools / Libraries                     |
|------------------|---------------------------------------|
| Programming      | Python                                |
| Data Handling    | Pandas, NumPy                         |
| Time-Series      | Prophet, statsmodels (Holt-Winters)   |
| Visualization    | Matplotlib, Seaborn                   |
| Dashboard        | Streamlit                             |
| Deployment       | Streamlit Cloud                       |
| Version Control  | Git & GitHub                          |

---

## 📊 Features

✅ Clean and process raw EIA data (`us_renewable_energy_consumption.csv`)  
✅ Aggregate monthly data into **reliable annual trends (1973–2023)**  
✅ Visualize consumption by **7 renewable sources**  
✅ Compare **sectoral distribution** (Electric Power, Transportation, etc.)  
✅ Interactive Streamlit dashboard with tabs for **Overview, By Source, By Sector, and Forecast**  
✅ Time-series forecasting with **Holt-Winters (primary)** and Prophet (benchmark)  
✅ 10-year outlook (2025–2034) with user-selectable models

---
## 📂 Project Structure

```
.
enerlytics/
├── app/
│ └── dashboard.py # Streamlit dashboard
├── data/
│ └── us_renewable_energy_consumption.csv # Raw data
│ └── cleaned_us_renewable_energy_no_2024.csv # Processed (1973–2023)
│ └── cleaned_us_renewable_energy.csv # (Optional: includes partial 2024)
├── notebooks/
│ └── 01_data_cleaning.ipynb # Data loading & preprocessing
│ └── 02_analysis.ipynb # EDA & visualizations
│ └── 03_forecasting.ipynb # Holt-Winters & Prophet models
├── LICENSE
├── README.md
├── requirements.txt
```

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/kucukogul/enerlytics.git
cd enerlytics

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app/dashboard.py
```

> 👉 https://powerthefuture.streamlit.app/

---

## ⚖️ License

MIT
