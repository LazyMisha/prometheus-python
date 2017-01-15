'''
Розробити функцію create_calendar_page(month,year), 
яка приймає 2 аргументи -- цілі числа -- місяць (нумерація починається з 1) і рік, 
та повертає оператором return 1 рядок, який містить сторінку календаря на цей місяць.

Якщо місяць та рік не задані, використати сьогоднішні значення.

"Сторінка", що повертається, має наступний формат:
приклад результату
Це значення є одним рядком із переносами рядка \n, пробіли після числа 28 відсутні. Зайві пробіли в кінці під-рядків або всього рядка, як і зайві порожні рядки недопустимі.

Тести із некорестними даними не проводяться.

Приклад викликів для тестування функції:
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)
'''

import calendar;

def create_calendar_page(month,year):
    
    page = '';
    days = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n';
    weekdays = calendar.Calendar();
    for i in weekdays.monthdayscalendar(year, month):
        for q in i:
            q = str(q);
            if q == 0:
                q = q.replace('0', ' ');
            if len(q) == 1:
                q = '0' + q;
            page += q + ' ';
        page = page + '\n';
    
    page = page.replace(' \n', '\n');
    page = page.replace('00', '  ');
    
    return days + page;
    
