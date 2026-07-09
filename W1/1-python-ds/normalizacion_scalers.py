import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# cargar dataset
data = pd.read_csv('partidos_cebollitas.csv')
print(data.head())

# Aplicamos normalización a los tiros al arco
scaler_norm = MinMaxScaler()

data['tiros_arco_local_norm'] = scaler_norm.fit_transform(data[['tiros_arco_local']])
data['tiros_arco_visitante_norm'] = scaler_norm.fit_transform(data[['tiros_arco_visitante']])
print(data[['tiros_arco_local', 'tiros_arco_local_norm']].head(9))