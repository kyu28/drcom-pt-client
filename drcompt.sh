#!/bin/sh

user=123456
password=88888888
ip=172.30.255.255
portalUrl='http://'$ip':801/eportal/portal/login?user_account=%2C0%2C'$user'&user_password='$password

while true; do
  wget -O - "$portalUrl"
  sleep 15
done
