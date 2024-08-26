from iniciar_populacao import iniciar_populacao
from torneio import selecao_torneio
from cruzamento import cruzamento_ox
from mutacao import mutacao
from melhor_individuo import melhor_individuo
from individuo import Individuo
from time_watcher import timer

@timer
def algoritmo_genetico(cidades, distancias, n_geracoes, n_populacao, n_individuos_torneio, taxa_mutacao, logger):
    populacao = iniciar_populacao(n_populacao, cidades, distancias, logger)
    melhor_individuo_atual = melhor_individuo(populacao)
    vetor_solucao = []

    for contador_geracoes in range(n_geracoes):
        nova_populacao = []

        while len(nova_populacao) < n_populacao:
            pai1 = selecao_torneio(populacao, n_individuos_torneio)
            pai2 = selecao_torneio(populacao, n_individuos_torneio)

            filho1_cr, filho2_cr = cruzamento_ox(pai1, pai2)

            filho1 = Individuo(cidades, distancias)
            filho2 = Individuo(cidades, distancias)
            
            filho1.ajustar_cromossomo(filho1_cr)
            filho2.ajustar_cromossomo(filho2_cr)

            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)

            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        populacao = nova_populacao
        melhor_individuo_geracao = melhor_individuo(populacao)

        if melhor_individuo_geracao.fitness < melhor_individuo_atual.fitness:
            melhor_individuo_atual = melhor_individuo_geracao

        vetor_solucao.append(melhor_individuo_geracao.fitness)
        print(f'[{contador_geracoes + 1}: {melhor_individuo_geracao.fitness} x {melhor_individuo_atual.fitness}]')

    return melhor_individuo_atual, vetor_solucao
