# Criar um gráfico de barras para visualizar o faturamento mensal.
import matplotlib.pyplot as plt

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
faturamento = [25000, 28000, 22000, 31000, 27000]

plt.bar(mes, faturamento, color=['#520120', '#08403E', '#706513', '#B57114', '#962B09'])

plt.title('Faturamento Mensal')
plt.xlabel('Mês')
plt.ylabel('Faturamento (R$)')

plt.show()
plt.savefig('exercicios/ex03.png')