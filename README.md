# Análisis de Ventas

Este proyecto genera datos sintéticos de ventas y realiza análisis con visualizaciones.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### 1. Generar datos sintéticos

Ejecuta el script para generar datos sintéticos:

```bash
python generar_datos_ventas.py
```

Esto generará un archivo `ventas.csv` con las siguientes columnas:
- **fecha**: Fecha de la venta (últimos 6 meses)
- **producto**: Nombre del producto vendido
- **cantidad**: Cantidad de unidades vendidas (1-10)
- **precio**: Precio unitario del producto

### 2. Análisis completo

Ejecuta el script de análisis completo:

```bash
python analisis.py
```

Este script realiza:
- Cálculo de ventas totales por mes
- Identificación del producto más vendido y con mayor ingresos
- Generación de gráficos de ventas por mes y top 5 productos

### 3. Generar gráficos

Ejecuta el script para generar visualizaciones:

```bash
python grafico_ventas.py
```

Genera dos gráficos:
- `ventas_por_mes.png`: Gráfico de barras con ventas mensuales
- `top5_productos.png`: Top 5 productos por ingresos

## Estructura de datos

El archivo CSV contiene 1000 registros de ventas sintéticas con 15 productos diferentes de tecnología.

## Archivos del proyecto

- `generar_datos_ventas.py`: Genera datos sintéticos de ventas
- `analisis.py`: Análisis completo de ventas
- `grafico_ventas.py`: Genera visualizaciones de los datos
- `ventas.csv`: Datos de ventas (generado)
- `requirements.txt`: Dependencias del proyecto

