import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('ventas.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

# Calcular ventas por mes
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())
ventas_por_mes = ventas_por_mes.sort_index()

# Si ventas_por_mes es index Period, convertir a str para mejor manejo
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6,4))
ventas_por_mes.plot(kind='bar')
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas (€)")
plt.tight_layout()
plt.savefig("ventas_por_mes.png")
plt.show()

# Calcular ventas por producto
df['ingreso'] = df['cantidad'] * df['precio']
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})

# Top 5 productos por ingresos
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()

