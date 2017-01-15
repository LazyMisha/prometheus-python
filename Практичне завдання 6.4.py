'''
Розробити функцію find_most_frequent(text), 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']
'''

from collections import Counter;
def find_most_frequent(text):
    
    newWords = [];
    text = text.lower();
    text = text.replace(',', ' ');
    text = text.replace('...', '');
    text = text.replace('!', '');
    text = text.replace('-', ' ');
    text = text.replace('?', '');
    text = text.replace(':', '');
    text = text.replace(';', '');
    text = text.replace('.', '');
    text = text.replace('  ', ' ');
    text = text.replace('   ', ' ');
    text = text.replace('    ', ' ');
    text = text.split(' ');
    
    if " " in text:
            text.remove(" ");
    
    count = Counter(text);
    
    maximum = max(count.values());
    
    for k, v in count.items():
        if v == maximum:
            newWords.append(k);
    
    if '' in newWords:
        delit = list(newWords.pop());
        return delit;
    else:
        return newWords;
