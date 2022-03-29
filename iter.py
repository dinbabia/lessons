"""
|=====================|
|==== COLLECTIONS ====|
|=====================|
"""

from itertools import product, permutations, combinations, combinations_with_replacement,accumulate, groupby, count,cycle,repeat
#infinite operators ( count,cycle,repeat)

# =========product===========
# combine, murag foil method
# a =[1,2,3]
# b = [4,5,6]
# prod = product(a,b)
# print(list(prod))

# =========permutations===========
# a = [1,2,3]
# b = permutations(a)
# c = list(b)
# print(c)
# print(len(c))

# =========combinations===========
# a = [1,2,3,4]
# b = combinations(a,2)
# c = list(b)
# print(c)
# d = combinations_with_replacement(a,2)
# print(list(d))

# =========accumulate===========
#1, 1+2, 1+2+3, 1+2+3+4
# a = [1,2,3,4]
# b = accumulate(a)
# print(list(b))
# #can use func=operator to dictate/ change accumulate strategy
# #1, 1*2, 1*2*3, 1*2*3*4
# import operator
# c = accumulate(a, func=operator.mul)
# print(list(c))
# d = [1,2,6,3,2,5]
# e = accumulate(d, func=max)
# print(list(e))

# =========groupby===========

#(1) basic sample
# def smaller_than_3(x):
#     return x < 3
# a = [5,6,1,2,3,4]
# b = groupby(a, key=smaller_than_3)
# #USING lambda.....key = lambda x: x < 3
# for key, value in b:
#     print(key, list(value))
    
#(2) upgrade sample
# people = [
#     {'name' : 'Din',
#     'age' :25},
#     {'name' : 'dad',
#     'age' :60},
#     {'name' : 'mom',
#     'age' :62},
#     ]
# people_grp = groupby(people, key= lambda x: 'senior' if x['age'] > 55 else 'young')
# for key, value in people_grp:
#     print(key, list(value))
    
    
# =========count,cycle,repeat===========
#INFINITE LOOPS

#COUNT
# for i in count(10, 2):
#     print(i)
#     if i == 50:
#         break

#COUNTER
# a = [1,2,3]
# counter = 0
# for i in cycle(a):
#     print(i)
#     if i == 3:
#         counter += 1
#         if counter == 4:
#             break
#         else:
#             print('again')

#REPEAT
# for i in repeat('hi', 4):
#     print(i)
