from receive import rev_msg
from send import send_msg
from hyxq import log
from hyxq import esu
import os
import socket
import requests
import random
import time
import traceback
import subprocess
import subprocess

log('Bot started')
i=0
while True:
    try:
        rev = rev_msg()
        if rev == None:
            continue
        if rev["post_type"] == "message":
            if rev["message_type"] == "group":
                message=rev['raw_message']
                if "[CQ:at,qq=3311599537]" in message:
                    qq = rev['sender']['user_id']
                    group = rev['group_id']
                    #issuecom = message.split('[CQ:at,qq=3311599537] ')[1]
                    #log("User "+str(qq)+" in group "+str(group)+" issued command "+issuecom)
                    if 'weekchart' in message and not 'weekpie' in message and not 'agechart' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            schoolID = message.split('weekchart ')[1]
                            log('User '+str(qq)+' call weekchart with schooID '+schoolID)
                            os.system('python weekchart.py --id '+schoolID)
                            if not os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekchart.png'):
                                log('Failed to generate weekchart with the ID of '+schoolID)
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate weekchart with the ID of '+schoolID})
                            if os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekchart.png'):
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=weekchart.png]'.format(qq)})
                                log('Send weekchart complete')
                                message = ['']
                                time.sleep(5)
                                os.system('del C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekchart.png')
                                log('Deleting weekchart.png')
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'weekpie' in message and not 'weekchart' in message and not 'agechart' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            date = message.split('weekpie ')[1]
                            log('User '+str(qq)+' call weekpie with time '+date)
                            os.system('python weekpie.py --time '+date)
                            if not os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekpie.png'):
                                log('Failed to generate weekpie with the time of '+date)
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate weekpie with the time of '+date})
                            if os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekpie.png'):
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=weekpie.png]'.format(qq)})
                                log('Send weekpie complete')
                                message = ['']
                                time.sleep(5)
                                os.system('del C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\weekpie.png')
                                log('Deleting weekpie.png')
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'agechart' in message and not 'weekchart' in message and not 'weekpie' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            log('User '+str(qq)+' call agechart')
                            os.system('python agechart.py')
                            if not os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\agechart.png'):
                                log('Failed to generate agechart')
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate agechart'})
                            if os.path.exists('C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\agechart.png'):
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=agechart.png]'.format(qq)})
                                log('Send agechart complete')
                                message = ['']
                                time.sleep(5)
                                os.system('del C:\\Users\\lemon\\Desktop\\HuayuChatting-bot\\bot\\data\\images\\agechart.png')
                                log('Deleting agechart.png')
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            echo = message.split('echo ')[1]
                            log('User '+str(qq)+' use echo: "'+echo+'"')
                            send_msg({'msg_type': 'group', 'number': group, 'msg': echo})
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'esu' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            schooID = message.split('esu ')[1]
                            if schooID == "24885":
                                log('User '+str(qq)+' use esu to '+str(schooID)+' with img')
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:image,file='+esu(24885)+']'.format(qq)})
                            else:
                                log('User '+str(qq)+' use esu to '+str(schooID)+' but failed')
                                send_msg({'msg_type': 'group', 'number': group, 'msg': 'Failed to esu '+schooID+'. errcode: esu this person is useless'})
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'os._exit()' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if str(qq)=="173887664":
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Bot exit with status 0'})
                                log("Bot exit due to exit command")
                                os._exit(0)
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                        time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'batch' in message:
                        if i==2:
                            qq = rev['sender']['user_id']
                            group = rev['group_id']
                            if str(qq)=="173887664" or str(qq)=="2673895667":
                                job = message.split('batch ')[1]
                                batcho = subprocess.getstatusoutput(job)[1]
                                send_msg({'msg_type': 'group', 'number': group, 'msg': batcho})
                                log('Admin issued '+job+" with output "+batcho)
                            else:
                                log("User "+str(qq)+" issue "+job+" failed due to permission denied")
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                        i=i+1
                        if i==3:
                            i=0
                    elif 'check' in message:
                        if i==2:
                            log('Check!')
                        i=i+1
                        if i==3:
                            i=0
                    else:
                        if i==2:
                            if str(qq)=="173887664" or str(qq)=="2673895667":
                                job = message.split('[CQ:at,qq=3311599537] ')[1]
                                batcho = subprocess.getstatusoutput(job)[1]
                                send_msg({'msg_type': 'group', 'number': group, 'msg': batcho})
                                log('Admin issued '+job+" with output "+batcho)
                            else:
                                qq = rev['sender']['user_id']
                                group = rev['group_id']
                                com = message.split('[CQ:at,qq=3311599537] ')[1]
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Unknown command: '+com})
                                log('User '+str(qq)+' send UNKNOWN command: "'+com+'"')
                        i=i+1
                        if i==3:
                            i=0
    except KeyboardInterrupt:
        log('Bot exit due to user interrupt')
        os._exit(0)
    except:
        print('Unknown Error occured with traceback: '+traceback.format_exc())
        log('Unknown Error occured')
        continue