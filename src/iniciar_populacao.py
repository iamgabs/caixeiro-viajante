from factory.individuo_factory import IndividuoFactory

def iniciar_populacao(n_individuos, cidades, distancias, logger: object):
    populacao = [IndividuoFactory.criar_individuo(cidades, distancias) for _ in range(n_individuos)]
    logger.info('[população iniciada] ..........')
    return populacao
