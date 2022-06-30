from itertools import accumulate,chain,compress,filterfalse,groupby,islice,starmap,zip_longest

print("Accumulate")
for it in accumulate([2,4,3,2,1]):
    print(it)

print("chain")
for it in chain(['ABC'],['DEF']):
    print(it)

print("chain from iterable")
for it in chain.from_iterable(['ABC','DEF']):
    print(it)

print("compress")
for it in compress([1,2,3,4],[0,1,0,1]):
    print(it)

print("FilterFalse")
for it in filterfalse(lambda x:x%2,range(10)):
    print(it)

print("isslice")

for it in islice([2,3,6,9,12,13,16,17],1,6,2):
    print(it)

print("starmap")

for it in starmap(pow,[(2,3),(3,3),(4,2)]):
    print(it)

print("map")

print(list(map(lambda x: x+2,[1,2,3,4])))

print('zip_longest')

print(list(zip_longest('ABCD','xy',fillvalue='_')))




