"""
|=================|
|==== STRINGS ====|
|=================|
"""
#upper(), lower()
#startswith(), endswith()
#find() -> return index 
#count() -> return count 
#replace() -> replace(to be replaced, replace to this)

#=========STRIP/SPLIT===========
sample = "    HELLO      Din       BABIA    "
sample2 = sample.strip()
sample3 = sample.split()
sample4 = "HELLO,Din,BABIA"
sample5 = sample4.split(',')
print(sample)
print(sample2)
print(sample3)
print(sample5)
sentence = []
for word in sample3:
    print(word, end = ' ')