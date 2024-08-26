from algoritmo_genetico import algoritmo_genetico

def executar_algoritmo_genetico(n_execucoes, cidades, distancias, n_geracoes, n_populacao, n_individuos_torneio, taxa_mutacao, logger):
    evolucao_media = [0] * n_geracoes 

    for exec in range(n_execucoes): 
        melhor_solucao, historico_solucoes = algoritmo_genetico(
            cidades, 
            distancias, 
            n_geracoes=n_geracoes, 
            n_populacao=n_populacao, 
            n_individuos_torneio=n_individuos_torneio, 
            taxa_mutacao=taxa_mutacao, 
            logger=logger
        )

        if len(historico_solucoes) != n_geracoes:
            raise ValueError("O comprimento de historico_solucoes não corresponde a n_geracoes")

        for i in range(n_geracoes):
            evolucao_media[i] += historico_solucoes[i]

    for i in range(n_geracoes):
        evolucao_media[i] /= n_execucoes

    return evolucao_media
