import pandas as pd
import random
from datetime import datetime, timedelta

# Ruta al archivo de Mockaroo
archivo = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\MOCK_DATA.csv"

# Leer el CSV
df = pd.read_csv(archivo)

print(f"Registros leídos: {len(df)}")
print(f"Columnas: {df.columns.tolist()}\n")

# Generar fechas válidas aleatorias entre 2016-05-01 y 2021-04-30
fecha_inicio = datetime(2016, 5, 1)
fecha_fin = datetime(2021, 4, 30)
diferencia_dias = (fecha_fin - fecha_inicio).days

# Crear lista de fechas aleatorias
fechas = []
for _ in range(len(df)):
    dias_random = random.randint(0, diferencia_dias)
    fecha = fecha_inicio + timedelta(days=dias_random)
    fechas.append(fecha.strftime('%Y-%m-%d'))

# Asignar las fechas
df['ano_mes'] = fechas

# Renombrar a año_mes para coincidir con SQL
df.rename(columns={'ano_mes': 'año_mes'}, inplace=True)

print("Primeras 10 filas:")
print(df.head(10))

# Guardar limpio
salida = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\prestamos_final.csv"
df.to_csv(salida, index=False, encoding='utf-8')

print(f"\n✅ Archivo corregido: {salida}")
print(f"Total registros: {len(df)}")
