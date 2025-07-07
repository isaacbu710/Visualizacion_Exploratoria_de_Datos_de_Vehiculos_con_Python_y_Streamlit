import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV desde la ruta correcta
car_data = pd.read_csv('car_data = pd.read_csv('vehicles_us.csv')')

# Crear un checkbox para permitir la construcción del histograma
build_histogram = st.checkbox('¿Construir histograma?')

# Si el checkbox está marcado, crear el histograma
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos')
    
    # Crear el histograma de la columna 'odometer'
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly con un key único
    st.plotly_chart(fig, use_container_width=True, key="histogram_odometer")

# Crear un checkbox para permitir la construcción del gráfico de dispersión
build_scatter_plot = st.checkbox('¿Construir gráfico de dispersión?')

# Si el checkbox está marcado, crear el gráfico de dispersión
if build_scatter_plot:
    st.write('Creación de un gráfico de dispersión para los datos de "odometer" vs "price"')
    
    # Crear el gráfico de dispersión entre "odometer" y "price"
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title="Odometer vs. Price")
    
    # Mostrar el gráfico Plotly con un key único
    st.plotly_chart(scatter_fig, use_container_width=True, key="scatter_odometer_price")


