import datetime
import os
import random

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