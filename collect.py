"""
|=====================|
|==== COLLECTIONS ====|
|=====================|
"""

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
#OrderedDict is only for older versions since the dict today remembers the order 

# =========Counter===========
# sample = "aaabbbbccccccddd  "
# sample_counter = Counter(sample)
# print(sample_counter)
# print(sample_counter.most_common(1))

# =========namedtuple===========
# image_1 = namedtuple('image_1', 'x,y')
# pt1 = image_1(1,3)
# print(pt1)
# print(pt1.x)
# print(pt1.y)

# =========defaultdict===========
#will raise a key error if dli sakto ang gi sulod
#return empty/0 if not found
# d = defaultdict(float)
# d['a'] =2
# d['b'] =5
# print(d)
# print(d['c'])

# =========deque===========
# d = deque()
# d.append('second')
# d.append('third')
# d.appendleft('first')
# print(d)
# d.pop()
# d.popleft()
# print(d)
# d.extendleft(['zero', 'one', 'two', 'three'])
# print(d)
# d.rotate(2)
# print(d)
# d.rotate(-1)
# print(d)

