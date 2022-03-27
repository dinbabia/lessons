"""
|==============|
|==== SETS ====|
|==============|
"""
#No duplicate elements
#Unordered
#mutable
#iterable

# =========No duplicate elements===========
# sample = {1,2,3,1,2,3,4,5,4,5}
# print(sample)
# sample2 = {"samples"}
# print(sample2)   

# =========Unordered===========
# sample = set("hello")
# sample.add('hi')
# sample.remove('h')
# sample.discard('babia') #do nothing
# print(sample)

# =========Union/Intersection===========
# odds = {1,3,5,7,9}
# even = {0,2,4,6,8}
# primes = {2,3,5,7}
# u = odds.union(even)
# print(u)
# i = odds.intersection(primes)
# print(i)

# =========Difference===========
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,13}
# diffA = setA.difference(setB)
# diffB = setB.difference(setA)
# diffC = setA.symmetric_difference(setB)
# print(diffA)
# print(diffB)
# print(diffC)

# =========Update===========
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,13}
# setA.update(setB)
# print(setA)
# =========Intersection Update===========
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,13}
# setA.intersection_update(setB) #intersection first then update setA
# print(setA)
# =========Differ Update===========
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,13}
# setA.difference_update(setB)   #difference first then update setA
# print(setA)
# =========Symmtericc Differ Update===========
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12,13}
# setA.symmetric_difference_update(setB) #symmetric difference first then update setA
# print(setA)

"""
|====================|
|==== SETS v.2.0 ====|
|====================|
"""
# =========is subset===========
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# print(setA.issubset(setB))
# print(setB.issubset(setA))

# =========is superset===========
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# print(setA.issuperset(setB))
# print(setB.issuperset(setA))

# =========is disjoint===========
# setA = {1,2,3,4,5,6}
# setB = {1,2,3}
# setC = {7,8,9}
# print(setA.isdisjoint(setB)) #FALSE if they HAVE SAME ELEMENTS
# print(setB.isdisjoint(setA))
# print(setC.isdisjoint(setA))

# =========frozen set===========
# setA = frozenset([2,3,4]) #cannot be changed
# print(setA)
