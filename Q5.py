def FindSymbol(Line):
    M = []
    for n in Line: 
        N = ord(n)
        if((N > 32 and N < 48) or (N > 57 and N < 65) or (N > 90 and N < 97) or (N > 122 and N < 128)):
            M.append(n)
    return M

A, TEXT = open("Text.txt",'r', encoding='utf-8'), ""
for Line in A: print(FindSymbol(Line))
