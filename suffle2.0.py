#eswarkada#srinuneelapala

import requests
from bs4 import BeautifulSoup
#d={}
f=open("suffle123.txt","a")
print("enter id number format like this... ""161405""")
a=input("enter starting idno: ")
b=input("enter endding idno: ")
url="http://10.11.4.25/p2Shuffle/index.php"
for i in range(int(a),int(b)):
    i=str(i)
    idno='N'+i
    hee={"ID":idno,"submit":"Submit"}
    r=requests.post(url,data=hee)
    a=r.text
    soup1 = BeautifulSoup(a,'html.parser')
    a1=soup1.find_all('b')[5].get_text()    # 5-ID
    a2=soup1.find_all('b')[13].get_text()   # 13-EXAM HALL
    a3=soup1.find_all('b')[15].get_text()    # DESK POSITION
    a4=soup1.find_all('b')[9].get_text()    # 9-YEAR & BRANCH
    a5=soup1.find_all('b')[17].get_text()    # 17-IP ADDRESS
    a6=soup1.find_all('b')[7].get_text()    #7-NAME
    print(a1+" "+a2+" "+a3+" "+a4+" "+a5+" "+a6)
    f.write(a1+"|"+a2+"|"+a3+"|"+a4+"|"+a5+"|"+a6+"\n")
while(True):
    exhall=input("Enter the ex hall like A3-SF9: ")
    mainlist=[]
    f=open("suffle123.txt","r")
    for i in f.readlines():
        mainlist.append((i.strip("\n")).split("|"))
    print("\n------------------------students of same room----------------------")
    for i in range(0,len(mainlist)):
        if mainlist[i][3]==exhall:
            print(mainlist[i][0]+" "+mainlist[i][1]+" "+mainlist[i][2]+" "+mainlist[i][3])
