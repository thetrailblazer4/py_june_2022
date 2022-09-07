# def hello_fun():
# 	return 'Hello!'

# def demo_func():
# 	return 'Demo!'

# def new_func():
# 	return 'new_func'


# print(hello_fun())
# print(demo_func())
# print(new_func())



# def demo_add(a,b):
# 	num_1 = a
# 	num_2 = b

# 	result = num_1 + num_2

# 	return result


# var_a = demo_add(2,4)

# new_var = var_a + 2

# print(new_var)
# print(demo_add(2,3))


# def hello_fun(greeting, name='John'):
# 	return f'{greeting} {name} func ran!'


# print(hello_fun('Hello'))


def emp_info(*args, **kwargs):
	print(args)
	print(kwargs)

emp_info('Python', 'Java', name='John', email='J@company.com')
