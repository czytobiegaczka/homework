'''
Napisz następujące funkcje:
2. fib(n)
Zwraca n-tą liczbę Fibonacciego, gdzie liczby Fibonacciego są zdefiniowane
następująco:
fib(0) = 0
fib(1) = 1
fin(n) = fib(n-2) + fib(n-1)
Co oznacza, że początkowe liczby Fibonacciego to: 0 1 1 2 3 5 8 13 21 34
Postaraj się do następnego spotkania ;) obliczyć tysięczną liczbę Fibonacciego
Dla chętnych: generator zwracający kolejne liczby Fibonacciego.
'''

def fib_ciag(n):
    ciag = []
    for count in range(n+1):
        if count == 0:
            ciag.append(0)
        elif count == 1:
            ciag.append(1)
        else:
            ciag.append(ciag[count-2] + ciag[count-1])
    return ciag

def fib_liczba(n):
    licz1 = 0
    licz2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for count in range(2, n+1):
        licz3 = licz1 + licz2
        licz1 = licz2
        licz2 = licz3

    return licz2

def fib_gen(n):
    licz1 = 0
    licz2 = 1
    for count in range(n+1):
        if count == 0:
            licz3 = 0
        elif count == 1:
            licz3 = 1
        else:
            licz3 = licz1 + licz2
        yield licz3
        licz1 = licz2
        licz2 = licz3

def main():
    print('CIĄG FIBONACCIEGO')
    liczba = int(input('podaj liczbę: '))
    generator = fib_gen(liczba)
    print(f'{liczba} elementem ciągu Fibonacciego jest : {fib_liczba(liczba)}')
    print(f'{liczba} kolejnych elementów ciągu Fibonacciego:')
    for i in range(liczba+1):
        print(f'F({i}) - {fib_ciag(liczba)[i]}')
    lista = [x for x in fib_gen(liczba)]
    print(lista)
    print(50*'-')
    for el in generator:
        print(el)

if __name__ == '__main__':
   main()
