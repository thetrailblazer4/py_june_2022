# Automate Parsing & Rename multiple files


import os

# print(os.getcwd())

os.chdir('C:/Users/zeus/Desktop/Py_Jul/My_files')

# print(os.getcwd())

# print(os.listdir())
file_names = os.listdir()

for i in file_names:
	f_names, f_extn = os.path.splitext(i)
	f_topic, f_course, f_num = f_names.split('-')

	f_topic = f_topic.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2)
	
	new_name = f"{f_num}-{f_topic}{f_extn}"

	os.rename(i, new_name)