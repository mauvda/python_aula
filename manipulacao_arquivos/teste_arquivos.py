#!/usr/bin/python3
# versao 1
# arquivo = open('pessoa.csv')
# dados = arquivo.read()
# arquivo.close()

# for info in dados.splitlines():
#     print('Nome: {}, Idade: {}'.format(*info.split(',')))
# Versao 2
# try:
#     arquivo = open('pessoa.csv')
#     for info in arquivo:
#         print('Nome: {} Idade: {}'.format(*info.strip().split(',')))
# finally:
#     arquivo.close()
# Versao 3
# with open('pessoa.csv') as arquivo:
#     for info in arquivo:
#         print('Nome: {} Idade: {}'.format(*info.strip().split(',')))
# Versao 4
with open('pessoa.csv') as arquivo:
    with open('pessoa.txt', 'w') as saida:
        for info in arquivo:
            pessoa = info.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)
