"""
|====================|
|==== DICTIONARY ====|
|====================|
"""

# =========Create dictionary===========
# sample = {'name' :'Din', 'age': 25}
# sample2 = dict(name='Din', age=25)
# print(sample)
# print(sample2)

#=========ITEMS, KEY, VALUES===========
# sample = dict(name='Din', age=25)
# print(sample.items())
# keys =sample.keys()
# print(keys)
# print(sample.values())
# for keys, values in sample.items(): print(keys, values)

#=========Delete, add, edit===========
# sample = dict(name='Din', age=25 )
# sample['name'] = 'Din Babia'
# sample['email'] = 'iamdin@facebook.com'
# del sample['age']
# print(sample)

#=========Pop, pop item===========
# sample = dict(name='Din', age=25, email='iamdin@facebook.com', address='tokyo' )
# sample.popitem() #python 3.7
# sample.pop('age')
# print(sample)

#=========UPDATE===========
sample = dict(name='Din', age=25 )
sample2 = dict(name='Din', age=25, email='iamdin@facebook.com' )
sample3 = dict(name='Din', age=25, email='iamdin@facebook.com', address='tokyo')
sample.update(sample2)
sample3.update(sample2)
print(sample)
print(sample3)