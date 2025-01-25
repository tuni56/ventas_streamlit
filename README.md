# Dashboard de Ventas 📊

Este repositorio contiene una aplicación interactiva desarrollada en Python utilizando Streamlit para analizar y visualizar datos de ventas a partir de un archivo CSV. La aplicación permite filtrar y explorar los datos según diferentes criterios, proporcionando métricas clave (KPI) y visualizaciones útiles.

## Características 🚀

- **Carga y procesamiento de datos**: Importa datos desde un archivo CSV (`Orders.csv`) y asegura el formato adecuado de las fechas.
- **Filtros personalizables**:
  - Rango de fechas.
  - Categoría de producto.
  - Segmento de cliente.
- **Métricas clave (KPIs)**:
  - Ventas totales.
  - Cantidad total de productos vendidos.
  - Beneficio total.
- **Visualizaciones**:
  - Ventas por ciudad.
  - Ventas por estado.
  - Productos más vendidos.
- **Interfaz interactiva**: Sidebar para aplicar filtros dinámicos y mostrar los resultados actualizados en tiempo real.

## Requisitos 📋

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior.
- Paquetes requeridos:
  - `streamlit`
  - `pandas`

Puedes instalarlos utilizando el siguiente comando:

```bash
pip install streamlit pandas
Uso 🛠️
Clona este repositorio:

bash
Copiar
Editar
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
Asegúrate de tener el archivo de datos Orders.csv en el mismo directorio que el script principal.

Ejecuta la aplicación:

bash
Copiar
Editar
streamlit run <NOMBRE_DEL_SCRIPT>.py
Interfaz de usuario:

Usa el sidebar para filtrar los datos por rango de fechas, categoría de producto y segmento de cliente.
Explora las métricas clave y visualizaciones en la sección principal de la aplicación.
Estructura del Proyecto 📂
bash
Copiar
Editar
├── Orders.csv                 # Archivo de datos (debes proporcionarlo).
├── dashboard.py               # Script principal de la aplicación.
├── README.md                  # Documentación del proyecto.
Visualizaciones Incluidas 📈
Ventas por Ciudad: Gráfico de barras con las ciudades con mayores ventas.
Ventas por Estado: Gráfico de barras mostrando las ventas agrupadas por estado.
Productos Más Vendidos: Lista con los 10 productos más vendidos por cantidad.
Ejemplo de Uso 📋
Supongamos que tienes un archivo Orders.csv con datos de ventas, incluyendo las columnas:

Order Date: Fecha de la orden.
Category: Categoría del producto.
Segment: Segmento del cliente.
Sales: Ventas generadas.
Quantity: Cantidad vendida.
Profit: Beneficio generado.
City: Ciudad.
State: Estado.
Product Name: Nombre del producto.
La aplicación procesará y visualizará estos datos de manera interactiva según tus filtros.

Contribuciones 🤝
¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación, sigue estos pasos:

Haz un fork de este repositorio.
Crea una rama para tu nueva funcionalidad:
bash
Copiar
Editar
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y haz un commit:
bash
Copiar
Editar
git commit -m "Añadir nueva funcionalidad"
Envía tus cambios:
bash
Copiar
Editar
git push origin feature/nueva-funcionalidad
Abre un Pull Request.
Licencia 📄
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.

Desarrollado con ❤️ usando Streamlit.
