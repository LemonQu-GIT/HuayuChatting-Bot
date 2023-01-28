import numpy,xlwt
from tools import *
from matplotlib import pyplot
from datetime import *
from argparse import ArgumentParser

info=readInfoByJson()
chattingAllWeeks=info[6]

def paint(weekKey,nextKey):
    schoolID2freq:dict[str,int]={}
    weekValue=chattingAllWeeks[weekKey]
    for schoolID in weekValue:
         if schoolID=='other':continue
         if not schoolID in schoolID2freq:schoolID2freq[schoolID]=0
         schoolID2freq[schoolID]+=1
    sortedFreq=sortByValue(schoolID2freq)
    freqsum:int=0
    for i in range(len(sortedFreq)):
        freqsum+=sortedFreq[i][1]
    schoolIDList=[]
    freqList=[]
    for i in range(len(sortedFreq)):
        schoolIDList.append(sortedFreq[i][0])
        freqList.append(sortedFreq[i][1]/freqsum)
    freq2pie=numpy.array(freqList)
    schoolID2label=schoolIDList
    pyplot.pie(freq2pie,labels=schoolID2label,labeldistance=0.5,radius=1.2,rotatelabels=True)
    pyplot.title('%s~%s'%(weekKey[0:10],nextKey[0:10]))
    pyplot.savefig("C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekpie.png")

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--time",
	    help="Choose the day you want",
	    dest="time",default="2020-02-23")
    args = arg_parser.parse_args()
    dayKey=args.time
    dayKey+=' 00:00:00'
    lastKey=None
    for weekKey in chattingAllWeeks:
        if lastKey is None:
            lastKey=weekKey
            weekKey='2020-02-23 00:00:00'
        if lastKey<=dayKey<=weekKey:
            paint(lastKey,weekKey)
            break
        lastKey=weekKey