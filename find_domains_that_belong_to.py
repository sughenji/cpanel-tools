#!/usr/bin/python3

import os,sys,pwd

if len(sys.argv) != 2:
	print('\nUsage: ./find_domains_that_belong_to.py USER\n')
	exit('Exiting...')

if (os.getuid() != 0):
	print('Please be root or use sudo.\n')
	exit()

os.chdir('/etc/valiases')

for files in os.listdir('/etc/valiases'):
	if pwd.getpwuid(os.stat(files).st_uid).pw_name == sys.argv[1]:
		print(files)
