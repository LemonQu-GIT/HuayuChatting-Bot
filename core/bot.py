#encoding=utf-8
from receive import rev_msg
from send import send_msg
from hyxq import log, esu, findImgURL, Download_Image, checkgroup, searchHuayuWiki, getConfig
import os, socket, socket, requests, random, time, traceback, subprocess, shutil

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
                if "[CQ:at,qq="+str(getConfig("botQID"))+" in message:
                    qq = rev['sender']['user_id']
                    group = rev['group_id']
                    if 'weekchart' in message and not 'weekpie' in message and not 'agechart' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if not checkgroup(qq) == "Ban":
                                schoolID = message.split('weekchart ')[1]
                                log('User '+str(qq)+' call weekchart with schooID '+schoolID)
                                os.system('python weekchart.py --id '+schoolID)
                                if not os.path.exists(getConfig('go-cqhttp_image_path')+'\\weekchart.png'):
                                    log('Failed to generate weekchart with the ID of '+schoolID)
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate weekchart with the ID of '+schoolID})
                                if os.path.exists(getConfig('go-cqhttp_image_path')+'\\weekchart.png'):
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=weekchart.png]'.format(qq)})
                                    log('Send weekchart complete')
                                    message = ['']
                                    time.sleep(5)
                                    os.system('del '+getConfig('go-cqhttp_image_path')+'\\weekchart.png')
                                    log('Deleting weekchart.png')
                                time.sleep(5)
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                        i=i+1
                        if i==3:
                            i=0
                        
                    elif 'weekpie' in message and not 'weekchart' in message and not 'agechart' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if not checkgroup(qq) == "Ban":
                                date = message.split('weekpie ')[1]
                                log('User '+str(qq)+' call weekpie with time '+date)
                                os.system('python weekpie.py --time '+date)
                                if not os.path.exists(getConfig('go-cqhttp_image_path')+'\\weekpie.png'):
                                    log('Failed to generate weekpie with the time of '+date)
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate weekpie with the time of '+date})
                                if os.path.exists(getConfig('go-cqhttp_image_path')+'\\weekpie.png'):
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=weekpie.png]'.format(qq)})
                                    log('Send weekpie complete')
                                    message = ['']
                                    time.sleep(5)
                                    os.system('del '+getConfig('go-cqhttp_image_path')+'\\weekpie.png')
                                    log('Deleting weekpie.png')
                                time.sleep(5)
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                        i=i+1
                        if i==3:
                            i=0
                        
                    elif 'agechart' in message and not 'weekchart' in message and not 'weekpie' in message and not 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if not checkgroup(qq) == "Ban":
                                log('User '+str(qq)+' call agechart')
                                os.system('python agechart.py')
                                if not os.path.exists(getConfig('go-cqhttp_image_path')+'\\agechart.png'):
                                    log('Failed to generate agechart')
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Failed to generate agechart'})
                                if os.path.exists(getConfig('go-cqhttp_image_path')+'\\agechart.png'):
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'[CQ:image,file=agechart.png]'.format(qq)})
                                    log('Send agechart complete')
                                    message = ['']
                                    time.sleep(5)
                                    os.system('del '+getConfig('go-cqhttp_image_path')+'\\agechart.png')
                                    log('Deleting agechart.png')
                                time.sleep(5)
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                        i=i+1
                        if i==3:
                            i=0
                        
                    elif 'echo' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if not checkgroup(qq) == "Ban":
                                echo = message.split('echo ')[1]
                                log('User '+str(qq)+' use echo: "'+echo+'"')
                                send_msg({'msg_type': 'group', 'number': group, 'msg': echo})
                                time.sleep(5)
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                        i=i+1
                        if i==3:
                            i=0
                        
                    elif 'esu' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if not checkgroup(qq) == "Ban":
                                schooID = message.split('esu ')[1]
                                if schooID == "24885":
                                    log('User '+str(qq)+' use esu to '+str(schooID)+' with img')
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:image,file='+esu(24885)+']'.format(qq)})
                                else:
                                    log('User '+str(qq)+' use esu to '+str(schooID)+' but failed')
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'Failed to esu '+schooID+'. errcode: esu this person is useless'})
                                time.sleep(5)
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                            
                        i=i+1
                        if i==3:
                            i=0
                        
                    elif 'os._exit()' in message:
                        if checkgroup(qq) == "Admin":
                            qq = rev['sender']['user_id']
                            group = rev['group_id']
                            if i==2:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Bot exit with status 0'})
                                log("Bot exit due to exit command")
                                os._exit(0)
                            time.sleep(5)
                            i=i+1
                            if i==3:
                                i=0
                        elif checkgroup(qq)=="Bot":
                            log('Bot filter triggered')
                            continue
                        else:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                    elif 'batch' in message:
                        qq = rev['sender']['user_id']
                        group = rev['group_id']
                        if i==2:
                            if checkgroup(qq) == "Admin":
                                job = message.split('batch ')[1]
                                batcho = subprocess.getstatusoutput(job)[1]
                                if not batcho=="":
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': batcho})
                                    log('Admin issued '+job+" with output "+batcho)
                                else:
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': "Command issued without output"})
                                    log('Admin issued '+job+" without output")
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                log("User "+str(qq)+" issue "+job+" failed due to permission denied")
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                        i=i+1
                        if i==3:
                            i=0
                    elif 'checkgroup' in message:
                            if i==2:
                                qq = rev['sender']['user_id']
                                group = rev['group_id']
                                log('Check!')
                                if not checkgroup(qq)=="Bot":
                                    if checkgroup(qq)=="Admin":
                                        QQIDC = message.split('checkgroup ')[1]
                                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+QQIDC+' is in group '+checkgroup(int(QQIDC))})
                                    else:
                                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+checkgroup(qq)})
                                else:
                                    log('Bot filter triggered')
                                time.sleep(5)
                            i=i+1
                            if i==3:
                                i=0
                    elif 'yolov5' in message:
                        if i==1:
                            qq = rev['sender']['user_id']
                            group = rev['group_id']
                            if checkgroup(qq) == "Experimental" or checkgroup(qq) == "Admin" :
                                yolov5B = time.perf_counter()
                                imgURL = findImgURL(message)
                                log(str(qq)+' issued yolov5 and the image URL is '+imgURL)
                                Download_Image(downloadUrl=imgURL,saveImagePath="./yolov5_img/")
                                os.system('activate yolov5&&python '+getConfig('yolov5_path')+'\\detect.py --source '+getConfig('QQImgDownload')+' --name yolov5_output --weights C:\\Users\\lemon\\Desktop\\yolov5\\yolov5m6.pt')
                                os.system('copy '+getConfig('yolov5_path')+'\\runs\\detect\\yolov5_output\\0.jpg '+getConfig('go-cqhttp_image_path')+'\\0.jpg')
                                os.system('copy '+getConfig('yolov5_path')+'\\runs\\detect\\yolov5_output2\\0.jpg '+getConfig('go-cqhttp_image_path')+'\\0.jpg')
                                os.system('copy '+getConfig('yolov5_path')+'\\runs\\detect\\yolov5_output3\\0.jpg '+getConfig('go-cqhttp_image_path')+'\\0.jpg')
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:image,file=0.jpg]'.format(qq)})
                                time.sleep(5)
                                shutil.rmtree(getConfig('yolov5_path')+r'\runs\detect\yolov5_output')
                                shutil.rmtree(getConfig('yolov5_path')+r'\runs\detect\yolov5_output2')
                                shutil.rmtree(getConfig('yolov5_path')+r'\runs\detect\yolov5_output3')
                                os.remove(getConfig('QQImgDownload')+'\\0.jpg')
                                os.remove(getConfig('go-cqhttp_image_path')+'\\0.jpg')
                                yolov5L = time.perf_counter()
                                counter = f"All yolov5 task finished in {yolov5L - yolov5B:0.2f} seconds"
                                log(counter)
                                send_msg({'msg_type': 'group', 'number': group, 'msg': counter})
                            else:
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                log(str(qq)+"'s permission denied due to banned")
                            time.sleep(5)
                        i=i+1
                        if i==3:
                            i=0
                    elif 'wiki' in message:
                            if i==2:
                                qq = rev['sender']['user_id']
                                group = rev['group_id']
                                if not checkgroup(qq) == "Ban":
                                    find_item = message.split('wiki ')[1]
                                    log(str(qq)+" search "+str(find_item)+" in huayuwiki")
                                    passage = searchHuayuWiki(find_item)
                                    if len(passage) > 1000:
                                        passage = passage[0:1000]
                                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"The passage is too long to inspect, so we extract the front 1000 characters"})
                                        log(find_item+"'s passage is too long!")
                                        send_msg({'msg_type': 'group', 'number': group, 'msg': passage})
                                    else:
                                        send_msg({'msg_type': 'group', 'number': group, 'msg': passage})
                                        log(find_item+"'s passage has been sent")
                                else:
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+"Permission denied"})
                                    log(str(qq)+"'s permission denied due to banned")
                                time.sleep(5)
                            i=i+1
                            if i==3:
                                i=0
                    else:
                        if i==2:
                            if checkgroup(qq)=="Admin":
                                job = message.split('[CQ:at,qq='+str(getConfig("botQID"))+'] ')[1]
                                batcho = subprocess.getstatusoutput(job)[1]
                                if not batcho=="":
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': batcho})
                                    log('Admin issued '+job+" with output "+batcho)
                                else:
                                    send_msg({'msg_type': 'group', 'number': group, 'msg': "Command issued without output"})
                                    log('Admin issued '+job+" without output")
                            elif checkgroup(qq)=="Bot":
                                log('Bot filter triggered')
                                continue
                            else:
                                qq = rev['sender']['user_id']
                                group = rev['group_id']
                                com = message.split('[CQ:at,qq='+str(getConfig("botQID"))+'] ')[1]
                                send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq='+str(qq)+']'+'Unknown command: '+com})
                                log('User '+str(qq)+' send UNKNOWN command: "'+com+'"')
                            time.sleep(5)
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