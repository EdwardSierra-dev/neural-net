import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
data = pd.read_csv("partidos_cebollitas.csv")
print(data.head(10))

# Estadisticas generales
print(data.describe())

# Promedio de goles
promedio_goles_local = data[data['equipo_local'] == 'Cebollitas FC']['goles_local'].mean()
promedio_goles_visitante = data[data['equipo_visitante'] == 'Cebollitas FC']['goles_visitante'].mean()

print("Promedio de goles de local:", promedio_goles_local)
print("Promedio de goles de visitante:", promedio_goles_visitante)

# Histograma de goles
fig, ax = plt.subplots(1,2, figsize=(12,4))

sns.histplot(data['goles_local'], kde=True, ax=ax[0], bins=10)
ax[0].set_title("Distribución de goles equipo local")

sns.histplot(data['goles_visitante'], kde=True, ax=ax[1], bins=10, color='red')
ax[1].set_title("Distribución de goles equipo visitante")
plt.show()

# Box plot para goles del equipo, rango habitual y señala los extremos
sns.boxplot(x=data['goles_local'])
plt.title("Boxplot goles")
plt.show()

# Scatterplot de posesión vs goles
sns.scatterplot(x='posesion_local (%)', y='goles_local', data=data)
plt.title("Relación posesión vs goles marcados (local)")
plt.show()

# Mapa de calor de correlación entre variables clave
plt.figure(figsize=(10,6))
sns.heatmap(data[['goles_local', 'goles_visitante', 'posesion_local (%)', 
                  'posesion_visitante (%)', 'tiros_arco_local', 
                  'tiros_arco_visitante']].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de calor - correlación entre variables")
plt.show()