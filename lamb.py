"""
|================|
|==== LAMBDA ====|
|================|
"""

#var function
# add10 = lambda x : x + 10
# print(add10(5))

#multiple args
# mult = lambda x,y: x*y
# print(mult(2,5))

#applying it in sorted key args
# points2D = [(1,2), (15,1), (5,-1), (10,4)]
# points2D_sorted_x = sorted(points2D) #Sort in x point
# points2D_sorted_y = sorted(points2D, key=lambda x: x[1]) #Sort in y point
# points2D_sorted_sums = sorted(points2D, key=lambda x: x[0] + x[1]) #Sort by sums of the tuple

# print(points2D_sorted_x)
# print(points2D_sorted_y)
# print(points2D_sorted_sums)

#applying it in map args
# a = [1,2,3,4,5]
# b = map(lambda x : x*2, a) #list compre can also do this
# print(list(b))

#applying it in filter args
# a = [1,2,3,4,5]
# b = filter(lambda x : x%2 ==0, a) #list compre can also do this
# print(list(b))

#applying it in reduce args
from functools import reduce
a = [1,2,3,4,5]
b = reduce(lambda x,y : x*y, a) #list compre can also do this
print(b)