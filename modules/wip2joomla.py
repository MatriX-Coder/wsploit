#!/usr/bin/python
# Wsploit Project

'''
this is joomla 
websites grabber
in same webserver 
using bing
'''

try:
	import urllib2, re, sys, os
except:
	print 'You need urllib2 , os , re and sys librarys installed.'

# i found this code on stackoverflow it counts lines in text file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
def lista(ipz):
	ss = open(ipz , 'r')
	ips = ss.readlines()
	for ip in ips:
		ip = ip.replace('\n' , '')
		one(ip) 

def one(s):
	try:
		page = 1
		print "\n"
		while page <= 200:
			bing = "http://www.bing.com/search?q=ip%3A"+s+"+index.php?option=com&first="+str(page)
			openbing  = urllib2.urlopen(bing)
			readbing = openbing.read()
			findbing = re.findall('<li class="b_algo"><h2><a href="(.*?)" h=',readbing)
			for i in range(len(findbing)):
				x = findbing[i]
				xz = re.findall('(.*?)index.php',x)
				ss = open('modules/tmp/jm.txt','a+')
				ss.writelines(xz)
				ss.writelines('\n')
				num_lines = sum(1 for line in open('modules/tmp/jm.txt'))
				sys.stdout.write("Number of Sites: %d   \r" % (num_lines) )
				sys.stdout.flush()
			page = page + 10

		print '\n'
		lines_seen = set()
		outfile = open('modules/tmp/jm1.txt', "a+")
		for line in open('modules/tmp/jm.txt', "r"):
    			if line not in lines_seen:
					outfile.write(line)   
					lines_seen.add(line)
		outfile = open('modules/tmp/jm1.txt','r')
		ss = outfile.read()
		print '\n' + '[*]-Target : ' + s + '\n'
		print ss
		print 'Uniq Sites Found : %s\n' % file_len('modules/tmp/jm1.txt')
		print '_'*50
		outfile.close()
		os.remove('modules/tmp/jm1.txt')			
		os.remove('modules/tmp/jm.txt')
	except(KeyboardInterrupt):
		print '\n[*] Ctrl + C detetcted Good bye'
		exit()
		
def init():
	print '\n[1]-Single IP'
	print '[2]-List Of IPs\n'
	line_1 = "Enter Option : "
	choose = raw_input(line_1)
	if choose.isdigit():
		choose = int(choose)
		pass
	else :
		print "Choose From List Bro"
		exit()
	if choose == 1:
		oneip = raw_input('\nEnter IP : ')
		one(oneip)
	if choose == 2:
		ipz = raw_input('\nEnter Text File : ')
		lista(ipz)
		
