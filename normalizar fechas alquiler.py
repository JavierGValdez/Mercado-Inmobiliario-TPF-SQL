import pandas as pd

# Leer tu archivo actual
ruta = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\Alquiler normalizado.xlsx"
df = pd.read_excel(ruta)  # O .csv según corresponda

# Convertir fecha de "Jul 2013" a "2013-07-01"
meses = {
    'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04',
    'May': '05', 'Jun': '06', 'Jul': '07', 'Ago': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12'
}

def convertir_fecha(row):
    mes_texto = row['mes']
    año = row['año']
    mes_num = meses.get(mes_texto, '01')
    return f"{año}-{mes_num}-01"

df['año_mes'] = df.apply(convertir_fecha, axis=1)

# Crear DataFrame final con solo las columnas necesarias
df_final = df[['id_departamento', 'precio_alquiler', 'año_mes']].copy()

ruta_salida = r"C:\Users\ASUS\Desktop\Javier\SQL Curso Coder\Proyecto Final SQL\Dataset\alquiler_limpio.csv"
df_final.to_csv(ruta_salida, index=False)
print(f"Archivo guardado en: {ruta_salida}")

# Guardar CSV limpio
df_final.to_csv('alquiler_limpio.csv', index=False)

print(f"✅ {len(df_final)} registros procesados")
print(df_final.head(10))