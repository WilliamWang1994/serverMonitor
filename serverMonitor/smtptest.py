#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send():
    my_sender = 'wangchenglong@edoctordata.cn'
    my_pass = '***********'
    my_user = 'wangchenglong@edoctordata.cn','tangpeizheng@edoctordata.cn'  #收件人邮箱
    msg=MIMEMultipart()
    att = MIMEText(open('eggs.csv', 'r').read(),'base64', 'utf-8')
    msg['From'] = Header("chenglong",'utf-8')  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = Header("tang", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = Header("server monitor",'utf-8')  # 邮件的主题，也可以说是标题
    msg.attach(MIMEText('csv', 'plain', 'utf-8'))
    att["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="eggs.csv"'
    msg.attach(att)
    try:
        server = smtplib.SMTP()
        server.connect("smtp.edoctordata.cn",25)
        server.set_debuglevel(1)
        server.ehlo
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("successf")
        count=1
    except smtplib.SMTPException:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
           print("fail")
           count=0
    if count==1:
       with open('eggs.csv', 'w') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow({"  "})

if __name__ == '__main__':
    send()
