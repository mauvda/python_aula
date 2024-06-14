#!/usr/bin/python3
# Quarto Campo: nome_orige , Nono Campo: nivel_orig
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        with open('ibge.txt', 'w') as saida:
            print('Baixando CSV....')
            dados = entrada.read().decode('latin1')
            print('Download Completo')
            for cidade in csv.reader(dados.splitlines()):
                print(f'{cidade[8]}: {cidade[3]}', file=saida)


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
