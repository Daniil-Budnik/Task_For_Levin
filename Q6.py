import re

# Конвертирование всех слов в нижний регистр
def UL(Word): return Word.upper().lower()

# Считываем текст, резервируем переменные
A, TEXT, S, List, Num, D = open("Text.txt",'r', encoding='utf-8'), "", [], [], [], []

# Весь текст в одну перменную
for Line in A: TEXT += Line

# Последовательность знаков . ! ?
for Symbol in TEXT: 
    if(Symbol == '.' or Symbol == '!' or Symbol == '?'): S.append(Symbol)

# Разделяем текст по знакам . ! ?
M = re.split('[.!?]',TEXT); M.pop()

# Получаем список из слов в предложении ?
for i in range(len(S)):
    if(S[i] == '?'): List += M[i].split()

# Сколько слов в списке
for x in range(len(List)):
    N = 1
    for y in range(x + 1, len(List)):
        if(UL(List[x]) == UL(List[y])): N += 1; D.append(y)
    Num.append(N)

# Удаляем повторяющиеся слова
for i in D[::-1]: List.pop(i); Num.pop(i)

# Вывод
for i in range(len(List)): print("Кол-во:",Num[i],'\tCлово:',List[i])