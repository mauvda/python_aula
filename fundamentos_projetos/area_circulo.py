#!/usr/bin/python3
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print(TerminalColor.ERRO +
          "Inclua um valor numerico no comando \n"
          "utilize ", sys.argv[0][2:], " <raio>" +
          TerminalColor.NORMAL)


def circulo(raio):
    return pi * raio ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    elif not sys.argv[1].isnumeric():
        help()
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    print("Area do circulo é: ", circulo(raio))
else:
    print("você está no módulo ", __name__)
