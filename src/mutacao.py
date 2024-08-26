from random import random, randint


def mutacao(individuo, taxa_mutacao):
    if random() < taxa_mutacao:
        a, b = sorted([randint(0, len(individuo.cromossomo) - 1) for _ in range(2)])
        individuo.cromossomo[a], individuo.cromossomo[b] = individuo.cromossomo[b], individuo.cromossomo[a]
        individuo.atualizar_aptidao()