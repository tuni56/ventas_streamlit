import streamlit as st
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Orders.csv')

# Asegúrate de que la columna 'Order Date' sea de tipo datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Título de la aplicación
st.title('Dashboard de Ventas')

# Filtro por rango de fechas
st.sidebar.subheader('Filtrar por fechas')
start_date = st.sidebar.date_input('Fecha de inicio', df['Order Date'].min())
end_date = st.sidebar.date_input('Fecha de fin', df['Order Date'].max())

# Convertir las fechas de entrada a datetime para hacer la comparación
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filtrar los datos por rango de fechas
date_filtered_df = df[(df['Order Date'] >= start_date) & (df['Order Date'] <= end_date)]

# Filtro por categoría de producto
category = st.sidebar.selectbox('Seleccionar categoría', df['Category'].unique())
category_filtered_df = date_filtered_df[date_filtered_df['Category'] == category]

# Mostrar los primeros registros del DataFrame filtrado
st.write(f"Mostrando datos de {category} entre {start_date.date()} y {end_date.date()}")
st.write(category_filtered_df)

# KPI de ventas
total_sales = category_filtered_df['Sales'].sum()
st.subheader('KPI de Ventas')
st.write(f"Ventas Totales: ${total_sales:,.2f}")

# KPI de cantidad
total_quantity = category_filtered_df['Quantity'].sum()
st.write(f"Cantidad Total: {total_quantity}")

# KPI de beneficios
total_profit = category_filtered_df['Profit'].sum()
st.write(f"Beneficio Total: ${total_profit:,.2f}")

# Visualización de ventas por ciudad
st.subheader('Ventas por Ciudad')
sales_by_city = category_filtered_df.groupby('City')['Sales'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_city)

# Visualización de ventas por estado
st.subheader('Ventas por Estado')
sales_by_state = category_filtered_df.groupby('State')['Sales'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_state)

# Visualización de productos más vendidos
st.subheader('Productos Más Vendidos')
top_products = category_filtered_df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(10)
st.write(top_products)

# Filtro por segmento de cliente
segment = st.sidebar.selectbox('Seleccionar segmento de cliente', df['Segment'].unique())
segment_filtered_df = category_filtered_df[category_filtered_df['Segment'] == segment]

# KPI de ventas por segmento
total_sales_segment = segment_filtered_df['Sales'].sum()
st.subheader(f'KPI de Ventas para el Segmento: {segment}')
st.write(f"Ventas Totales en este Segmento: ${total_sales_segment:,.2f}")
