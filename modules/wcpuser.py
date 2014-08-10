#!/usr/bin/python
# Wsploit Project

'''
this is CPanel user finder
module it works in single
or with list I know the code 
looks like shit :(
'''

try:
	import httplib
except:
	print 'You Need httplib Installed'

import wcolors

def one():
	line_1 = "\nEnter site : "
	site_cp = raw_input(line_1)

	if 'http://' in site_cp:
		site_cp = site_cp.replace('http://','')
	if '/' in site_cp:
		site_cp = site_cp.replace('/', '')

	users = site_cp
	if 'www' in users:
		users = users.replace('www','')
	if '.' in users:
		users = users.replace('.', '')
	if '-' in users:
		users = users.replace('-','')

	print '\n[*] Target : %s\n' % site_cp

	while len(users) > 1 :
		users = users[:-1]


		conn = httplib.HTTPConnection(site_cp)
		conn.request("GET", '/cgi-sys/guestbook.cgi?user=%s' % users)
		r1 = conn.getresponse()
		rep = r1.read()
		if 'invalid username' in rep.lower():
			print users
		else:
			print wcolors.color.BLUE + "\n--> Found %s\n" % (users) + wcolors.color.ENDC

def lista():
	line_2 = "\nEnter List Path : "

	site_cp = raw_input(line_2)
	sites = open(site_cp,'r')
	sites =	sites.readlines()
	for site in sites:
		if 'http://' in site:
			site = site.replace('http://','')
		if '/' in site:
			site = site.replace('/', '')
		print '\n[*] Target : %s\n' % site
		site = site.strip()


		users = site
		if 'www' in users:
			users = users.replace('www','')
		if '.' in users:
			users = users.replace('.', '')
		if '-' in users:
			users = users.replace('-','')
		while len(users) > 1 :

			conn = httplib.HTTPConnection(site)
			conn.request("GET", '/cgi-sys/guestbook.cgi?user=%s' % users)
			r1 = conn.getresponse()					
			rep = r1.read()
			if 'invalid username' in rep.lower():
				print users
			else:
				print wcolors.color.BLUE  + "\n--> Found : %s\n" % (users) + wcolors.color.ENDC
				ss = open('cpusers.txt','a+')
				ss.writelines(users+'\n')
			users = users[:-1]
	ss = open('cpusers.txt','r')
	final = ss.read()
	print '\n\nAll Users : \n' + final
def init():
	print '\n[1]-Single URL'
	print '[2]-List Of URLs\n'
	line_3 = "Enter Option : "
	choose = raw_input(line_3)
	if choose.isdigit():
		choose = int(choose)
		pass
	else :
		print "Choose From List Bro"
		exit()
	if choose == 1:
		one()
	if choose == 2:
		lista()
	
