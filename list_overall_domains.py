#!/usr/bin/python3

import os

if (os.getuid() != 0):
	print('Please be root or use sudo.\n')
	quit()

domains = os.listdir('/etc/valiases')

os.chdir('/etc/valiases')
for i in domains:
	print(i)

print('Done.')
