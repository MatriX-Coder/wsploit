#!/usr/bin/python
# Wsploit Project

'''
this is very
simple script 
that tries to
login anonymously
to ftp
'''


try:
	import ftplib
except:
	print 'You need ftplib library installed.'

def init():
	path = raw_input('\nEnter List Path : ')
	file = open(path,'r')
	ips = file.readlines()
	for ip in ips:
		ip = ip.strip()
		try:
			s = ftplib.FTP( ip, 'anonymous', 'anonymous@wsploit').login()
			if s == '230 Anonymous user logged in.':
				print ip+' ---> Successfully Loged In !'
		except ftplib.all_errors:
			print ip
