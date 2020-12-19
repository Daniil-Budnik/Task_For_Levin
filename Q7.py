def UL(Word): return Word.upper().lower()

FILE, TEXT, WORD = open("Text.txt",'r', encoding='utf-8'), "", []

for Line in FILE: TEXT += Line

LIST = TEXT.split()

N1 = 1
for i in range(1, len(LIST)):
    if(UL(LIST[0]) == UL(LIST[i])): N1 += 1

for x in range(1, len(LIST)):
    N = 1
    for y in range(x + 1, len(LIST)):
        if(UL(LIST[x]) == UL(LIST[y])): N += 1
    if(N == N1): WORD.append(LIST[x])

print("Первое слово встретилось:", N1, "раза.\n")
for i in WORD: print(i)