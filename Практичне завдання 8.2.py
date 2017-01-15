'''
Розробити функцію find_fraction(summ), 
яка приймає 1 аргумент -- невід'ємне ціле число summ, 
та повертає тьюпл, що містить 2 цілих числа -- чисельник та знаменник найбільшого правильного нескорочуваного дробу, для якого сума чисельника та знаменника дорівнює summ. Повернути False, якщо утворити такий дріб неможливо.

Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
'''

def find_fraction(summ):
    pivsumm = summ / 2;
    chis = 0;
    znam = 0;
    if summ <= 2:
        return False;
    if summ % 2 == 0:
        if pivsumm % 2 == 0:
            return (pivsumm - 1), (pivsumm + 1);
        else:
            return (pivsumm - 2), (pivsumm + 2);
    elif summ % 2 != 0:
        chis = (summ - 1) / 2;
        znam = summ - chis;
        return chis, znam;
