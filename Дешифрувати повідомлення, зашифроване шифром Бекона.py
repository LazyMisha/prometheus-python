'''
Для кодування повідомлень Френсіс Бекон запропонував кожну літеру тексту замінювати на групу з п'яти символів «А» або «B» (назвемо їх "ab-групами"). Для співставлення літер і кодуючих ab-груп в даному завданні використовується ключ-ланцюжок aaaaabbbbbabbbaabbababbaaababaab, в якому порядковий номер літери відповідає порядковому номеру початку ab-групи.

Наприклад: літера "а" - перша літера алфавіту; для визначення її коду беремо 5 символів з ключа, починаючи з першого: aaaaa. Літера "c" - третя в алфавіті, отже для визначення її коду беремо 5 символів з ключа, починаючи з третього: aaabb.

Таким чином, оригінальне повідомлення перетворюється на послідовність ab-груп і може далі бути накладене на будь-який текст відповідної довжини: А позначається нижнім регістром, В - верхнім.

Наприклад, початкове повідомлення - Prometheus.

1. Кодуємо його через ab-послідовності:
p = abbab
r = babab
o = aabba
m = bbaab
e = abbbb
t = babba
h = bbbab
e = abbbb
u = abbaa
s = ababb
Результат: abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb

2. Підбираємо текст приблизно такої ж довжини, в якому сховаємо наше повідомлення: Welcome to the Hotel California Such a lovely place Such a lovely place

3. Для зручності розбиваємо його на групи по 5 символів і відкидаємо зайву частину (щоб при декодуванні не отримувалися зайві п'ятірки). Співставимо ab-рядок і текст-сховище для порівняння:
abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb
Welco metot heHot elCal iforn iaSuc halov elypl aceSu chalo vely

4. Змінюємо регістр символів, кодуючи A та B:
abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb
wELcO MeToT heHOt ELcaL iFORN IaSUc HALoV eLYPL aCEsu cHaLO vely

5. Повертаємо початкові пробіли на місце:
wELcOMe To The HOtEL caLiFORNIa SUcH A LoVeLY PLaCE sucH a LOvely

Для дешифрування повідомлення необхідно виконати зворотні дії.

Вхідні дані: рядок, передається в програму як аргумент командного рядка. Може містити пробіли та літери латинського алфавіту в будь-якому регістрі. Для передачі в якості одного аргументу рядок береться в подвійні лапки.

Результат роботи: рядок - дешифроване повідомлення.

Наприклад

Вхідні дані: I canT DAnCE i CANt TAlK Hey
видаляємо пробіли, розбиваємо на групи по 5 символів: IcanT DAnCE iCANt TAlKH ey
ey відкдається
символи нижнього регістру перетворюються в a, верхнього - в b: baaab bbabb abbba bbabb
декодуємо, використовуючи ключ:
baaab = w
bbabb = i
abbba = k
bbabb = i
Результат: wiki
Вхідні дані: Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat
видаляємо пробіли, розбиваємо на групи по 5 символів: HotsU nBEAT IngdO WNbUR NINgm YFEet JuStW alKIn garOU nDHOt suNmA kiNGm eSWea t
t відкдається
символи нижнього регістру перетворюються в a, верхнього - в b: baaab abbbb baaab bbabb bbbaa bbbaa babab aabba aaabb abbba aabab aabba abbaa
декодуємо, використовуючи ключ:
baaab = w
abbbb = e
baaab = w
bbabb = i
bbbaa = l
bbbaa = l
babab = r
aabba = o
aaabb = c
abbba = k
aabab = y
aabba = o
abbaa = u
Результат: wewillrockyou
'''

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

import sys

dic = {"aaaaa":'a', "aaaab":'b', "aaabb":'c', 
    "aabbb":'d', "abbbb":'e', "bbbbb":'f', 
    "bbbba":'g', "bbbab":'h', "bbabb":'i', 
    "babbb":'j', "abbba":'k', "bbbaa":'l', 
    "bbaab":'m', "baabb":'n', "aabba":'o', 
    "abbab":'p', "bbaba":'q', "babab":'r', 
    "ababb":'s', "babba":'t', "abbaa":'u', 
    "bbaaa":'v', "baaab":'w', "aaaba":'x', 
    "aabab":'y', "ababa":'z'}

x = sys.argv[1]

x = x.replace(' ', '')

y = ''

z = 0

l = []

for i in x:
    if i.islower() == True:
        x = x.replace(i, "a")
    elif i.isupper() == True:
        x = x.replace(i, "b")

while z < len(x):
    l.append(x[z:z+5])
    z += 5
    for i in l:
        if len(i) < 5:
            del l[l.index(i)]

for a in l:
    for i in dic.keys():
        if i == a:
            y = y + dic.get(i)
print y
