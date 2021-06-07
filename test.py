from bigO import BigO
from random import randint

def quickSort(n):  # in-place | not-stable
    k=1
    i=1
    while(k<=n):
        i=i+1
        k=k+i


lib = BigO()
complexity = lib.test(quickSort, "random")
complexity = lib.test(quickSort, "sorted")
complexity = lib.test(quickSort, "reversed")
complexity = lib.test(quickSort, "partial")
complexity = lib.test(quickSort, "Ksorted")