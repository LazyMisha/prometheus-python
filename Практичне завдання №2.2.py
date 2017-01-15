'''
Вхідні дані: 3 числа x, y та z. x, y -- невід'ємні цілі числа, z дорівнює 0 або 1. x не дорівнює 0. Передаються як аргументи командного рядка.

Вихідні дані: рядок "Everybody sing a song: <текст пісеньки>.", де <текст пісеньки> формується з у куплетів, розділених пробілами. Всі куплети однакові і складаються з x 'la' через дефіс. Якщо z дорівнює одиниці, в кінці ставиться окличний знак, інакше крапка. За відсутності куплетів пробіл перед крапкою/окличним знаком не ставиться.

Підказка: для цього можна застосувати множення рядків.

Приклад
Вхідні дані: 2 3 1
Приклад виклику: python lab2_2.py 2 3 1
Результат: Everybody sing a song: la-la la-la la-la!
Вхідні дані: 1 0 0
Приклад виклику: python lab2_2.py 1 0 0
Результат: Everybody sing a song:.
'''

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

w = 'la-'

text = ' ' + w * (x - 1) + 'la'

kuplet = y * text

if z == 1:
        kon = '!'
else:
        kon = '.'

q = 'Everybody sing a song:' + kuplet + kon
        
print q
