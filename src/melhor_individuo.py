
def melhor_individuo(populacao):
    return min(populacao, key=lambda ind: ind.fitness)