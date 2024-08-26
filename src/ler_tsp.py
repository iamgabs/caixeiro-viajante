import numpy as np

def ler_arquivo_tsp(nome_arquivo, logger: object):
    logger.info('[Lendo TSP] ...............')
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()

    cidades = list(range(int(linhas[3].split()[-1])))  # Número de cidades
    distancias = np.zeros((len(cidades), len(cidades)))

    linha_inicial = linhas.index("EDGE_WEIGHT_SECTION\n") + 1
    valores = list(map(int, ' '.join(linhas[linha_inicial:]).split()))

    k = 0
    for i in range(len(cidades) - 1):
        for j in range(i + 1, len(cidades)):
            distancias[i][j] = valores[k]
            distancias[j][i] = valores[k]
            k += 1

    logger.info('[Leitura do TSP finalizada]')

    return cidades, distancias