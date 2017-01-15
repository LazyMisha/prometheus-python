'''
Розробити класс Sphere для представлення сфери у тривимірному просторі.

Забезпечити наступні методи класу:

конструктор, який приймає 4 дійсних числа: радіус, та 3 координати центру кулі. Якщо конструктор викликається без аргументів, створити об'єкт сфери із одиничним радіусом та центром у початку координат. Якщо конструктор викликається з 1 аргументом, створити об'єкт сфери з відповідним радіусом та центром у початку координат.
метод get_volume(), який повертає дійсне число -- об'єм кулі, обмеженої поточною сферою.
метод get_square(), який повертає дійсне число -- площу зовнішньої поверхні сфери.
метод get_radius(), який повертає дійсне число -- радіус сфери.
метод get_center(), який повертає тьюпл із 3 дійсними числами -- координатами центра сфери в тому ж порядку, в яком вони задаються в конструкторі.
метод set_radius(r), який приймає 1 аргумент -- дійсне число, та змінює радіус поточної сфери, нічого не повертаючи.
метод set_center(x,y,z), який приймає 3 аргументи -- дійсних числа, та змінює координати центра сфери, нічого не повертаючи. Координати задаються в тому ж порядку, що і в конструкторі.
метод is_point_inside(x,y,z), який приймає 3 аргументи -- дійсних числа -- координати деякої точки в просторі (в тому ж порядку, що і в конструкторі), та повертає логічне значення True або False в залежності від того, чи знаходиться ця точка всередині сфери.
Тести із некорестними даними не проводяться.

Приклад послідовності дій для тестування класу:
s0 = Sphere(0.5) # test sphere creation with radius and default center
print s0.get_center() # (0.0, 0.0, 0.0)
print s0.get_volume() # 0.523598775598
print s0.is_point_inside(0, -1.5, 0) # False
s0.set_radius(1.6) 
print s0.is_point_inside(0, -1.5, 0) # True
print s0.get_radius() # 1.6
'''

import math
class Sphere(object):
    
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
		self.radius = radius; self.x = x; self.y = y; self.z = z;
    
    def get_volume(self):
        return (4.0 / 3.0) * (math.pi * (self.radius**3));
        
    def get_square(self):
        return 4.0 * (math.pi * (self.radius * self.radius));
        
    def get_radius(self):
        return self.radius;
        
    def get_center(self):
        return float(self.x), float(self.y), float(self.z);
            
    def set_radius(self, r):
        self.radius = r;
        
    def set_center(self, x1, y1, z1):
            self.x = x1; 
            self.y = y1; 
            self.z = z1;
        
    def is_point_inside(self, x, y, z):
         if math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2) <= self.radius**2:
             return True;
         else:
             return False;
