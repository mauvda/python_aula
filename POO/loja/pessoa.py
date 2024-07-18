MAIOR_IDADE = 18


class Pessoa:
    # Inicializador
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Metodo para retorno de string da classe
    def __str__(self):
        # Valida se idade tem valor e depois exibe
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade} anos)'

    # Valida maioridade
    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE
