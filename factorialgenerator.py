from fastpickle import *
from math import factorial as fac


flist = fastload("factorials")
blist = fastload("binomiallist")
bkeys = blist.keys()
N = 150
#print(flist)
#print(blist)

def factorial(n):
    if n<len(flist):
        return flist[n]
    return fac(n)

def nchoosek(n,k):
    if (n,k) in bkeys:
        return blist[(n,k)]
    if (n,n-k) in bkeys:
        return blist[(n,n-k)]
    return flist[n]//(flist[k]*flist[n-k])
#print(nchoosek(2,2))


"""
list = [factorial(n) for n in range(N)]
fastdump("factorials",list)
flist = list

for n in range(N):
    if (n,n) in blist.keys():
        continue
    blist.update({(n,k): nchoosek(n,k) for k in range(n+1)})
    fastdump("binomiallist",blist)
    bkeys = blist.keys()
"""
