# Methods --> Regular, Class Methods, Static Methods

import datetime

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

	@classmethod
	def update_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday ==5 or day.weekday() == 6:
			return False
		return True


emp_str_1 = 'John-K-50000'


new_emp_1 = Employee.from_str(emp_str_1)

my_date = datetime.date(2022,8,28)

print(Employee.is_workday(my_date))

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)



# print(new_emp_1.first)

# new_emp_1 = Employee()

# import datetime

print(datetime.__file__)