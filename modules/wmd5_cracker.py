#!/usr/bin/python
# Wsploit Project

'''
this is MD5 cracker 
module using 
md5.darkbyte.ru api 
'''

try:
	import httplib
except:
	print 'You need httplib library installed.'

import wcolors
def init():
	try:
		line_3 = "\nEnter MD5 Hash : "
		hash_md5 = raw_input(line_3)
	
		conn = httplib.HTTPConnection('md5.darkbyte.ru')
		conn.request("GET", '/api.php?q=%s' % hash_md5)
		r1 = conn.getresponse()
		rep = r1.read()
		if rep == '':
			print wcolors.color.RED + "\n    [-]Hash (%s) not cracked :(" % hash_md5 + wcolors.color.ENDC
		else:
			print wcolors.color.BLUE + "\n    [*]Hash Cracked : %s" % rep + wcolors.color.ENDC
	except(KeyboardInterrupt):
		print '\n[*] Ctrl + C detetcted Good bye'
		exit()
