import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet


st.set_page_config(
    page_title="Renewable Energy Insights Dashboard",
    page_icon="🌍",
    layout="wide"
)

@st.cache_data
def load_data():
    project_root = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(project_root, "data", "cleaned_us_renewable_energy_no_2024.csv")
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str))
    return df

df = load_data()

def get_yearly_total(df):
    renewable_cols = [
        'Hydroelectric Power', 'Geothermal Energy', 'Solar Energy',
        'Wind Energy', 'Wood Energy', 'Waste Energy',
        'Fuel Ethanol, Excluding Denaturant'
    ]
    yearly = df.groupby('Year')[renewable_cols].sum().reset_index()
    yearly['Total'] = yearly[renewable_cols].sum(axis=1)
    return yearly, renewable_cols

def get_sectoral_2023(df):
    df_2023 = df[df['Year'] == 2023]
    sectoral = df_2023.groupby('Sector')['Total_Renewable'].sum().sort_values(ascending=False)
    return sectoral

st.title("🌍 US Renewable Energy Insights Dashboard")
st.markdown("""
This dashboard analyzes **U.S. renewable energy consumption from 1973 to 2023**,  
covering trends by energy source, sector, and long-term forecasting.
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview",
    "⚡ By Energy Source",
    "🏭 By Sector (2023)",
    "🔮 10-Year Forecast"
])

with tab1:
    st.header("Total Renewable Energy Consumption (1973–2023)")
    yearly, _ = get_yearly_total(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(yearly['Year'], yearly['Total'], marker='o', linewidth=2, color='green')
    ax.set_xlabel("Year")
    ax.set_ylabel("Consumption (Trillion BTU)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with tab2:
    st.header("Consumption by Energy Source")
    yearly, renewable_cols = get_yearly_total(df)
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in renewable_cols:
        ax.plot(yearly['Year'], yearly[col], label=col, linewidth=2)
    ax.set_xlabel("Year")
    ax.set_ylabel("Consumption (Trillion BTU)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with tab3:
    st.header("Sectoral Distribution (2023)")
    sectoral = get_sectoral_2023(df)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sectoral.values, labels=sectoral.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

with tab4:
    st.header("10-Year Forecast (2025–2034) using Prophet")

    if st.button("Run Forecast"):
        with st.spinner("Training Prophet model..."):
            ts_df = df.groupby('Date')['Total_Renewable'].sum().reset_index()
            ts_df.columns = ['ds', 'y']

            model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=False,
                daily_seasonality=False,
                changepoint_prior_scale=0.05
            )
            model.fit(ts_df)

            future = model.make_future_dataframe(periods=120, freq='MS')
            forecast = model.predict(future)

            fig = model.plot(forecast, figsize=(12, 6))
            ax = fig.gca()
            ax.axvline(x=pd.to_datetime('2024-01-01'), color='red', linestyle='--', label='Forecast Start')
            ax.legend()
            st.pyplot(fig)

            st.subheader("Forecast Summary (2030 & 2034)")
            forecast_2030 = forecast[forecast['ds'].dt.year == 2030]['yhat'].mean()
            forecast_2034 = forecast[forecast['ds'].dt.year == 2034]['yhat'].mean()
            st.metric("Expected Consumption in 2030", f"{forecast_2030:,.0f} Trillion BTU")
            st.metric("Expected Consumption in 2034", f"{forecast_2034:,.0f} Trillion BTU")

st.markdown("---")
st.caption("💡 Data Source: U.S. Energy Information Administration (EIA) | Project: [Enerlytics](https://github.com/kucukogul/enerlytics)")