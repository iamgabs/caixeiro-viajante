from individuo import Individuo

class IndividuoFactory:
    @staticmethod
    def criar_individuo(cidades, distancias, min_v=None, max_v=None):
        return Individuo(cidades, distancias, min_v, max_v)
