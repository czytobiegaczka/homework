'''
Zadanie 1.2 Pole trójkąta
Napisz program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta
o takich bokach.
Wzór Herona: √ p(p−a)( p−b)( p−c) , gdzie p jest połową obwodu: (a+b+c)/2 .
Pierwiastek kwadratowy to funkcja sqrt z modułu math, można też podnieść do potęgi 0.5.
'''

from math import sqrt


def add_side(_side):
    while True:
        try:
            new_side = float(input(f'bok {_side} = '))
            if new_side == 0:
                print('\nKONIEC PROGRAMU- DO ZOBACZENIA')
                exit()
            elif new_side < 0:
                print('dopuszczalne tylko liczby większe od 0')
            else:
                return new_side
        except Exception:
            print('dopuszczalne tylko liczby')



def is_triangle(_triangle):
    one, two, three = _triangle
    if one + two > three and one + three > two and two + three > one:
        return True
    else:
        print(f'boki o długościach: {one:.2f}, {two:.2f}, {three:.2f} - nie tworzą trójkąta')
        return False


triangle = []

print('POLE TRÓJKĄTA')
print('``````````````')
print('podaj wymiary trójkąta ( 0 - koniec obliczeń): \n')

while True:
    for side in range(1, 4):
        triangle.append(add_side(side))
    if is_triangle(triangle):
        break
    else:
        triangle = []

a, b, c = triangle
p = (a + b + c) / 2

print(f'\nPole trójkąta o bokach: {a:.2f}, {b:.2f}, {c:.2f} wynosi: {sqrt(p * (p - a) * (p - b) * (p - c)):.2f} ')
