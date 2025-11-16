# Análisis de Ventas

Este proyecto genera datos sintéticos de ventas para análisis.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script para generar datos sintéticos:

```bash
python generar_datos_ventas.py
```

Esto generará un archivo `ventas.csv` con las siguientes columnas:
- **fecha**: Fecha de la venta (últimos 6 meses)
- **producto**: Nombre del producto vendido
- **cantidad**: Cantidad de unidades vendidas (1-10)
- **precio**: Precio unitario del producto

## Estructura de datos

El archivo CSV contiene 1000 registros de ventas sintéticas con 15 productos diferentes de tecnología.

