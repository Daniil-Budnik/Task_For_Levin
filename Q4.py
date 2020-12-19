import numpy as np

A = np.loadtxt("NumTabMatrix.txt")
M = []

for Line in A:
    for Num in Line:
        S = str(int(Num))
        if(len(S) == 3):
            for Z in S:
                Triger = True
                for El in M: 
                    if(El == Z): Triger = False
                if(Triger): M.append(Z) 

M = sorted(M)
print(M)