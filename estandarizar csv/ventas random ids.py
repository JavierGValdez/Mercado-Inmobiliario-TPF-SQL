import pandas as pd
import random

ubi = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\Ventas normalizado.csv"

# Leer archivo
codificaciones = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
separadores = [';', ',', '\t']
df = None

for encoding in codificaciones:
    for sep in separadores:
        try:
            df = pd.read_csv(ubi, encoding=encoding, sep=sep)
            if len(df.columns) >= 2:
                break
        except:
            continue
    if df is not None and len(df.columns) >= 2:
        break

print(f"Columnas: {df.columns.tolist()}")
print(f"Registros: {len(df)}")

# Asignar IDs aleatorios
df['id_departamento'] = [random.randint(1, 3085) for _ in range(len(df))]

# Convertir año a fecha completa (año-01-01)
df['año_mes'] = df['año'].astype(str) + '-01-01'

# Seleccionar y ordenar columnas
df_final = df[['id_departamento', 'precio_venta', 'año_mes']]

print("\nPrimeras 5 filas:")
print(df_final.head())

# Guardar
ruta_salida = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\ventas_final.csv"
df_final.to_csv(ruta_salida, index=False, sep=',', encoding='utf-8')

print(f"\n✅ Guardado: {ruta_salida}")
