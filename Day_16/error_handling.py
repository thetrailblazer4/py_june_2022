'''
FileNotFoundError: [Errno 2] No such file or directory: 'dem.log'
NameError: name 'old_var' is not defined

try:
	pass
except Exception:
	pass
else:
	pass
finally:
	pass


'''


try:
	f = open('demo.log')
	# if f.name == 'demo.log':
	# 	raise Exception

except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()

finally:
	print('----<executing>-------')
