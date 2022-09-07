# message = 'Hello World'
# new_message = 'Hello'

# print(message)
# print(new_message)

'''
LEGB Rule: Local --> Enclosing --> Global --> Built-in

'''

# x = 'global x'

# def demo():
# 	x = 'local x'
# 	print(x)

# demo()
# print(x)

# import builtins

# # print(dir(builtins))

# print(help(max))

# list_1 = [56,12,9,92]

# # print(list_1)

# # def max():
# # 	pass

# print(max(list_1))

# LEGB

x = 'global x'

def outer():
	x= 'outer x'

	def inner():
		x = 'inner x'
		print(x)
	inner()
	print(x)


outer()
print(x)