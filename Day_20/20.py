# class Employee():

# 	raise_amt = 1.07

# 	def __init__(self, first, last, pay):
# 		self.first = first
# 		self.last = last
# 		self.email = f'{first}.{last}@company.com'
# 		self.pay = pay

# 	def fullname(self):
# 		return f'{self.first} {self.last}'

# 	def apply_raise(self):
# 		self.pay = int(self.pay * self.raise_amt)

# 	def __repr__(self):
# 		return f"Employee('{self.first}', '{self.last}', {self.pay})"

# 	def __str__(self):
# 		return f"{self.fullname()}, {self.pay}"
	
# emp_1 = Employee('John', 'K', 50000)

# print(repr(emp_1))
# print(emp_1)




class Employee():

	raise_amt = 1.07

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		# self.email = f'{first}.{last}@company.com'
		self.pay = pay

	@property
	def email(self):
		 return f'{self.first}.{self.last}@company.com'

	@property
	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('John', 'K', 50000)

emp_1.first = 'Jane'

print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)