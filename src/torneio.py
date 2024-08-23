from random import randint

def selecao_torneio(populacao, n_individuos):
    indice_melhor_torneio = randint(0, len(populacao) - 1)
    for _ in range(n_individuos - 1):
        indice = randint(0, len(populacao) - 1)
        if populacao[indice].fitness < populacao[indice_melhor_torneio].fitness:
            indice_melhor_torneio = indice
    return populacao[indice_melhor_torneio]