import matplotlib.pyplot as plt

def exibirGrafico():
    # Dados de exemplo
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    temperaturas = [29, 31, 30, 28, 27, 25]
    
    # Redimensionando o gráfico
    plt.figure(figsize=[10.0, 5.0])

    # Criação do gráfico
    plt.plot(meses, temperaturas)

    #Exibindo o gráfico
    plt.show()

    plt.savefig('chart3.png')