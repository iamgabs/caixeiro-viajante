from ler_tsp import ler_arquivo_tsp
from algoritmo_genetico import algoritmo_genetico
import logging
import colored_logs as colors

handler = logging.StreamHandler()
handler.setFormatter(colors.formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger = logging.getLogger(__name__)

n_pop = 30
n_genes = 5
min_v = -5
max_v = 5
qt_individuos_torneio = 3
tx_mut = 0.05
n_geracoes = 100
n_execucoes = 5

if __name__ == '__main__':
    nome_arquivo = "./brazil58.tsp"
    cidades, distancias = ler_arquivo_tsp(nome_arquivo, logger)
    melhor_solucao, historico_solucoes = algoritmo_genetico(cidades, distancias, n_geracoes=100, n_populacao=50, n_individuos_torneio=5, taxa_mutacao=0.1, logger=logger)
    
    print("______________________________________________")
    print('\033[96m', f'''Melhor solução encontrada: {melhor_solucao.cromossomo} \n
    com distância total de {int(melhor_solucao.fitness)}''', '\033[0m')
    print("______________________________________________")

