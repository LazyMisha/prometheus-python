'''
Розробити функцію count_holes(n), 
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число, 
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами (вважати, що у "4" та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом.

пояснення щодо отворів в цифрах

Незначущими нулями на початку запису числа, якщо такі є, нехтувати.

Наприклад
Виклик функціїі: count_holes('123')
Повертає: 0
Виклик функціїі: count_holes(906)
Повертає: 3
Виклик функціїі: count_holes('001')
Повертає: 0
Виклик функціїі: count_holes(-8)
Повертає: 2
Виклик функціїі: count_holes(-8.0)
Повертає: ERROR
'''

def count_holes(n):
    
    if type(n) != int and type(n) != str and type(n) != long:
        return 'ERROR'
    else:
        try:
            num_dictitionary = {'0' : 1, '4' : 1, '6' : 1, '8' : 2, '9' : 1};
            counter = 0;
            n = int(n);
            n = str(n);
            for i in n:
                if i in num_dictitionary:
                    counter = counter + num_dictitionary.get(i);
            return counter;
        except ValueError:
            return 'ERROR'
        except TypeError:
            return 'ERROR'
