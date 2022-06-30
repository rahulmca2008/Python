# count(start,[step]) , [] in arguments -> optional
# cycle(p) => p0,p1,..,plast,p0,p1....
# repeat(elem,[n]) -> repeat elem endlessly or till n times.

from itertools import count, cycle, repeat
"""
iterator = count(10,2)
for it in iterator:
    if it==40:
        break
    print(it)
"""
def count_iter(start:int,step:int,end:int):
    for it in count(start,step):
        if it==end:
            break
        print(it)
count_iter(10,2,40)

print("\ncycle")
j=0
for it in cycle('ABCD'):
    if j>10:
        break
    print(it)
    j+=1

for it in repeat('ABCD',3):
    print(it)



