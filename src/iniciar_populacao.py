from factory.individuo_factory import IndividuoFactory

def iniciar_populacao(n_individuos, cidades, distancias):
    populacao = [IndividuoFactory.criar_individuo(cidades, distancias) for _ in range(n_individuos)]
    return populacao
