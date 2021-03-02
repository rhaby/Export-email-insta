import os
import sys
import hashlib
import mechanize
import requests
from time import sleep




if sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")


def rhaby(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(50. / 1000)


API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
__banner__ = """\033[1;33m
 |\   /| IBFrhaby - insta-Brute-Force this tools is free and open source (Beta) 
  \|_|/  Author: ArHaBy*
  /. .\  Version: 2.0v
 =\_Y_/= Telegram: @ciku370
  {>o<}  Telegram: @rhaby
=============================================="""
print(__banner__)
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 1- hashtag user")
rhaby("$")
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 2- insta checker")
rhaby("$")
ali1 = input("$ enter number tool : ")
if ali1 == '2':
    import requests
    import os
    from bs4 import BeautifulSoup

    


    class Instagram:
        def __init__(self, username):
            self.username = str(username)

        def get_request(self):
            """
            Returns page contents
            :return str:
            """
            request = requests.get('https://www.instagram.com/' + self.username)
            if request.status_code == 200:
                return request.content
            else:
                raise Exception(" This username is not used: {}".format(self.username))

        def content_parser(self):
            """
            Returns parsed page contents
            :return str:
            """
            content = self.get_request()
            source = BeautifulSoup(content, 'html.parser')
            return source

        def get_info(self):
            """
            Returns instagram infos
            :return dict:
            """
            source = self.content_parser()
            description = source.find("meta", {"property": "og:description"}).get("content")
            info_list = description.split("-")[0]
            followers = info_list[0:info_list.index("Followers")]
            info_list = info_list.replace(followers + "Followers, ", "")
            following = info_list[0:info_list.index("Following")]
            info_list = info_list.replace(following + "Following, ", "")
            posts = info_list[0:info_list.index("Posts")]
            results = {"followers": followers, "following": following, "posts": posts}
            return results

        def print_info(self):

            url = "https://www.instagram.com/" + self.username + "/?__a=1"
            r = requests.get(url)
            businessA = str(r.json()["graphql"]["user"]["is_business_account"])
            
            photo = str(r.json()["graphql"]["user"]["profile_pic_url_hd"])
            idd = str(r.json()["graphql"]["user"]["id"])
            info = self.get_info()
            # ______________________________________
            s = '35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":\"' + self.username + '\","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}'
            userAAgent = "Instagram 99.4.0"
            url = 'https://i.instagram.com/api/v1/users/lookup/'
            myobj = {'signed_body': s, "ig_sig_key_version": "9"}
            x = requests.post(url, headers={'User-Agent': userAAgent}, data=myobj)
            

            if (businessA == "True"):
                payload = ''
                url = ("https://i.instagram.com/api/v1/users/" + idd + "/info/")
                headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
                    "cache-control": "max-age=0",
                    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=4420; shbts=1614677973.417921; csrftoken=ZzUmpQwG0f2qWmprQb7qkBLFSShJ8yHa; ds_user_id=45045757437; sessionid=45045757437%3AvdEk0feDj30hFk%3A6; rur=FTW",
                    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)"
                }
                response = requests.Session().get(url, data=payload, headers=headers)
                email = (response.json()["user"]["public_email"])
                if (email == ""):
                    print(' ☠' * 15)
                    print ("the user don't have email")
                else:
                    print(' ☠' * 15)
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(info["followers"]))
                    print(" Following: {}".format(info["following"]))
                    print ("email : " + email)
                    with open('Available.txt', 'a') as x:
                        x.write(email + "\n")


                    
                    
            
                
    class Helper:
        @staticmethod
        def read_file(filename):
            """
            Returns account lists
            :param filename:
            :return list:
            """
            accounts = [line.rstrip('\n') for line in open(filename, encoding="utf8")]
            return accounts

        @staticmethod
        def retry():
            """
            Decides wanna try again
            :return boolean:
            """
            q = input(" Press E to repeat operation or press H to exit the program: ")
            if q.upper() == "E":
                os.system("cls||clear")
                return True
            else:
                return False


    if __name__ == "__main__":
        while True:
            accounts = Helper.read_file("accounts.txt")
            for account in accounts:
                info = Instagram(account)
                try:
                    info.print_info()
                except Exception as e:
                    print(e)

            retry = Helper.retry()
            if not retry:
                break

if ali1 == '1':
    import requests
    import secrets
    import sys as n
    import time as mm
    from time import sleep
    jruksr= '\033[1;32m'
    jruks = '\033[1;33m'
    ruks_q = '\033[1;36m'
    ruks_h = '\033[1;31m'
    print(ruks_q+'='*60)
    ruks_f=f"""
    {jruksr}
      _____           _                    
     |_   _|         | |                   
       | |  _ __  ___| |_ __ _             
       | | | '_ \/ __| __/ _` |            
      _| |_| | | \__ \ || (_| |            
     |_____|_| |_|___/\__\__,_|      {jruks}      
      _               _     _              
     | |             | |   | |             
     | |__   __ _ ___| |__ | |_ __ _  __ _ 
     | '_ \ / _` / __| '_ \| __/ _` |/ _` |
     | | | | (_| \__ \ | | | || (_| | (_| |
     |_| |_|\__,_|___/_| |_|\__\__,_|\__, |
                                      __/ |
                                     |___/ 
    """
    print(ruks_f)
    print(ruks_q+'='*60)
    head = {
    'HOST': "www.instagram.com",
    'KeepAlive' : 'True',
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
    'Cookie': 'cookie',
    'Accept' : "*/*",
    'ContentType' : "application/x-www-form-urlencoded",
    "X-Requested-With" : "XMLHttpRequest",
    "X-IG-App-ID": "936619743392459",
    "X-Instagram-AJAX" : "missing",
    "X-CSRFToken" : "missing",
    "Accept-Language" : "en-US,en;q=0.9"
    }

    ruks = requests.Session()
    rhaby = 'welcome to hashtag user'

    #===============================#
    m1 = input('Hashtag_1 : '+ruks_h)
    m2 = input('Hashtag_2 : '+ruks_q)
    m3 = input('Hashtag_3 :'+ruks_h)
    m4 = input('Hashtag_4 : '+ruks_q)
    m5 = input('Hashtag_5 : '+ruks_h)
    m6 = input('Hashtag_6 : '+ruks_q)
    fileuser = open('accounts.txt', 'a')
    #===============================#
    print('The rhaby developer tool is free, not for sale')
    print('='*60) 
    def ruks1():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m1}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks1()

    #===============================#
    def ruks2():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m2}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                
                print('='*60)
         
    ruks2()	
    #===============================#
    def ruks3():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m3}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                
                print('='*60)
         
    ruks3()
    #===============================#
    def ruks4():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m4}'
                    ruks = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks4()
    #===============================#
    def ruks5():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m5}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks5()			
    #===============================#
    def ruks6():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m6}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            fileuser.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                    print('='*60)
                    print(u'نتهى السحب')  
                    print(u' في لستة accounts.txt ')       
              
    ruks6()			
    #===============================#









