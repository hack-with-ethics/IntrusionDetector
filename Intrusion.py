#!/bin/bash/python3
#***********************
#Author:Mr.Whitehat
#Date:15-8-2023
#Last-Modified:15-8-2023
#***********************
#Intrusion_Detection
import socket

import time

import smtplib

import datetime

import sys
#[May use Threadin Also]
#[Import Statement]
def Is_Computer_Online():
    #[Info]IF The Computer is Online 
    host = "google.com"
    #[Info]Default Host And port This May [Bypass Firewall] Or Allow This Through Firewall
    port = 443

    try:
        #[Socket Connection]
        s = socket.create_connection((host,port))
        #Return True
        return True
    except:
        #Return False
        return False
def Send_Mail(sm,Rm,msg1,time):
    #[Send_Mail Through Gmail Host Through Transport Layer Security Or SSl ]
    server = smtplib.SMTP("smtp.gmail.com",587)
    passwd = "" #[FiLL this With the App Password For Gmail]
    #[Passwd For The Email Sender]
    server.starttls()
    #[Starting Tls() Connection]
    server.login(sm,passwd)
    #[Login Connection] Smtp
    msg = f"Subject:{msg1}\n\nTime:{time}"
    
    server.sendmail(sm,Rm,msg)
    #[Bingo !!]

while True:
    #Infitely Run BackGround
    if Is_Computer_Online():
        #Run The snippet If the Function Is True
        time = datetime.datetime.now()
        #[Date]Current Date
        cur=time.strftime("%H:%M:%S %D-%M-%Y")
        #[Formating The Date]
        message = "Intrusion Detected"
        sender_mail=""
        Receiver_mail=""
        try:
            Send_Mail(sender_mail,Receiver_mail,message,cur)
        except:
            continue
        sys.exit()
    else:
        #If False
        
        time.sleep(10)
        #Sleep[10]
        continue 
#[Warning:]If The Mail is Send Then the Loop Will BReak
    
