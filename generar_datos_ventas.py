import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuración
np.random.seed(42)  # Para reproducibilidad
random.seed(42)

# Productos disponibles
productos = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Auriculares",
    "Webcam", "Tablet", "Smartphone", "Impresora", "Router",
    "Disco Duro", "Memoria RAM", "Procesador", "Tarjeta Gráfica", "Fuente de Poder"
]

# Generar fechas (últimos 6 meses)
fecha_inicio = datetime.now() - timedelta(days=180)
fecha_fin = datetime.now()

# Número de registros a generar
num_registros = 1000

# Generar datos sintéticos
datos = []

for i in range(num_registros):
    # Fecha aleatoria en el rango
    dias_aleatorios = random.randint(0, 180)
    fecha = fecha_inicio + timedelta(days=dias_aleatorios)
    
    # Producto aleatorio
    producto = random.choice(productos)
    
    # Cantidad (1-10 unidades)
    cantidad = random.randint(1, 10)
    
    # Precio según el producto (con variación)
    precios_base = {
        "Laptop": 800, "Mouse": 25, "Teclado": 50, "Monitor": 200,
        "Auriculares": 80, "Webcam": 60, "Tablet": 300, "Smartphone": 500,
        "Impresora": 150, "Router": 40, "Disco Duro": 100, "Memoria RAM": 80,
        "Procesador": 250, "Tarjeta Gráfica": 400, "Fuente de Poder": 70
    }
    
    precio_base = precios_base[producto]
    # Precio con variación del ±20%
    precio = round(precio_base * (1 + random.uniform(-0.2, 0.2)), 2)
    
    datos.append({
        "fecha": fecha.strftime("%Y-%m-%d"),
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio
    })

# Crear DataFrame
df_ventas = pd.DataFrame(datos)

# Ordenar por fecha
df_ventas = df_ventas.sort_values("fecha").reset_index(drop=True)

# Guardar en CSV
df_ventas.to_csv("ventas.csv", index=False, encoding="utf-8-sig")

print(f"Datos generados exitosamente: {num_registros} registros")
print(f"Archivo guardado: ventas.csv")
print("\nPrimeras 10 filas:")
print(df_ventas.head(10))
print("\nResumen estadístico:")
print(df_ventas.describe())
print("\nDistribución por producto:")
print(df_ventas["producto"].value_counts())

