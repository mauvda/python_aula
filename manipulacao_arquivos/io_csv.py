#!/usr/bin/python3
import csv

with open('pessoa.csv') as entrada:
    for registro in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*registro))
