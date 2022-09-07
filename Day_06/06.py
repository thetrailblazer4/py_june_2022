# Reusable - Whenever it is required we can use it 

# DRY --> Don't Repeat yoursel

import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(0)

def sqaure(length):
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(90)

for i in range(200):
	sqaure(150)
	my_turtle.right(11)


# print(list(range(10)))

# for i in range(10):
# 	print('Hello')






turtle.done()


# import builtins

# print(dir(builtins))