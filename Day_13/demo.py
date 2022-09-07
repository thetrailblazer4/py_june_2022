# def demo():
# 	print('Hello World')


# def new_demo():
# 	print('This is new_demo fn')


# def demo_2():
# 	print('This is demo_2')

# def demo_3():
# 	print('This is demo_3')	


# demo()
# new_demo()
# demo_2()
# demo_3()

'''
A programming language is said to have First-class functions 
when functions in that language are treated like any other variable. 

For example, in such a language, 
a function can be passed as an argument to other functions, 
can be returned by another function and 
can be assigned as a value to a variable

first-class functions if it treats functions as first-class citizens

This means the language supports passing functions as arguments to other functions, 
returning them as the values from other functions, and 
assigning them to variables or storing them in data structures.

a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.[1]

'''


# def square(x):
# 	return x * x

# result = square
# print(result(4))


# def outer():
# 	message = 'Hi'

# 	def inner_func():
# 		print(message)

# 	return inner_func

# new_var = outer()
# new_var()


def square(x):
	return x * x


def cube(x):
	return x * x * x



# lst_1 = [1,2,3,4]

# def our_func(func, arg_lst):
# 	result = []

# 	for i in arg_lst:
# 		result.append(func(i))

# 	return result

# print(our_func(square, lst_1))