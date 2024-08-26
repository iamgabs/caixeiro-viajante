from ler_tsp import ler_arquivo_tsp
from analises import grafico_do_algoritmo
import logging
import colored_logs as colors
from executar_algoritmo_genetico import executar_algoritmo_genetico

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

    solucao = executar_algoritmo_genetico(
        n_execucoes, 
        cidades, 
        distancias,
        n_geracoes,
        n_pop,
        qt_individuos_torneio,
        tx_mut,
        logger
    )

    solucao2 = executar_algoritmo_genetico(
        n_execucoes, 
        cidades, 
        distancias,
        n_geracoes,
        n_pop,
        qt_individuos_torneio,
        (tx_mut+ 0.02),
        logger
    )

    grafico_do_algoritmo(solucao, 'grafico_algoritmo_1', logger)
    grafico_do_algoritmo(solucao2, 'grafico_algoritmo_2', logger)

