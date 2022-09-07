# What --> lists - Data Structure
# why --> To  store and organise multplie items
# how --> ['item_1', 'item_2']

# # Mutable - Lists
# list_1 = ['item_1', 'item_2', 'item_3']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'item_a'

# print(list_1)
# print(list_2)


# Immutable - Tuples
# tuple_1 = ('item_1', 'item_2', 'item_3')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'item_a'

# print(tuple_1)
# print(tuple_2)


# Sets
# list_1 = ['item_1', 'item_2', 'item_3', 'item_1', 'item_1','item_3','item_3']
# sets = {'item_1', 'item_2', 'item_3', 'item_1', 'item_1','item_3','item_3'}

# print('item_1' in sets)

# # Empty_lists
# empty_list = []
# empty_list = list()

# # Empty_tuple
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty_sets
# empty_set = {}   #Don't use this method, it is used for creating dict
# empty_set = set()



# Dictionary -- Key:value pair
# word --> meaning

# emp_info_1 = ['John', 'M', 60000, ['Python', 'Java']]
# emp_info_2 = [60000, 'John', 'M', ['Python', 'Java']]

# emp_info = {'pay': 60000, 'first':'John', 'last':'M', 'prog_lang':['Python', 'Java']}

print(emp_info.keys())
print(emp_info.values())
print(emp_info.items())

for i, v in emp_info.items():
	print(f"{i} - {v}")

# for i in emp_info.items():
# 	print(i)

# print(emp_info['pay'])

# print(emp_info['first'])
# print(emp_info.get('email', 'Not Found!'))

# emp_info['pay'] = 65000
# emp_info['email'] = 'J@company.com'

# emp_info.update({"pay": 70000, 'email':'J@company.com'})
# del emp_info['pay']

# emp_info.pop('pay')

# print(emp_info)