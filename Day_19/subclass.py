class Emp():

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

class Developer(Emp):
	raise_amt = 1.09

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Emp):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)

		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print(emp.fullname())

	

emp_1 = Emp('John', 'K', 50000)
emp_2 = Developer('Jane', 'M', 60000, 'Python')
mgr = Manager('John', 'K', 50000)

# mgr.add_emp(emp_1)
# mgr.add_emp(emp_2)
# # mgr.remove_emp(emp_2)

# mgr.print_emps()

# emp_1.raise_amt = 1.09

# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# print(help(Developer))

print(isinstance(mgr, Developer))
print(issubclass(Manager, Emp))