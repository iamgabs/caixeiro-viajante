from iniciar_populacao import iniciar_populacao
from torneio import selecao_torneio
from cruzamento import cruzamento_uniforme
from mutacao import mutacao_uniforme
from melhor_individuo import melhor_individuo
from ler_tsp import ler_arquivo_tsp

def algoritmo_genetico(cidades, distancias, n_geracoes, n_populacao, n_individuos_torneio, taxa_mutacao):
    populacao = iniciar_populacao(n_populacao, cidades, distancias)
    melhor_individuo_atual = melhor_individuo(populacao)

    for _ in range(n_geracoes):
        nova_populacao = []

        while len(nova_populacao) < n_populacao:
            pai1 = selecao_torneio(populacao, n_individuos_torneio)
            pai2 = selecao_torneio(populacao, n_individuos_torneio)

            filho1, filho2 = cruzamento_uniforme(pai1, pai2)

            mutacao_uniforme(filho1, taxa_mutacao)
            mutacao_uniforme(filho2, taxa_mutacao)

            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        populacao = nova_populacao
        melhor_individuo_geracao = melhor_individuo(populacao)

        if melhor_individuo_geracao.fitness < melhor_individuo_atual.fitness:
            melhor_individuo_atual = melhor_individuo_geracao

    return melhor_individuo_atual


if __name__ == '__main__':
    nome_arquivo = "brazil58.tsp"
    cidades, distancias = ler_arquivo_tsp(nome_arquivo)
    melhor_solucao = algoritmo_genetico(cidades, distancias, n_geracoes=100, n_populacao=50, n_individuos_torneio=5, taxa_mutacao=0.1)
    print("______________________________________________")
    print('\033[96m', f'''Melhor solução encontrada: {melhor_solucao.cromossomo} \n
    com distância total de {int(melhor_solucao.fitness)}''', '\033[0m')
    print("______________________________________________")

