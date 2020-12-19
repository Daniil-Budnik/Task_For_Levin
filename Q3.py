import numpy as np

def qSort(arr):
    if len(arr) <= 1: return arr
    else: return qSort([x for x in arr[1:] if abs(x) < abs(arr[0])]) + \
               [arr[0]] + \
               qSort([x for x in arr[1:] if abs(x) >= abs(arr[0])])
    

A = np.loadtxt("NumLine.txt")
B = sorted(A,key=abs)
C = qSort(A)
print("Метод sorted:\n",B,"\nМетод qSort:\n",C)