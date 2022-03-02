#Please hope I'll never use this shit again

import os
import requests

c = 1
p = 1
t = ""
t_tries = 0

def urldlmk(url,c,p,t):
    url = (str(url)+'chapters/'+str(c)+'/'+str(t)+str(p)+'.jpg')
    return url

def download(urldl,p):
    dl = requests.get(urldl, allow_redirects=True)
    if dl.status_code == 404 :
        return "404"
    else :
        return dl

print("I really do hate my life")

os.chdir(r"C:\Users\fuschy\Desktop\temp")
url = input("Enter the desired lescan url: ")

while True :
    while t_tries < 3:
                urldl = urldlmk(url,c,p,t)
                print(urldl)
                dl = download(urldl,p)
                if dl == "404" :
                    t = t+'0'
                    print("Error")
                    t_tries += 1
                    
                else : 
                    open((str(c)+'-'+str(p)+'.jpg'), 'wb').write(dl.content)
                    print(str(c)+'-'+str(p)+" Downloaded!")
                    t = ""
                    t_tries = 0
                    p += 1
    t = ""
    p = 1
    t_tries = 0
    c += 1