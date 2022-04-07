'''
Napisz następujące funkcje:
1. suma_cyfr(n)
Zwraca sumę wartości cyfr, z których składa się liczba n. Np. dla parametru 1023
wynikiem powinno być 6. n ma być typu int , a nie str.
2. fib(n)
Zwraca n-tą liczbę Fibonacciego, gdzie liczby Fibonacciego są zdefiniowane
następująco:
fib(0) = 0
fib(1) = 1
fin(n) = fib(n-2) + fib(n-1)
Co oznacza, że początkowe liczby Fibonacciego to: 0 1 1 2 3 5 8 13 21 34
Postaraj się do następnego spotkania ;) obliczyć tysięczną liczbę Fibonacciego
Dla chętnych: generator zwracający kolejne liczby Fibonacciego.
3. czy_pierwsza(liczba)
Sprawdza czy liczba jest pierwsza i zwraca True albo False.
'''

def suma_cyfr(n):
    suma = 0
    for cyfra in n:
        suma += int(cyfra)
    return suma

while True:
    try:
        liczba = input('podaj liczbę (koniec - pusty ciąg): ')
        if liczba == '':
            break
        print(f'suma cyfr liczby: {liczba} wynosi: {suma_cyfr(liczba)}')
    except Exception as e:
        print('dozwolone tylko liczby calkowite')



