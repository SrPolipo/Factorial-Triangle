from fastpickle import *
from math import factorial




def nchoosek(n,k):
    return flist[n]//(flist[k]*flist[n-k])
#print(nchoosek(2,2))



flist = fastload("factorials")

print(flist)

blist = fastload("binomiallist")

print(blist)


"""
#list = [factorial(n) for n in range(34)]

#fastdump("factorials",list)
final = {}
for n in range(34):
    final.update({(n,k): nchoosek(n,k) for k in range(n+1)})

fastdump("binomiallist",final)
"""
