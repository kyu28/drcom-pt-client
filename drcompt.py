#drcom Pt compatible client
import urllib.request
import time
import sys
import os

def Connect(url):
  try:
    res=urllib.request.urlopen(portalUrl)
    print(res.read().decode('utf-8'))
  except:
    print("Connection error")

version='1.0'
configFile='account.cfg'

if os.path.exists(configFile):
  f=open(configFile,'r')
  user=f.readline()
  password=f.readline()
  ip=f.readline()
  interval=int(f.readline())
  portalUrl='http://'+ip[0:-1]+':801/eportal/portal/login?user_account=%2C0%2C'+user[0:-1]+'&user_password='+password[0:-1]
  f.close()
  print('Drcom Pt compatible client '+version)
  while True:
    Connect(portalUrl)
    time.sleep(interval)
else:
  print('Config file not found')
  print('Set your user account and password in "'+os.getcwd()+'\\'+configFile+'"')
  print('\nFor example, if your account is 123456, password is 88888888, you need to access 172.31.255.255 to get online and you want it refreshes every 30s')
  print('Your config file should look like this:\n')
  print('123456\n88888888\n172.31.255.255\n30')
