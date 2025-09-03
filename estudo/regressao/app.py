import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dados = pd.read_csv('./estudo/regressao/Consumo_cerveja.csv', sep=';')
print(dados)

# Retorna número de linhas e colunas
print(dados.shape)

# Descritivas
print(dados.describe().round(2))

# Matriz de correlação 

# utilizado para identificar se duas variaveis tem relação onde uma sobe a outra desce
# ou se uma sobe, a outra também sobe
dados_corr = dados

del dados_corr['data']

print(dados_corr.corr().round(4))
