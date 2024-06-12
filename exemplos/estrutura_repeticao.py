from random import randint

numero_informado = {20}
numero_secreto = int (randint(0, 9))

while numero_secreto not in numero_informado:
    numero_informado = int(randint(0, 9))
    if numero_informado != numero_secreto:
        print('Voce tentou o numero', numero_informado, 'e falhou')

print('Numero encontrado, o nomero é:', numero_informado)