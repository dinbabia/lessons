"""
|===============|
|==== LISTS ====|
|===============|
"""

#=========INSERT/APPEND================
# sample = [1,2,3,4,5]
# sample.insert(1, 9)
# sample.append(21)
# print(sample)

#=========POP==========================
# sample = [1,2,3,4,5]
# pop_item = sample.pop()
# print(pop_item)
# print(sample)

#=========REVERSE==========================
# sample2 = [1,2,3,4,5,6,7]
# sample2.reverse()
# print(sample2)

#=========SORT numbers/float======================
# sample3 = [5,2.2,2.1,7,75,25,54, -45]
# sample3.sort(reverse=True)
# print(sample3)

#=========SORT strings=======================
# asd = ['cute', 'cat','cry', 'crab' ]
# asd.sort()
# print(asd)

#=========Sorted===========
# sample3 = [5,2.2,2.1,7,75,25,54, -45]
# new_sample3 = sorted(sample3, reverse=True)
# print(new_sample3)

#=========Extend + COUNT===========
# sample = [1,2,3,4] 
# sample2 = [11,12,13]
# sample.extend(sample2)
# print(sample)
# sample3 = [21,22,23]
# sample4 = sample2 + sample3 + sample2
# print(sample4)
# print(sample4.count(11))

#=========LIST COMPRE + INDEX===========
# a = [2,3,4,5,6,7]
# b = [x**3 for x in a if x%2==0]
# c = [x**3 if x%2==0 else f"{x} is no even" for x in a]
# print(b)
# print(c)
# print(a.index(3))

#=========UNPACKING===========
# sample2 = [1,2,3,4,5,6,7]
# a,b,c,d,e , f ,g =sample2
# w,x,*y,z =sample2
# print(e)
# print(y)
