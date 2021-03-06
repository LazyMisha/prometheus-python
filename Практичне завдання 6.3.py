'''
Розробити функцію saddle_point(matrix), 
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків, 
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).

Наприклад
1 2 3
3 2 1
Виклик функції: saddle_point([[1,2,3],[3,2,1]])
Повертає: False
8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
Виклик функції: saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
Повертає: (1, 2)
21
Виклик функції: saddle_point([[21]])
Повертає: (0, 0)
'''

def saddle_point(matrix):

    count,last = 0,0;
    for i in matrix:
        if i.count(min(i)) == 1:
            m = i.index(min(i));
            col = [];
            for j in matrix:
                col.append(j[m]);
            if col.count(max(col)) == 1 and min(i) == max(col):
                result = (int(m), int(col.index(max(col))));
                count += 1;
        if count > last:
            last = count;
            return result;
    if count == 0:
        return False;
