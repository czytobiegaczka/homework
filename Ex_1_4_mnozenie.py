'''
Zadanie 1.4 Zgadywanka 1 (mnożenie)
Napisz program sprawdzający znajomość tabliczki mnożenia.
Program losuje dwie liczby z zakresu od 1 do 10. Podaje te dwie liczby i pyta jaki jest ich
iloczyn (nie podaje wyniku). Użytkownik ma podać wynik. Program pyta o wynik wielokrotnie,
tak długo, aż użytkownik poda prawidłowy wynik. Na końcu program informuje, w której próbie
udało się znaleźć wynik. Napisz program tak, aby łatwo („w jednym miejscu”) można było
zmienić zakres losowanych liczb na inny.
'''
from random import randint

zakres = 10
number_1 = randint(1, zakres)
number_2 = randint(1, zakres)
result = 0
quantity = 0

print('LEKCJA MNOŻENIA')
print('```````````````')

while result != number_1 * number_2:
    try:
        quantity += 1
        result = int(input(f'{number_1} * {number_2} = '))
    except Exception:
        print('możliwe tylko liczby całkowite')

print(f'BRAWO! - prawidłowy wynik w : {quantity} próbie')
