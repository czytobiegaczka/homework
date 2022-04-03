'''
Zadanie 1.2 Pole trójkąta
Napisz program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta
o takich bokach.
Wzór Herona: √ p(p−a)( p−b)( p−c) , gdzie p jest połową obwodu: (a+b+c)/2 .
Pierwiastek kwadratowy to funkcja sqrt z modułu math, można też podnieść do potęgi 0.5.
'''

def is_sum_of_one_and_two_more_than_three(one, two, three):
    if one == 0 or two == 0 or three == 0 :return False
    if one + two > three : return True
    if one + three > two : return True
    if two + three > one : return  True
    return False

side_a = 0
side_b = 0
side_c = 0

print('POLE TRÓJKĄTA')

while not is_sum_of_one_and_two_more_than_three(side_a, side_b, side_c):
    try:
        side_a = float(input(f'długość bok a: '))
        if side_a <= 0:
            print('dopuszczalne tylko liczby większe od 0')
    except Exception:
        print('dopuszczalne tylko liczby większe od 0')