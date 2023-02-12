import requests, logging, time, os, datetime, random, json, urllib
import pandas as pd
from urllib.parse import *
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def log(event):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("["+time+"] "+event)
    os.system("echo ["+time+"] "+event+" >> oops.log")

def esu(schooID):
    if schooID==24885:
        gifVpng = random.randint(0,2)
        if gifVpng==0:
            img = random.randint(1,5)
            imgo = str(img)+".gif"
            return imgo
        elif gifVpng==1:
            img = random.randint(1,11)
            imgo = str(img)+".png"
            return imgo
        else:
            img = random.randint(1,1)
            imgo = str(img)+".jpg"
            return imgo
    else:
        return None

def findImgURL(URL):
    prefixcod=URL.split('url=')[1]
    suffixcode=prefixcod.split(']')[0]
    return suffixcode

def Download_Image(downloadUrl: str or list, saveImagePath: str, headers: dict = None, proxies: dict = None) -> bool or str:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(funcName)s -> %(message)s')
    agent = UserAgent()
    if isinstance(downloadUrl, str):
        downloadUrlParse = urlparse(downloadUrl)
        if headers is None:
            headers = {
                'User-Agent': agent.random,
                'Referer': f'{downloadUrlParse.scheme}://{downloadUrlParse.netloc}',
                'Host': downloadUrlParse.netloc,
            }
            response = requests.get(downloadUrl, headers=headers, timeout=20, proxies=proxies).content
        if os.path.isdir(saveImagePath):
            newSaveImagePath = saveImagePath + fr'\0.jpg'
        else:
            newSaveImagePath = os.path.splitext(saveImagePath)[0] + '.jpg'
        with open(newSaveImagePath, 'wb') as f:
            f.write(response)

def checkgroup(QQID):
    with open('config.json', encoding='utf-8') as config:
        result = json.load(config)
        AdminL = result.get('permissions').get('Admin')
        ExperimentalL = result.get('permissions').get('Experimental')
        BanL = result.get('permissions').get('Ban')
        BotL = result.get('permissions').get('Bot')
        if QQID in ExperimentalL:
            return "Experimental"
        elif QQID in AdminL:
            return "Admin"
        elif QQID in BanL:
            return "Ban"
        elif QQID in BotL:
            return "Bot"
        else:
            return "User"

def searchHuayuWiki(item):
    url = urllib.parse.quote("https://hywiki.xyz/wiki/"+str(item),safe='/:?=.')
    req = requests.get(url=url)
    req.encoding = "utf-8"
    html = req.text
    soup = BeautifulSoup(req.text,features="html.parser")
    passage = soup.find("div",class_="mw-parser-output")
    if passage is None:
        return "Failed to fetch content of "+'"'+item+'" from hywiki'
    else:
        outputpre1 = passage.text.strip()
        return outputpre1.replace('[编辑 | 编辑源代码]','')

def getConfig(things):
    with open('config.json', encoding='utf-8') as config:
        result = json.load(config)
        if things == "yolov5_path":
            return result.get('config').get('yolov5_path')
        elif things == "go-cqhttp_image_path":
            return result.get('config').get("go-cqhttp_image_path")
        elif things == "QQImgDownload":
            return result.get('config').get("QQImgDownload")
        elif things == "botQID":
            return result.get('config').get("botQID")
        else:
            return "Failed"