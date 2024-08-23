from individuo import Individuo
from random import randint

def cruzamento_uniforme(individuo1, individuo2):
    n_genes = len(individuo1.cromossomo)
    filho1 = Individuo(individuo1.cidades, individuo1.distancias)
    filho2 = Individuo(individuo2.cidades, individuo2.distancias)

    filho1_cr = []
    filho2_cr = []

    for i in range(n_genes):
        if randint(0, 1) == 0:
            filho1_cr.append(individuo1.cromossomo[i])
            filho2_cr.append(individuo2.cromossomo[i])
        else:
            filho1_cr.append(individuo2.cromossomo[i])
            filho2_cr.append(individuo1.cromossomo[i])

    filho1.ajustar_cromossomo(filho1_cr)
    filho2.ajustar_cromossomo(filho2_cr)

    return filho1, filho2