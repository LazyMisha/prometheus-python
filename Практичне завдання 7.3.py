'''
Розробити класс SuperStr, який наслідує функціональність стандартного типу str і містить 2 нових методи:

метод is_repeatance(s), який приймає 1 аргумент s та повертає True або False в залежності від того, чи може бути поточний рядок бути отриманий цілою кількістю повторів рядка s. Повернути False, якщо s не є рядком. Вважати, що порожній рядок не містить повторів.
метод is_palindrom(), який повертає True або False в залежності від того, чи є рядок паліндромом. Регістрами символів нехтувати. Порожній рядок вважати паліндромом.
Приклад послідовності дій для тестування класу:
s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 (рядок)
print int(s) # 123123123123 (ціле число)
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True
'''

class SuperStr(str):

    def __init__(self, string):
        self.string = string;
    
    def is_repeatance(self, s):
        self.s = s;
        if type(s) != str:
            return False;
        if len(self.string) == 0:
            return False;
        l = [];
        for i in self.string:
            if i not in l:
                l.append(i);
        l = ''.join(l);
        d = len(l);
        if l == self.s[-d]:
            return True;
        else:
            return False;
            
    def is_palindrom(self):
        self.string = self.string.lower().replace(' ', '');
        bar = '';
        num = 0;
        while num < len(self.string):
            bar += self.string[-num - 1];
            num += 1;
        if bar == self.string:
            return True;
        else:
            return False;
