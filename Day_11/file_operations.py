# f = open('new_file.txt', 'r')

# # print(f.read())

# for i in f:
# 	print(i, end='')



# f.close()



# with open('new_file.txt', 'r') as rf:
# 	for i in rf:
# 		print(i, end='')

# with open('my_file.txt', 'w') as f:
# 	f.write('Hello')
# 	f.seek(0)
# 	f.write('Hey')

# with open('new_file.txt', 'r') as rf:
# 	with open('copy_new_file.txt', 'w') as wf:
# 		for line in rf:
# 			wf.write(line)



# with open('demo.jpg', 'rb') as rf:
# 	with open('copy_demo.jpg', 'wb') as wf:
# 		for line in rf:
# 			wf.write(line)


''' Read/write csv file'''

import csv

# with open('emp_info.csv', 'r') as csv_file:
	
# 	csv_reader = csv.reader(csv_file)
	
# 	for i in csv_reader:
# 		print(i[3])


# with open('emp_info.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)
	
# 	with open('copy_emp.csv', 'w') as new_file:
# 		csv_writer = csv.writer(new_file, delimiter='\t')
		
# 		for line in csv_reader:
# 			csv_writer.writerow(line)


with open('copy_emp.csv', 'r') as csv_file:
	
	csv_reader = csv.reader(csv_file, delimiter = '\t')
	
	for i in csv_reader:
		print(i[3])
		