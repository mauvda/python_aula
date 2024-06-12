from random import randint


def rolar_dado():
    return randint(1, 6)


for x in range(1, 7):
    if (x % 2 == 1):
        continue
    if (rolar_dado() == x):
        print(f'Encontrou o nomero {x} e ganhou')
        break
else:
    print("Não teve vencedores")
