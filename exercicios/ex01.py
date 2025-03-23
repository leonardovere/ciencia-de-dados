# Criar um gráfico de barras para visualizar a população de diferentes cidades.
import matplotlib.pyplot as plt

cidade = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']
populacao = [12300, 6700, 2800, 1500, 1940]

plt.figure(figsize=[10.0, 8.0])
plt.bar(cidade, populacao, color=['#3F6CA6', '#548DBF', '#9BD1F2', '#8C8149', '#8C1C03'])

plt.title('Distribuição da população por cidades')
plt.xlabel('Cidade')
plt.ylabel('População (milhares)')

plt.show()
plt.savefig('exercicios/ex01.png')