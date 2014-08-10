#!/usr/bin/python
# Wsploit Project

'''
this is wordpress 
websites grabber
in same webserver 
using bing
'''

# fixed by khaled ferjani thx so much ;)

try:
	import urllib2, re
except:
	print 'You need urllib2 and re librarys installed.'

def init():
	path = raw_input("Sites Path : ")
	ss = open(path,'r')
	sites = ss.readlines()
	for site in sites:
		alexa = 'http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % site
		openalexa = urllib2.urlopen(alexa)
		readalexa = openalexa.read()
		popularity_rank = re.findall("POPULARITY[^\d]*(\d+)", readalexa)
		aa = popularity_rank[0]
		print site + '\t---> ' + aa
