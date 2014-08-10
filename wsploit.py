#!/usr/bin/python
# 									bismillah 

'''

www.fb.com/matrixcoder2 | matrix_coder@outlook.com | www.matrixcoder.co.vu
Thanks for people who helped for making this project available : Khaled Ferjani and all python community
Wsploit works well in linux environment but it needs some editing if using under windows (remove the colors)
Wsploit is coded by MatriX Coder my real name is Mohamed Aziz and i'm from tunisia
This project is inspired from websploit link http://goo.gl/EO0RFR
'''


try:
	import os, sys
except:
	print 'You need print os and sys librarys installed.'
	
try:
	from platform import system
except:
	print 'You need print platform library installed.'

sys.stdout.write("\x1b]2;Wsploit V1.8\x07") # setting the title

from modules import wcolors
from modules import wmd5_cracker
from modules import wjoomlacomponents
from modules import wcpuser
from modules import wip2sites
from modules import wip2joomla
from modules import wip2wp
from modules import walexarank
from modules import wreverseip
from modules import wftpanon

def wmodules():

	try :

		print "[1]-Online MD5 Cracker"
		print "[2]-CPanel User Finder"
		print "[3]-All Websites On Same Server - (Bing)"
		print "[4]-Joomla Websites On Same Server - (Bing)"
		print "[5]-Wordpress Websites On Same Server - (Bing)"
		print "[6]-Alexa Rank"
		print "[7]-Reverse IP - (Yougetsignal)"
		print "[8]-Joomla Compnent Scanner"
		print "[9]-FTP Anonymous Lgin\n"
		line_1 = "Enter Option : "
		choose = raw_input(line_1)
		if choose == "exit":
			exit()

		if choose.isdigit():
			choose = int(choose)
			pass
		else :
			print "Choose From List Bro"
			exit()
		if choose == 1:
			wmd5_cracker.init()
		if choose == 2:
			wcpuser.init()
		if choose == 3:
			wip2sites.init()
		if choose == 4:
			wip2joomla.init()
		if choose == 5:
			wip2wp.init()
		if choose == 6:
			walexarank.init()
		if choose == 7:
			wreverseip.init()
		if choose == 8:
			wjoomlacomponents.init()
		if choose == 9:
			wftpanon.init()
		elif choose > 9 :
			print "Choose From List Bro"
			exit()

	except(KeyboardInterrupt):
		print "\n[*] Ctrl + C detetcted Good bye"
		exit()

# this is the logo part
def wlogo():
	
	logo = '''
	 .S     S.     sSSs   .S_sSSs    S.        sSSs_sSSs     .S  sdSS_SSSSSSbs
	.SS     SS.   d%%SP  .SS~YS%%b   SS.      d%%SP~YS%%b   .SS  YSSS~S%SSSSSP
	S%S     S%S  d%S'    S%S   `S%b  S%S     d%S'     `S%b  S%S       S%S
	S%S     S%S  S%|     S%S    S%S  S%S     S%S       S%S  S%S       S%S
	S%S     S%S  S&S     S%S    d*S  S&S     S&S       S&S  S&S       S&S
	S&S     S&S  Y&Ss    S&S   .S*S  S&S     S&S       S&S  S&S       S&S
	S&S     S&S  `S&&S   S&S_sdSSS   S&S     S&S       S&S  S&S       S&S
	S&S     S&S    `S*S  S&S~YSSY    S&S     S&S       S&S  S&S       S&S
	S*S     S*S     l*S  S*S         S*b     S*b       d*S  S*S       S*S
	S*S  .  S*S    .S*P  S*S         S*S.    S*S.     .S*S  S*S       S*S
	S*S_sSs_S*S  sSS*S   S*S          SSSbs   SSSbs_sdSSS   S*S       S*S
	SSS~SSS~S*S  YSS'    S*S           YSSP    YSSP~YSSY    S*S       S*S
	                     SP                                 SP        SP
	                     Y                                  Y         Y
	_______________________________________________________________________\n\n'''


	print wcolors.color.BLUE + logo + wcolors.color.ENDC
	print '\t[Author : MatriX Coder (Mohamed Aziz From Tunisia)]'
	print '\t[Facebook : www.fb.com/matrixcoder2]'
	print '\t[Version : V1.8]\n\n' 


def main():

	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')

	wlogo()
	wmodules()

	# removing the shit
	try:
		# All bing
		os.remove('modules/tmp/all.txt')
		os.remove('modules/tmp/all1.txt')
		# Joomla bing
		os.remove('modules/tmp/jm.txt')
		os.remove('modules/tmp/jm1.txt')
		# Wordpress bing
		os.remove('modules/tmp/wp.txt')
		os.remove('modules/tmp/wp1.txt')
	except:
		pass
if __name__ == '__main__':
	main()


