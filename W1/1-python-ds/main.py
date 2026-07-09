import pandas as pd

"""
vector = np.array([1, 2, 3, 4])
matriz = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(vector.shape) # Indica que es un vector de n items
print(matriz.shape) # Indica que es una matriz de nxn
"""

data = pd.read_csv("partidos_cebollitas.csv")
print(data.head()) # Revisar los primeros datos de la info

data.info() # Revisar las columnas del archivo.

# Manejo de datos faltantes
data.isnull().sum()
data['goles_local'] = data['goles_local'].fillna(data['goles_local'].mean())
print("Valores nulos de imputación: ")
print(data.isnull().sum())

# One-hot
data = pd.get_dummies(data, columns=['equipo_local', 'equipo_visitante'])
print(data.head())

# Eliminar filas duplicadas
data.drop_duplicates(inplace=True)

print("Filas antes de eliminar duplicados: ", len(data))
data.drop_duplicates(inplace=True)
print("Filas después: ", len(data))

# Manejo de fechas
data['fecha_partido'] = pd.to_datetime(data['fecha_partido'], errors='coerce')

print("Fechas inválidas (NaT) luego de la conversión: ")
print(data['fecha_partido'].isnull().sum())

# Vista del ds manipulado
print(data.head())
print("Shape final del dataset: ", data.shape)