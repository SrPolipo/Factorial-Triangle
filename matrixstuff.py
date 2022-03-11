import numpy as np

def delta(i,j,n):
    if i == j:
        return 1
    if i%n == j%n:
        return -1
    return 0

def operator(n):
    return np.matrix([[delta(i,j,n) for i in range(n+1)] for j in range(n+1)])

def vector(n):
    return np.transpose(np.matrix([(n+1-i)**n for i in range(n+1)]))

print(operator(3))
"""
for n in range(1,10):

    """
"""
x = operator(10)
for n in range(1,11):
    print(x**n)

print(x**10*vector(10))
"""
