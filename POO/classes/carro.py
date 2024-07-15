class Carro():
    def __init__(self, max, atual=0):
        self.max = max
        self.atual = atual

    def acelerar(self, delta=5):
        if self.atual + delta < self.max:
            self.atual += delta
            return f'Voce acelerou {delta} km/h e sua velocidade é de {self.atual} km/h'
        else:
            self.atual = self.max
            return f'Voce esta a {self.atual} km/h e não pode acelerar mais'

    def frear(self, delta=5):
        if self.atual - delta > 0:
            self.atual -= delta
            return f'Voce freou e sua velocidade atual é {self.atual} km/h'
        else:
            self.atual = 0
            return f'Voce parou o carro'


if __name__ == '__main__':
    c1 = Carro(max=180)

    for _ in range(25):
        print(c1.acelerar(3))
    for _ in range(10):
        print(c1.frear(20))
