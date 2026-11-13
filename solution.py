import os #trabalha com caminhos
import pandas as pd #lê e manipula o arquivo CSV.
import numpy as np #realiza cálculos e operações com matrizes

PASTA = os.path.dirname(os.path.abspath(_file_))


def regressao_linear(arquivo):

    # Lê o arquivo CSV
    caminho = os.path.join(PASTA, arquivo)
    df = pd.read_csv(caminho)

    # Seleciona as variáveis
    area = df["area_util_m2"].to_list()
    quartos = df["quantidade_quartos"].to_list()
    preco = df["preco_venda"].to_list()

    # Cria a matriz X
    X = np.column_stack((
        np.ones(len(area)),
        area,
        quartos
    ))

    # Cria a matriz Y
    Y = np.array(preco)

    # Calcula os coeficientes
    beta = np.linalg.solve(X.T @ X, X.T @ Y)

    # Retorna os três coeficientes
    return beta.tolist()


# Teste da função
resultado = regressao_linear("imoveis_lar_perfeito.csv")

print(resultado)
