from matplotlib import pyplot as plt

def grafico_do_algoritmo(solucao, nome, logger):
    plt.figure()

    plt.plot(solucao, label='Evolução Média')
    
    plt.title('Evolução Média do Algoritmo Genético')
    plt.xlabel('Gerações')
    plt.ylabel('Distância Total')

    plt.legend()

    plt.savefig(f'./img/{nome}.png')

    logger.info(f"Gráfico do Algoritmo Genético salvo como '{nome}.png'")

    plt.close()
