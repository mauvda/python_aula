# # [ expressão for item in list if condição ]
# dobro_de_pares = [i * 2 for i in range(11) if i % 2 == 0]
# print(dobro_de_pares)

# generator = (i ** 2 for i in range(10) if i % 2 == 0)
# print(next(generator))  # Saida 0
# print(next(generator))  # Saida 4
# print(next(generator))  # Saida 8
# print(next(generator))  # Saida 16
# print(next(generator))  # Saida 64
# # print(next(generator)) Fail
# generator = (i ** 2 for i in range(10) if i % 2 == 0)
# for numero in generator:
#     print(numero)
# dicionario = {i: i * 2 for i in range(11) if i % 2 == 0}
# print(dicionario)

# for numero, dobro in dicionario.items():
#     print(f'{numero} X 2 = {dobro}')
