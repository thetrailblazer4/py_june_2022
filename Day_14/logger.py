
def logger(func):
	import logging
	logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
	
	def log_func(*args, **kwargs):
		logging.info(f"Running '{func.__name__}' with args:{args} & kwargs: {kwargs} ")
		print(func(*args, **kwargs))
	return log_func

@logger
def add(a,b):
	return a + b

@logger
def sub(a,b):
	return a - b 

def multiply(a,b):
	return a * b  


sub(4,2)
