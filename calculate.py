from fastpickle import *


binomials = fastload("binomiallist")

def sgn(n):
    if n%2 == 0:
        return 1
    return -1



factorial = lambda n: sum(  [binomials[(n,k)]*sgn(k)*(n+1-k)**n for k in range(n+1)]    )

print(binomials)
print(factorial(33))
