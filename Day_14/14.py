# def outer(msg):
# 	def inner_func():
# 		print(msg)

# 	return inner_func

# my_func = outer('Hello')
# my_func()


def dec_func(func):
	def wrapper_func(*args, **kwargs):
		print('Hello World!')
		return func(*args, **kwargs)
	return wrapper_func

@dec_func
def display():
	print('The display func was executed!')

@dec_func
def emp_info(name, age):
	print(f"emp_info ran with args: {name}, {age}")

def demo_display():
	print('The demo_display func was executed!')

# display()
emp_info('John', 28)
# display()
# dec_disp = dec_func(emp_info)
# dec_disp()