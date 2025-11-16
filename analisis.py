import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ============================================================================
# 1. Cargar datos del CSV
# ============================================================================

# Cargar el archivo CSV de ventas
df_ventas = pd.read_csv("ventas.csv", encoding="utf-8-sig")

# Convertir la columna fecha a tipo datetime
df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])

# Calcular el total de cada venta (cantidad * precio)
df_ventas["total"] = df_ventas["cantidad"] * df_ventas["precio"]

print("Datos cargados exitosamente")
print(f"Total de registros: {len(df_ventas)}")
print("\nPrimeras filas:")
print(df_ventas.head())
print("\n" + "="*70 + "\n")

# ============================================================================
# 2. Calcular ventas totales por mes
# ============================================================================

# Extraer año-mes de la fecha
df_ventas["año_mes"] = df_ventas["fecha"].dt.to_period("M")

# Agrupar por mes y sumar los totales
ventas_por_mes = df_ventas.groupby("año_mes")["total"].sum().reset_index()
ventas_por_mes["año_mes_str"] = ventas_por_mes["año_mes"].astype(str)

print("Ventas totales por mes:")
print(ventas_por_mes)
print("\n" + "="*70 + "\n")

# ============================================================================
# 3. Determinar producto más vendido y con mayor ingresos
# ============================================================================

# Producto más vendido (por cantidad total)
productos_cantidad = df_ventas.groupby("producto")["cantidad"].sum().reset_index()
productos_cantidad = productos_cantidad.sort_values("cantidad", ascending=False)
producto_mas_vendido = productos_cantidad.iloc[0]

# Producto con mayor ingresos (por total de ventas)
productos_ingresos = df_ventas.groupby("producto")["total"].sum().reset_index()
productos_ingresos = productos_ingresos.sort_values("total", ascending=False)
producto_mayor_ingresos = productos_ingresos.iloc[0]

print("Producto más vendido (por cantidad):")
print(f"  Producto: {producto_mas_vendido['producto']}")
print(f"  Cantidad total: {producto_mas_vendido['cantidad']} unidades")
print("\nProducto con mayor ingresos:")
print(f"  Producto: {producto_mayor_ingresos['producto']}")
print(f"  Ingresos totales: ${producto_mayor_ingresos['total']:,.2f}")
print("\n" + "="*70 + "\n")

# ============================================================================
# 4. Graficar ventas por mes
# ============================================================================

plt.figure(figsize=(12, 6))
plt.bar(ventas_por_mes["año_mes_str"], ventas_por_mes["total"], color="steelblue", edgecolor="black")
plt.xlabel("Mes", fontsize=12, fontweight="bold")
plt.ylabel("Ventas Totales ($)", fontsize=12, fontweight="bold")
plt.title("Ventas Totales por Mes", fontsize=14, fontweight="bold")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3, linestyle="--")
plt.tight_layout()
plt.savefig("ventas_por_mes.png", dpi=300, bbox_inches="tight")
print("Gráfico guardado: ventas_por_mes.png")
plt.close()

# ============================================================================
# 5. Graficar top 5 productos por ingresos
# ============================================================================

# Obtener los top 5 productos por ingresos
top_5_productos = productos_ingresos.head(5)

plt.figure(figsize=(10, 6))
plt.barh(top_5_productos["producto"], top_5_productos["total"], color="coral", edgecolor="black")
plt.xlabel("Ingresos Totales ($)", fontsize=12, fontweight="bold")
plt.ylabel("Producto", fontsize=12, fontweight="bold")
plt.title("Top 5 Productos por Ingresos", fontsize=14, fontweight="bold")
plt.grid(axis="x", alpha=0.3, linestyle="--")

# Agregar etiquetas con los valores en las barras
for i, v in enumerate(top_5_productos["total"]):
    plt.text(v, i, f"${v:,.2f}", va="center", fontweight="bold")

plt.tight_layout()
plt.savefig("top_5_productos.png", dpi=300, bbox_inches="tight")
print("Gráfico guardado: top_5_productos.png")
plt.close()

print("\n" + "="*70)
print("Análisis completado exitosamente")
print("="*70)

