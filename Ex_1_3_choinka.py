'''
Zadanie 1.3 Choinka
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach
„choinkę” ze znaków * . Np. dla parametru 3 powinno się wypisać:
   *
  ***
 *****
*******
'''

print('CHOINKA')
print('```````\n')

lines = 0

while lines <= 0:
    try:
        lines = int(input('ilość poziomów: '))
        if lines <= 0:
            print('dopuszczalne tylko liczby większe od 0')
    except Exception:
        print('możliwe tylko liczby całkowite dodatnie')

tree = ''
for count in range(1, lines + 1):
    tree = (lines - count) * ' '
    tree += ((count * 2) - 1) * '*'
    print(tree)


