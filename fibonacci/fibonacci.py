#!/user/local/bin/python3
def fibonacci(limite, numeros=(0, 1)):
    return numeros if len(numeros) == limite else \
        fibonacci(limite, numeros + (sum(numeros[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
else:
    print(f'Voce esta em {__name__}')
