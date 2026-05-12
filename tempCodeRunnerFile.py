# Max
import functools
l=[19,34,554,65,765,43]
def max(a,b):
    if(a>b):
        return a
    else:
        return b
res = functools.reduce(max,l)
print(res)    