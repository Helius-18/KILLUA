import requests
from bs4 import BeautifulSoup
import webbrowser
import time
dicto={}

def getter(url):
    global r,soup
    try:
        r=requests.get(url=url)
        soup=BeautifulSoup(r.text,"html.parser")
    except:
        pass
    if(url=="delete"):
        del soup
        del r


def change_episode(link):
    try:
        getter("https://hdonlines.net/"+link)
        global dicto
        getter("https:"+str(soup.find("iframe")["src"]))
        souped=soup.find_all("li",class_="linkserver")
        getter("delete")
        for i in souped:
            dicto[str(i.text)]=i["data-video"]
        try:
            del dicto["Main Server"]
            del dicto["Server Hyrax"]
            del souped
        except:
            pass
        if("Beta Server" in dicto.keys()):
            dicto["Beta Server"]=("https:"+str(dicto["Beta Server"]))
        fdicto=[]
        i=0
        for server in dicto.keys():
            fdicto.append({i:dicto[server]})
            i+=1
        return(fdicto)
    except:
        print("epsd not found")
        quit()

def change_server():
    print("changing to server...",len(dicto))
    if("Xstreamcdn" in dicto.keys()):
        webbrowser.open(dicto["Xstreamcdn"])
        del dicto["Xstreamcdn"]
    elif("Doodstream" in dicto.keys()):
        webbrowser.open(dicto["Doodstream"])
        del dicto["Doodstream"]
    elif("Mixdrop" in dicto.keys()):
        webbrowser.open(dicto["Mixdrop"])
        del dicto["Mixdrop"]
    elif("StreamSB" in dicto.keys()):
        print("This server may contain ads")
        webbrowser.open(dicto["StreamSB"])
        del dicto["StreamSB"]
    elif(len(dicto)==0):
        print("no other servers")
        time.sleep(2)
        quit()

def random_stuff(url):
    getter(url) 
    getter("https://hdonlines.net"+str(soup.find("a",class_="bwac-btn")["href"]))
    epis=soup.find_all("a",class_="btn-eps")
    depis=[]
    for i in range(len(epis)):
        depis.append({
            "href":epis[i]["href"]
        })
    return(depis)
    # n=len(epis)-int(input("Choose episode:\n"))
    # change_episode(n,epis)
    # while(True):
    #     t=int(input("1.next epsd\t2.pre epsd\t3.coustom epsd\n4.change movie(or)series\t5.not working(change server)\t6.exit\n"))
    #     if(t==1):
    #         n-=1
    #         change_episode(n,epis)
    #     elif(t==2):
    #         n=n+1
    #         change_episode(n,epis)
    #     elif(t==3):
    #         n=len(epis)-int(input("Enter epsd no:"))
    #         change_episode(n,epis)
    #     elif(t==5):
    #         change_server()
    #         continue
    #     elif(t==4):
    #         name=input("Enter name:\n")
    #         search(name)
    #         del name
    #         break
    #     elif(t==6):
    #         quit()
    #     elif(t==1830):
    #         print(len(epis)-n,epis,dicto,sep="\n")
    #     else:
    #         print("wrong input")
    #         time.sleep(2)
    #         break


def search(name):
    print("hai")
    # n=int(input())
    # random_stuff("https://hdonlines.net"+str(names[n]["href"]))

def killua(game):
    name=str(game).strip()
    getter("https://hdonlines.net/search/?name={}".format(name.replace(" ","+")))
    names=soup.find_all("a",class_="ml-mask jt")
    dmnames=[]
    for i in range(len(names)):
        dmnames.append({
            "name":str(names[i]["title"]),
            "image":str(names[i].find_next('img',class_="lazy thumb mli-thumb")["data-original"]).replace("\n","").replace("\t","").replace(" ",""),
            "href":str(names[i]["href"]).replace("\n","").replace("\t","").replace(" ","")
        })
    return(dmnames)