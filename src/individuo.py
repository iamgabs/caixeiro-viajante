from random import randint, shuffle

class Individuo:
    def __init__(self, cidades, distancias, min_v=None, max_v=None):
        self.cidades = cidades
        self.distancias = distancias
        if min_v is not None and max_v is not None:
            self.cromossomo = [randint(min_v, max_v) for _ in range(len(cidades))]
        else:
            self.cromossomo = self.iniciar_individuo()
        self.fitness = self.get_fitness()

    def iniciar_individuo(self):
        cromossomo = self.cidades[:]
        shuffle(cromossomo)
        return cromossomo


    def ajustar_cromossomo(self, cromossomo):
        self.cromossomo = cromossomo
        self.fitness = self.get_fitness()


    def atualizar_aptidao(self):
        self.fitness = self.get_fitness()


    def get_fitness(self):
        return sum(self.distancias[self.cromossomo[i]][self.cromossomo[i + 1]] for i in range(len(self.cromossomo) - 1)) \
               + self.distancias[self.cromossomo[-1]][self.cromossomo[0]]  