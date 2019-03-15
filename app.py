#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-q','--question',help='Use one argument and keyword',type=int)
args=parser.parse_args()

f = open('access.log','r')
ip_list=[] # Stores unique ip's.
chrome_version_list=[] # Stores unique chrome versions.
bot_path_list=[]
status_code_list=[] # Stores unique status codes.

for line in f: # loop for each access.
    ip = line.split(' -')[0] # ip parsing

    if ip not in ip_list: # Adding each unique
        ip_list.append(ip) # ip to list.

    # Finds each one chrome version and adds in to list.
    if 'Chrome' in line:
        chrome_version=line.rsplit('Chrome/')[-1].split(' ')[0]
        if chrome_version not in chrome_version_list:
            chrome_version_list.append(chrome_version)

    request_type=line.rsplit('''] ''')[-1].split(' ')[0] # Selects each req type('Get', 'Post',etc)

    # Add paths into the list.
    if ' 403 ' in line:
        if 'bot' in line:
            bot_path_list.append(line.rsplit(request_type)[-1].split(''' HTTP''')[0])

    # Selects status codes and adds into the list.
    status_code=line.rsplit('''" ''')[1].split(' ')[0]
    if status_code not in status_code_list:
        status_code_list.append(status_code)
    
if args.question== 1:
    print(len(ip_list)) # Prints how many differnt ip access to site.

elif args.question==2:
    # Prints highest and lowest chrome versions.
    print('En Yuksek: {}\nEn Dusuk: {}'.format(max(chrome_version_list),min(chrome_version_list)))

elif args.question==3:
    # Checks if paths exist.
    if (len(bot_path_list)==0):
        print('There is no path.')
    # If exist then prints paths.
    else:
        for path in bot_path_list:
            print(path,'\n')

elif args.question==4:
    # Prints each status codes and how many times exist.
    for status_code in status_code_list:
        f = open('access.log','r')
        count=0
        for line in f:
            if status_code in line:
                count+=1
        print(int(status_code),count,'\n')