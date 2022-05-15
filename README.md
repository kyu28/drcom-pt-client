# drcom-pt-client
Drcom Pt version client with refresh timer<br>
<br>
Dr.com Pt版本客户端 可用于网页认证的drcom

# Python版使用方法  
在程序相同目录下创建account.cfg并填入四行数据<br>
第一行填入帐号<br>
第二行填入密码<br>
第三行填入认证服务器IP<br>
第四行填入刷新时间  

实例亦可见account.cfg.example<br>
例：如你的帐号为123456，密码为88888888，认证服务器IP地址为172.31.255.255，每60秒刷新一次，则account.cfg应是<br>
```
123456
88888888
172.31.255.255
60
````

account.cfg创建后即可运行  
exe版双击运行，drcom将显示详细信息，drcomq将静默运行  
该脚本定时自动更新以大幅降低断网概率  

# 脚本版使用方法  
Linux/Mac OS X/Unix修改`drcompt.sh`，Windows修改`drcompt.bat`中user账号、password密码、ip认证服务器IP字段并保存，再运行脚本  

# SZUer看这里
2022新宿舍区IP 172.30.255.42
