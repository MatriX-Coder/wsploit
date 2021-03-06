#!/usr/bin/python
# Wsploit Project

'''
this is simple joomla
components scanner
'''

try:
	import urllib2, Queue
except:
	print 'You need urllib2 and Queue librarys installed.'

try:
	from threading import Thread
except:
	print 'You need threading library installed.'

try:
	from time import sleep
except:
	print 'You need time library installed.'


paths = [
'/components/com_tag',
'/components/com_virtuemart',
'/components/com_jvehicles',
'/components/com_s5clanroster',
'/components/com_fireboard',
'/components/com_fabrik',
'/components/com_jinc',
'/components/com_xcloner-backupandrestore',
'/components/com_dshop',
'/components/com_ponygallery',
'/components/com_bearleague',
'/components/com_obsuggest',
'/components/com_alameda',
'/components/com_estateagent',
'/components/com_collector',
'/components/com_qcontacts',
'/components/com_niceajaxpoll',
'/components/com_xmap',
'/components/com_team',
'/components/com_joomnik',
'/components/com_question',
'/components/com_jmsfileseller',
'/components/com_rsfiles',
'/components/com_versioning',
'/components/com_hello',
'/components/com_calcbuilder',
'/components/com_jmsfileseller',
'/components/com_xmovie',
'/components/com_people',
'/components/com_idoblog',
'/components/com_adsmanager',
'/components/com_xgallery',
'/components/com_alfurqan15x',
'/components/com_alfurqan',
'/components/com_billyportfolio',
'/components/com_jimtawl',
'/components/com_content',
'/components/com_jfuploader',
'/components/com_kunena',
'/components/com_jooproperty',
'/components/com_jsupport',
'/components/com_markt',
'/components/com_img',
'/components/com_clanlist',
'/components/com_clan',
'/components/com_ckforms',
'/components/com_dcnews',
'/components/com_connect',
'/components/com_rsappt_pro2',
'/components/com_techfolio',
'/components/com_zcalendar',
'/components/com_tpjobs',
'/components/com_simpleshop',
'/components/com_sef',
'/components/com_searchlog',
'/components/com_contact',
'/components/com_enmasse',
'/components/com_elite_experts',
'/components/com_ezautos',
'/components/com_jgen',
'/components/com_jphone',
'/components/com_mosets',
'/components/com_jefaqpro',
'/components/com_picsell',
'/components/com_ongallery',
'/components/com_equipment',
'/components/com_zoomportfolio',
'/components/com_amblog',
'/components/com_joltcard',
'/components/com_jp_jobs',
'/components/com_bfquiztrial',
'/components/com_qpersonel',
'/components/com_pandafminigames',
'/components/com_golfcourseguid',
'/components/com_jejob',
'/components/com_jeajaxeventcalendar',
'/components/com_jradio',
'/components/com_spidercatalog',
'/components/com_/components/commedia',
'/components/com_fss',
'/components/com_icagenda',
'/components/com_spidercalendar',
'/components/com_joomgalaxy',
'/components/com_ornekek',
'/components/com_weblinks',
'/components/com_rokmodule',
'/components/com_discussions',
'/components/com_hm/components/community',
'/components/com_eslamiat',
'/components/com_listing',
'/components/com_jeemasms',
'/components/com_yjcontactus',
'/components/com_timereturns',
'/components/com_jce',
'/components/com_joomtouch',
'/components/com_jdirectory',
'/components/com_jesubmit',
'/components/com_sobi2',
'/components/com_acooldebate',
'/components/com_booklibrary',
'/components/com_acymailing',
'/components/com_doqment',
'/components/com_allcinevid',
'/components/com_jotloader',
'/components/com_jeauto',
'/components/com_ccboard',
'/components/com_ccinvoices',
'/components/com_flipwall',
'/components/com_sponsorwall',
'/components/com_cbe',
'/components/com_jscalendar',
'/components/com_restaurantguide',
'/components/com_nkc',
'/components/com_aardvertiser',
'/components/com_clantools',
'/components/com_remository',
'/components/com_dateconverter',
'/components/com_wmtpic',
'/components/com_donateprocess',
'/components/com_gamesbox',
'/components/com_jcafe',
'/components/com_awd_song',
'/components/com_picasa2gallery',
'/components/com_ybggal',
'/components/com_joomdocs',
'/components/com_answers',
'/components/com_galleryxml',
'/components/com_oziogallery2',
'/components/com_listbingo',
'/components/com_easygb',
'/components/com_jtickets',
'/components/com_jesectionfinder',
'/components/com_realtyna',
'/components/com_/components/community',
'/components/com_jomestate',
'/components/com_jtickets',
'/components/com_cinema',
'/components/com_jstore',
'/components/com_annonces',
'/components/com_lead',
'/components/com_sar_news',
'/components/com_chronocontact',
'/components/com_chronoconnectivity',
'/components/com_djartgallery',
'/components/com_quran',
'/components/com_g2bridge',
'/components/com_reservations',
'/components/com_jepoll',
'/components/com_mycar',
'/components/com_mediqna',
'/components/com_zelig',
'/components/com_bookmarks',
'/components/com_hotproperty',
'/components/com_jombib',
'/components/com_store',
'/components/com_mosforms',
'/components/com_/components/comprofiler',
'/components/com_crowdsource',
'/components/com_camp',
'/components/com_ms/components/comment',
'/components/com_extcalendar',
'/components/com_imoti',
'/components/com_product',
'/components/com_event',
'/components/com_simpledownload',
'/components/com_news',
'/components/com_article',
'/components/com_jequoteform',
'/components/com_konsultasi',
'/components/com_sebercart',
'/components/com_php',
'/components/com_jinc',
'/components/com_mytube',
'/components/com_jbudgetsmagic',
'/components/com_surveymanager',
'/components/com_jreservation',
'/components/com_foobla_suggestions',
'/components/com_djcatalog',
'/components/com_turtushout',
'/components/com_alphauserpoints',
'/components/com_lucygames',
'/components/com_bfsurvey_profree',
'/components/com_tpdugg',
'/components/com_joomloc',
'/components/com_joomlub',
'/components/com_artportal',
'/components/com_agora',
'/components/com_gameserver',
'/components/com_digifolio',
'/components/com_bca-rss-syndicator',
'/components/com_expose',
'/components/com_equotes',
'/components/com_media',
'/components/com_misterestate',
'/components/com_wrapper',
'/components/com_mailto',
'/components/com_autartimonial',
'/components/com_artforms',
'/components/com_redshop',
'/components/com_staticxt',
'/components/com_spa',
'/components/com_jomtube',
'/components/com_golfcourseguide',
'/components/com_huruhelpdesk',
'/components/com_joomdle',
'/components/com_youtube',
'/components/com_joomla-visites',
'/components/com_ttvideo',
'/components/com_appointinator',
'/components/com_photomapgallery',
'/components/com_spielothek',
'/components/com_pbbooking',
'/components/com_beamospetition',
'/components/com_neorecruit',
'/components/com_cgtestimonial',
'/components/com_jgrid',
'/components/com_zina',
'/components/com_pro_desk',
'/components/com_user',
'/components/com_k2',
'/components/com_rsbook_15',
'/components/com_gk3_photoslide',
'/components/com_jvideodirect',
'/components/com_jcalpro',
'/components/com_banners',
'/components/com_datsogallery',
'/components/com_joomradio',
'/components/com_jfbconnect',
'/components/com_myblog',
'/components/com_phocamaps',
'/components/com_contact_enhanced',
'/components/com_aicontactsafe',
'/components/com_poll']

def one():
		def test(target,path):
			if 'http://' not in target:
				target = 'http://'+target

			bb = target+path
			try:
				a = urllib2.urlopen(bb)
				c = a.getcode()
				if c == 200:
					print 'Found ---> '+path[12:]
			except urllib2.URLError:
				pass
		thrdlst = []
		target = raw_input('\nEnter site : ')

		for path in paths:
			t = Thread(target=test , args=(target,path))
			t.start()
			thrdlst.append(t)
			sleep(0.009)
		for b in thrdlst:
			b.join()


    
def lista():
	path = raw_input('\nEnter List Path : ')
	sites = open(path,'r')
	sites =	sites.readlines()
	print '\n'
	for site in sites:
		if 'http://' not in site:
			site = 'http://'+site
		site = site.strip()
		print '\n[*] Target : %s\n' % site
		for path in paths:
			bb = site+path
			try:
				a = urllib2.urlopen(bb)
				c = a.getcode()
				if c == 200:
					print 'Found ---> '+path[12:]
			except urllib2.URLError:
				pass

		

def init():
	print '\n[1]-Single URL'
	print '[2]-List Of URLs\n'
	line_1 = "Enter Option : "
	choose = raw_input(line_1)
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
		

