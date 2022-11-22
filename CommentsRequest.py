#!/usr/bin/env python3

import requests

cookies = {'PHPSESSID':'kf0hsfv9d8ja33a2r3b2emc377', 'security':'impossible'} 

url='http://127.0.0.1/DVWA/vulnerabilities/xss_s/' 

form_input = open("/home/student/Desktop/scripts/keyboard_Input.txt") 
form_send = form_input.read() 
form_data = {'txtName':'Test IT', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}   
r = requests.post(url, cookies=cookies, data=form_data) 

 
