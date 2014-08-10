#!/usr/bin/python
# Wsploit Project

'''
this is reverse 
ip script that grabs
all websites in same 
webserver using 
yougetsignal
'''

# Coded by JoinSe7en here is the original code http://goo.gl/8fs8K1  just added it to wsploit
# note you have limited number of trys

try:
	import urllib2, urllib, json, sys
except:
	print 'You need urllib2 , urllib , json and sys librarys installed.'
	
def init():

		url = "http://domains.yougetsignal.com/domains.php"
		contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
		def request(target, httpsproxy=None, useragent=None):
			url = "http://domains.yougetsignal.com/domains.php"
			
			global contenttype
			contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
			if not useragent:
				useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
			else:
				print "["+ bc.G + "+" + bc.ENDC + "] User-Agent: " + useragent

			if httpsproxy:
				print "["+ bc.G + "+" + bc.ENDC + "] Proxy: " + httpsproxy + "\n"
				opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'http': 'http://' + httpsproxy}))
				urllib2.install_opener(opener)

			postdata = [('remoteAddress',target),('key','')]
			postdata = urllib.urlencode(postdata)

			request = urllib2.Request(url, postdata)

			request.add_header("Content-type", contenttype)
			request.add_header("User-Agent", useragent)
			try:
				result = urllib2.urlopen(request).read()
			except urllib2.HTTPError, e:
				print "Error: " + e.code
			except urllib2.URLError, e:
				print "Error: " + e.args

			obj = json.loads(result)
			return obj


		def output(obj):
			print "Status:    " + obj["status"]
			if obj["status"] == "Fail":
				message = obj["message"].split(". ")
				print  "Error:     "  + message[0] + "."
				sys.exit(1)

			print "\nSites Found : " + obj["domainCount"] + '\n'
			for domain, hl in obj["domainArray"]:
				print domain
		target = raw_input('\nEnter IP : ')
		obj = request(target)
		output(obj)
