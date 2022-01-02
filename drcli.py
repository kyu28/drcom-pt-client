#drcom 5.2.0(Pt) compatible client for Windows
import requests
import time
import sys
import os

def Connect(url):
  try:
    res=requests.post(url=portalUrl,timeout=30)
    res.raise_for_status()
    print(res.text)
  except:
    print("Connection error")

configFileName='dcacc.txt'
configFile=os.getcwd()+'\\'+configFileName

if os.path.exists(configFile):
  f=open(configFile,'r')
  user=f.readline()
  password=f.readline()
  ip=f.readline()
  portalUrl='http://'+ip[0:-1]+':801/eportal/portal/login?user_account=%2C0%2C'+user[0:-1]+'&user_password='+password[0:-1]
  f.close()
  while True:
    Connect(portalUrl)
    time.sleep(60)
else:
  print('Config file not found')
  print('Give your user account and password in "'+configFile+'" in this format:')
  print('(First line your user account)')
  print('(Second line your password)')
  print('(Third line Dr.com eportal IP address)')
  print('\nFor example, if your account is 123456, password is 88888888 and you need to access 172.31.255.255 to get online')
  print('Your config file should look like this:\n')
  print('123456\n88888888\n172.31.255.255')
