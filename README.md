# drcom-pt-client
Drcom Pt version client with refresh timer<br>
<br>
Dr.com Pt版本客户端 可用于网页认证的drcom

# 使用方法
在程序相同目录下创建dracc.txt并在内部填入三行数据<br>
第一行填入帐号<br>
第二行填入密码<br>
第三行填入认证服务器IP<br>

实例亦可见dracc-example.txt<br>
例：如你的帐号为123456,密码为88888888,认证服务器IP地址为172.31.255.255,则dracc.txt应是<br>
`123456`<br>
`88888888`<br>
`172.31.255.255`<br>

dcacc.txt创建后即可运行<br>
exe版双击运行，因使用pyinstaller -w选项故运行时不会有界面显示<br>
py版需要python3解释器及requests库，你可能需要`pip install requests`<br>
该脚本定时自动更新以大幅降低断网概率

# SZUer看这里
2022新宿舍区IP 172.30.255.42
