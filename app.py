import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Conjunto de datos de anuncios de venta de coches') # Encabezado

car_data = pd.read_csv('vehicles_us.csv') # Leer el dataframe vehicles_us
hist_checkbox = st.checkbox('Construir histograma.') # Crear un checkbox para el histograma
scatter_checkbox = st.checkbox('Construir gráfico de dispersión.') # Crear un checkbox para el gráfico de dispersión

if hist_checkbox: # Al hacer click en el checkbox del histograma
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches.')

    # Crea un histogrma
    fig = px.histogram(car_data, x='odometer')

    # Mostrar el histograma Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox: # Al hacer click en el checkbox del gráfico de dispersión
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches.')

    # Crea un gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')

    # Mostrar el gráfico de dispersión Plotly intercativo
    st.plotly_chart(fig, use_container_width=True)
