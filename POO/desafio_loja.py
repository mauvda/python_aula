#!/usr/bin/python3
from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro Garrido', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2024, 7, 18), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtd_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtd_compras} compras')
    print(f'Ultima compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
else:
    print(__name__)
