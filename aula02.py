import matplotlib.pyplot as plt
import pandas as pd

def exibirGrafico():
    # Criar DataFrame
    dados = {
        "Categoria": ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis', 'Brinquedos'],
        "Vendas": [15000, 12000, 18000, 9000, 7000]
    }

    df = pd.DataFrame(dados)

    # Criar gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(
        df['Categoria'],
        df['Vendas'],
        color=['yellow', 'red', 'green', 'blue', 'brown', 'purple']
    )

    # Adicionar rótulos e título
    plt.title('Vendas por Categoria de Produto')
    plt.xlabel('Categoria')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45) # Rotaciona 45° a label do eixo X
    plt.grid(axis='both', linestyle='--', alpha=0.5)

    # Exibe dados estatísticos Para cada coluna
    print('-' * 10 + 'Dados de Categorias' + '-' * 10)
    print(df['Categoria'].describe())

    print('-' * 10 + 'Dados de Vendas' + '-' * 10)
    print(df['Vendas'].describe())

    plt.show()
    plt.savefig('chart2.png')
