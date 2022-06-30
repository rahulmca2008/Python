l = lambda x: x+4
print(l(2))
llc = lambda lst1: [x for x in lst1 if x%2==0]
print(llc([2,12,3,9,19,22]))
lsc = lambda set1: {x for x in set1 if x>0}
print(lsc({2,-2,0,-5,12}))
ldc = lambda dict1:{key:dict1[key] for key in dict1.keys() if len(key)==1}
print(ldc({'a':1,'b':2,'bd':12,'efg':3,'c':5}))
#### lambda with filter
lst1 = [-2,0,5,6,9,-1,2]
lf = list(filter(lambda x:x>2,lst1))
print(lf)
### lambda with map
lm = list(map(lambda x:x+4,lst1))
print(lm)
### lambda with reduce
from functools import reduce
lr = reduce(lambda a,b:a if a>b else b, lst1)
print("maximum",lr)