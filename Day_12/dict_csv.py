import csv

with open('C:/Users/zeus/Desktop/Py_Jul/Day_11/emp_info.csv', 'r') as csv_file:
	
	csv_reader = csv.DictReader(csv_file)

	with open('modified_csv', 'w') as new_file:
		fieldnames = ['emp_id','first_name', 'last_name']
		csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
		csv_writer.writeheader()
		for i in csv_reader:
			del i['email']
			csv_writer.writerow(i)
