from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,get_user_model
from twilio.rest import Client
from background_task import background
from django.contrib.auth.models import User
from userprofile.models import profile
import datetime

# Web Scraping
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib.request
import requests
import time, os

#My Models
from updated.models import update


URL = os.environ.get("TELEGRAM_URL", "")




from django.core.mail import send_mail,EmailMultiAlternatives
from .settings import EMAIL_HOST_USER

User=get_user_model()




# @background(schedule=900)
# def notify_user(repeat_untill=None):
#     nor=datetime.datetime.now().time().hour
#     nor1=datetime.datetime.now().time().minute
#     nor2=datetime.datetime.now().time().second
#     if nor==0 and nor1==0:
#         user_lst=profile.objects.filter(premium=True)
#         for usr in user_lst:
#             account_sid = usr.sid
#             auth_token = usr.token
#             client = Client(account_sid, auth_token)
#             message = client.messages.create(
#                                       from_='whatsapp:+14155238886',
#                                       body="This is just a reminder message.",
#                                       to='whatsapp:+91'+str(usr.mobile)
#                                   )
#             usr.sent=usr.sent+1
#             usr.save()
#         time.sleep(60)
#     my_url="http://210.212.85.155"
#     bg=0
#     #try:
#     uClient=requests.get(my_url,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'},timeout=10)
#     #except:
#     #	bg=1
#     if bg==0:
#     	pagehtml=uClient.content
#     	#uClient.close()
#     	page_soup=soup(pagehtml,"html.parser")
#     	containers=page_soup.findAll("div",{"class":"col col-7"})
#     else:
#     	containers=[]
#     try:
#     	id_new=int(containers[0]["id"][13:])
#     except:
#     	id_new=-1
#     print(id_new)
#     obj=update.objects.filter(notice='archit')
#     obj=obj.first()
#     if id_new>=int(obj.notice_id):
#     	no=id_new-int(obj.notice_id)
#     	if no>=5:
#     		no=5
#     	user_lst=profile.objects.filter(premium=True)
#     	for i in range(no):
#     		user_lst=profile.objects.filter(premium=True)
#     		for usr in user_lst:
#     			account_sid = usr.sid
#     			auth_token = usr.token
#     			client = Client(account_sid, auth_token)
#     			message = client.messages.create(
# 				                          from_='whatsapp:+14155238886',
# 				                          body="You have Got 1 new Notice on the InfoCenter and that is -\n\n\n*"+" ".join(containers[i].text.split()).capitalize()+"* \n\n\nThanks and Regards\nArchit Kumar Dwevedi ",
# 				                          to='whatsapp:+91'+str(usr.mobile)
# 				                      )
#     			usr.sent=usr.sent+1
#     			usr.save()
#     	obj.notice_id=float(id_new)
#     	obj.save()




#here Starts actual



from telegram.models import telegram_id,telegram_offset
from scraping.bot_reply import bot
import random



def send_Telegram_Message(chat_id,msg):
    my_url=URL+str(chat_id)+"&text="+str(msg)
    # while True:
    try:
        result=requests.get(my_url).json()
        # break
    except:
        # print("here")
        pass
    # print("Done")




# @background(schedule=0)
def get_New_Id():
    #print("GO GO")
    obl=telegram_offset.objects.filter(active=True).first()
    my_url=URL+str(obl.offset + 1)
    result=requests.get(my_url).json()['result']
    length=len(result)
    for i in range(length):
        sent_message=result[i]['message']['text']
        chat_id=int(result[i]['message']['chat']['id'])
        obj=telegram_id.objects.filter(tel_id=chat_id)
        if obj.count()==0:
            obj=telegram_id(tel_id=chat_id)
            obj.save()
        else:
            obj=obj.first()
        # if obj.sub:
        # print("Over")
        if sent_message=='/getNotified' or sent_message=='/getnotified':
            # obj=telegram_id(tel_id=chat_id)

            obj.sub=True
            obj.save()
            msg="""Congratulations ! \n You will be Notified as soon as New Notification comes up.
            \n"""
            send_Telegram_Message(chat_id=chat_id,msg=msg)
        # else:
        #     msg="""Congratulations ! \n You will be Notified as soon as New Notification comes up.
        #     \n"""
        #     send_Telegram_Message(chat_id=chat_id,msg=msg)
        else:
            if sent_message=="help" and not(obj.sub):
                response="""Sorry You are not Subscribed to get Notifications of new Notices of the Infoconnect\n\n
Please send '/getNotified' to get New Notices Updates on Telegram."""
            elif sent_message=="help" and obj.sub:
                response="""Congratulations ! \n You will be Notified as soon as New Notification comes up.
            \n"""
            else:
                response=bot.get_response(sent_message)
                option=random.choice([0,1])
                response=str(response)
                if option:
                    response+="""\n\n\nTo Know more about me send 'help'"""
            send_Telegram_Message(chat_id=chat_id,msg=response)
        obl.offset=int(result[i]['update_id'])
        obl.save()
    # get_New_Id()





@background(schedule=0)
def notify_user(repeat_untill=None):
    #print("herer")
    get_New_Id()
    my_url="http://210.212.85.155"
    bg=0
    #try:
    uClient=requests.get(my_url,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'},timeout=10)
    #except:
    #   bg=1
    if bg==0:
        pagehtml=uClient.content
        #uClient.close()
        page_soup=soup(pagehtml,"html.parser")
        containers=page_soup.findAll("div",{"class":"col col-7"})
    else:
        containers=[]
    try:
        id_new=int(containers[0]["id"][13:])
    except:
        id_new=-1
    # print(id_new)
    obj=update.objects.filter(notice='archit')
    obj=obj.first()
    if id_new>=int(obj.notice_id):
        no=id_new-int(obj.notice_id)
        if no>=5:
            no=5
        user_lst=profile.objects.filter(premium=True)
        for i in range(no):
            user_lst=profile.objects.filter(premium=True)
            # for usr in user_lst:
            # account_sid = "ACb6b53459ccfcc8f01ed12048c29ced69"
            # auth_token = "5088f8375c618f5013f186b4058fcf03"
            # client = Client(account_sid, auth_token)
            # message = client.messages.create(
            #                           from_='whatsapp:+14155238886',
            #                           body="You have Got 1 new Notice on the InfoCenter and that is -\n\n\n*"+" ".join(containers[i].text.split()).capitalize()+"* \n\n\nThanks and Regards\nArchit Kumar Dwevedi ",
            #                           to='whatsapp:+917052093141'
            #                       )
            # usr.sent=usr.sent+1
            # usr.save()
            print("sent")
            # from_email=EMAIL_HOST_USER
            # email="dwevediar@gmail.com"
            # email1="psujz5fgti@pomail.net"
            # to_list=[email,email1]
            # subject="New Notice - InfoConnect"
            message="You have Got 1 new Notice on the InfoCenter and that is -\n\n\n"+" ".join(containers[i].text.split()).capitalize()+" \n\n\nThanks and Regards\nArchit Kumar Dwevedi "
            # send_mail(subject,message,from_email,to_list)
            ojh=telegram_id.objects.filter(sub=True)
            for klj in ojh:
                send_Telegram_Message(chat_id=klj.tel_id,msg=message)
        obj.notice_id=float(id_new)
        obj.save()
        count=0
        while count!=1800:
            time.sleep(1)
            get_New_Id()
            count+=1
        # print("Slept")
    notify_user()

# #
# print("Go")
# notify_user()
# get_New_Id()


def index(request):
	return render(request, "index.html",{})


def congo(request):
	return render(request,"congo.html",{})
