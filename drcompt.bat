set user=123456
set password=88888888
set ip=172.30.255.255
set "portalUrl=http://%ip%:801/eportal/portal/login?user_account=%%2C0%%2C%user%&user_password=%password%"

for /l %%a in (0, 0, 1) do (
  curl "%portalUrl%"
  timeout -nobreak 15
)

