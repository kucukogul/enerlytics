## 🌍 Project Overview

The **Renewable Energy Insights Dashboard** is a data analysis project that aims to explore and visualize renewable energy production trends across different countries and energy sources.  
It provides insight into how solar, wind, hydro, and other renewables have evolved over the years — helping data-driven decisions for sustainability.

---

## 🎯 Objectives

- Analyze renewable energy production data by **country, year, and energy source**
- Identify top-producing countries and growth trends
- Create **interactive visualizations** for better understanding
- Build a simple **Streamlit dashboard** for user interaction

---

## 🧩 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Programming | Python |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud / Render |
| Version Control | Git & GitHub |

---

## 📊 Features

✅ Clean and process renewable energy datasets (Kaggle or open-source)  
✅ Yearly and country-wise trend visualization  
✅ Energy source comparison (Solar, Wind, Hydro, etc.)  
✅ Interactive Streamlit dashboard  
✅ Ready-to-extend for ML forecasts or Big Data (Spark)

---

## 🧠 Future Enhancements

- Add **ARIMA / Prophet time series models** for energy forecasting
- Integrate **PostgreSQL** as a data source
- Migrate analysis to **PySpark** for large-scale datasets
- Add **API endpoint** to fetch live renewable energy data

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/kucukogul/enerlytics.git
cd enerlytics

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app/dashboard.py
