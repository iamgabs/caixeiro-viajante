from random import randint

def cruzamento_ox(pai1, pai2):
    n = len(pai1.cromossomo)
    filho1 = [-1] * n
    filho2 = [-1] * n
    
    start, end = sorted([randint(0, n - 1) for _ in range(2)])
    
    filho1[start:end+1] = pai1.cromossomo[start:end+1]
    filho2[start:end+1] = pai2.cromossomo[start:end+1]

    p2_values = [gene for gene in pai2.cromossomo if gene not in filho1]
    p1_values = [gene for gene in pai1.cromossomo if gene not in filho2]

    idx_filho1 = (end + 1) % n
    idx_filho2 = (end + 1) % n

    for value in p2_values:
        if filho1[idx_filho1] == -1:
            filho1[idx_filho1] = value
        else:
            idx_filho1 = (idx_filho1 + 1) % n
            filho1[idx_filho1] = value

    for value in p1_values:
        if filho2[idx_filho2] == -1:
            filho2[idx_filho2] = value
        else:
            idx_filho2 = (idx_filho2 + 1) % n
            filho2[idx_filho2] = value

    return filho1, filho2