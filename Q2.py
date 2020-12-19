import numpy as np

A = np.transpose(np.loadtxt("NumTab.txt"))

print(np.transpose(A),'\n')

N = 0

for I in range(len(A)):
    if(N == 0): N += 1; A[I] = sorted(A[I])
    elif(N == 1): N += 1; A[I] = sorted(A[I])[::-1]
    else: N = 0

print(np.transpose(A))