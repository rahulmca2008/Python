from itertools import product, permutations, combinations, combinations_with_replacement
#product - cartesian product

print("cartesian product")

for it in product("ABCD", repeat=2):
    print(it)

print("combinations")

print(list(combinations('ABCD',2)))

print("Combinations with replacement")

print(list(combinations_with_replacement('ABCD',2)))

print("permutations")

print(list(permutations('ABCD',2)))





