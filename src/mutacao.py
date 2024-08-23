from random import random, randint

def mutacao_uniforme(individuo, taxa_mutacao):
    n_genes = len(individuo.cromossomo)
    novo_cromossomo = []

    for i in range(n_genes):
        if random() < taxa_mutacao:
            novo_valor = randint(0, n_genes - 1) 
            novo_cromossomo.append(novo_valor)
            print(f'Mutou o gene {i}!')
        else:
            novo_cromossomo.append(individuo.cromossomo[i])

    individuo.ajustar_cromossomo(novo_cromossomo)
    print(f'Indivíduo antes da mutação: {individuo.cromossomo}')
    print(f'Indivíduo depois da mutação: {novo_cromossomo}')
    return individuo