my_dict = {'masha' : 2023, 'lesha' : 2017, "pasha" : 2004}
print(my_dict)
print(my_dict['masha'])
print(my_dict.get ('Igor'))
my_dict.update({'pavel' : 2012, 'vika' : 2020})
print(my_dict)
Al = my_dict.pop('masha')
print(Al)
print(my_dict)


my_set = {1, 'Яблоко', 42.314}
print(my_set)
my_set.update([(5,6,7), 2020])
print(my_set)
