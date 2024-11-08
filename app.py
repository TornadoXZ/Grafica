import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Actividad"]  # Cambia esto por el nombre de tu base de datos
collection = db["Base"]  # Cambia esto por el nombre de tu colección

# Obtener los datos desde MongoDB
datos = list(collection.find())

# Convertir los datos a un DataFrame
df = pd.DataFrame(datos)

# Verificar las columnas y las primeras filas
print("Columnas disponibles:", df.columns)
print("Primeras filas del DataFrame:")
print(df.head())

# Agrupar los datos por 'Deporte o Servicio' y calcular la media de la 'Edad'
df_agrupado = df.groupby("Deporte o Servicio")["Edad"].mean().reset_index()

# Mostrar el DataFrame agrupado
print("Datos agrupados:")
print(df_agrupado)

# Graficar los resultados
plt.figure(figsize=(10,6))
plt.bar(df_agrupado["Deporte o Servicio"], df_agrupado["Edad"], color='skyblue')
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para que no se sobrepongan
plt.xlabel("Deporte o Servicio")
plt.ylabel("Edad promedio")
plt.title("Edad promedio por Deporte o Servicio")
plt.tight_layout()  # Ajustar el diseño para que todo encaje bien
plt.show()
