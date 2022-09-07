# Class & Instances, Class variables


class Employee():

	raise_amt = 1.07

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
	

emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Jane', 'M', 60000)

emp_1.raise_amt = 1.09

print(emp_1.raise_amt)
print(emp_2.raise_amt)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.raise_amt)

# print(emp_1.first)
# print(emp_1.last)
# print(f'{emp_1.first} {emp_1.last}')
# print(f'{emp_2.first} {emp_2.last}')

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# emp_2 = Employee('Jane', 'M', 50000)

# emp_1.first = 'John'
# emp_1.last = 'K'
# emp_1.email = 'John.K@company.com'
# emp_1.pay = 50000


# emp_2.first = 'Jane'
# emp_2.last = 'M'
# emp_2.email = 'Jane.M@company.com'
# emp_2.pay = 60000