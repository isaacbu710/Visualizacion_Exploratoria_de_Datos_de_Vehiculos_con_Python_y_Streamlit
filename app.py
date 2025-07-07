import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Obtener el puerto de entorno (opcional, pero no es obligatorio dentro del script si usas --server.port en Render)
port = int(os.environ.get('PORT', 8501))

# Cargar el archivo CSV desde la ruta relativa
car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualización de datos de vehículos')

# Crear un checkbox para permitir la construcción del histograma
build_histogram = st.checkbox('¿Construir histograma?')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Crear un checkbox para permitir la construcción del gráfico de dispersión
build_scatter_plot = st.checkbox('¿Construir gráfico de dispersión?')

if build_scatter_plot:
    st.write('Gráfico de dispersión: "odometer" vs "price"')
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title="Odometer vs. Price")
    st.plotly_chart(scatter_fig, use_container_width=True)


