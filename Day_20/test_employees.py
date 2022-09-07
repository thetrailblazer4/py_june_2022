import unittest
from employees import Employee

class TestEmployee(unittest.TestCase):


	@classmethod
	def setUpClass(cls):
		print('setUpClass')


	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')



	def setUp(self):
		self.emp_1 = Employee('John', 'K', 50000)
		self.emp_2 = Employee('Jane', 'M', 60000)
		print('setUp\n')

	def tearDown(self):
		print('tearDown\n')

	def test_email(self):

		self.assertEqual(self.emp_1.email, 'John.K@company.com')
		self.assertEqual(self.emp_2.email, 'Jane.M@company.com')

		self.emp_1.first = 'Tom'
		self.emp_2.first = 'Kate'

		self.assertEqual(self.emp_1.email, 'Tom.K@company.com')
		self.assertEqual(self.emp_2.email, 'Kate.M@company.com')

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John K')
		self.assertEqual(self.emp_2.fullname, 'Jane M')

		self.emp_1.first = 'Tom'
		self.emp_2.first = 'Kate'

		self.assertEqual(self.emp_1.fullname, 'Tom K')
		self.assertEqual(self.emp_2.fullname, 'Kate M')

	def test_apply_raise(self):

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 53500)
		self.assertEqual(self.emp_2.pay, 64200)





if __name__ == '__main__':
	unittest.main()