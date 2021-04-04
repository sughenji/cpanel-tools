#!/usr/bin/python3

import os,sys,pwd

if len(sys.argv) != 2:
	print('\nUsage: ./find_account_from_domain.py DOMAIN\n')
	exit('Exiting...')

if (os.getuid() != 0):
	print('Please be root or use sudo.\n')
	exit()

os.chdir('/etc/valiases')

print('Domain ' + str(sys.argv[1]) + ' belongs to cPanel account: ' + str(pwd.getpwuid(os.stat(sys.argv[1]).st_uid).pw_name))
