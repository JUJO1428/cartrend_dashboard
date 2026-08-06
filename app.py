import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('construir histograma')

if hist_button:
    st.write('Análisis de ventas de vehiculos usados en Estados Unidos')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('construir diagrama de dispresión')

if disp_button:
    st.write('Analisis de ventas de vehiculos utilizando diagrama de dispresión')
    fig2 = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig2, use_container_width=True)


