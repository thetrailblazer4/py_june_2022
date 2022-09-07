# create a function which return the index of the given item from the list.

# new_var = ['hello', 'Hi', 'Bye','Hey']
# find_index(new_var, 'Hi')



def find_index(arg_list, target):
	for index, value in enumerate(arg_list):
		if value == target:
			return index
	return 'Not Found!'


demo_var = 'A new var'


