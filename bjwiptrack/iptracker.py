
import argparse
import requests, json
import sys
from sys import argv
import os
import time


parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

print (red+"""
.__________________________________    _____  _________  ____  __._____________________ 
|   \______   \__    ___/\______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \
|   ||     ___/ |    |    |       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/
|   ||    |     |    |    |    |   \/    |    \     \___|    |  \  |        \ |    |   \
|___||____|     |____|    |____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  /
                                 \/         \/        \/        \/        \/         \/                                                       
"""+red)

print("""Welcome to IpTracker would you like to start the tool
        [1] start
        [99] quit 
""")

starttool = input("Enter your choice: ")

if starttool == "1":
        print("starting tool")
        time.sleep(1)


if starttool == "99":
        print("exiting")
        time.sleep(1)
        exit()
        
if starttool == "":
        print('ERROR')
        time.sleep(1)
        exit()



ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print(red+"<--------------->"+red)
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print(red+"<--------------->"+red)
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
