from .pessoa import Pessoa


class Cliente(Pessoa):
    # Contrutor da class junto com construtor da Super Classe
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    # Metodo para armazenar compras na lista compras[]
    def registrar_compra(self, compra):
        self.compras.append(compra)

    # Metodo para litar ultima compra, organizando com sorted()
    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=lambda compra: compra.data)[-1].data

    # Metodo para listar valor total das compras armazenadas em compras[]
    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
