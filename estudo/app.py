import pandas as pd

dados = pd.read_csv('./estudo/dados.csv')

print(dados)

# Exibe os dados de uma coluna do dataset
print(sorted(dados['Anos de Estudo'].unique()))
print(sorted(dados['UF'].unique()))
print(sorted(dados['Sexo'].unique()))
print(sorted(dados['Cor'].unique()))

# Variáveis qualitativas contínuas
print(f'De {dados.Altura.min()} até {dados.Altura.max()} metros')