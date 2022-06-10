#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.the_path import path_util


class sendemailutil():



    def sendqq(self,emailpeople,file):     #接收者；附件

        mineemail = '980975647@qq.com' #我的账号
        pwd = 'vcjggwbfxecabfbb'
        now = time.strftime('%Y-%m—%d-%H-%M-%S')


        #主题
        msg = MIMEMultipart()
        msg['Subject'] = now + '测试报告'   #邮件的标题
        msg['From'] = mineemail    #邮件发送者
        msg['To'] = emailpeople    #邮件的接收者


        #文字内容
        count = MIMEText('您好，自动化测试报告，请查阅~~','plain','utf-8')
        msg.attach(count)

        #附件部分
        part =MIMEApplication(open(file,'rb').read())     #打开附件
        part.add_header('content-disposition','attachment',filename=file) #添加头部信息
        msg.attach(part)

        #多个附件
        # path = ['附件地址1','附件地址2']
        # for item in path:
        #     part =MIMEApplication(open(item,'rb').read())     #打开附件
        #     part.add_header('content-disposition','attachment',filename=file) #添加头部信息
        #     msg.attach(part)

        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", timeout=25)  # 连接SMTP邮件服务，默认端口是25
            s.login(mineemail, pwd)  # 登录服务器
            s.sendmail(mineemail, emailpeople, msg.as_string())  # 发送邮件
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")



if __name__ == '__main__':
    sendemailutil().sendqq('980975647@qq.com',path_util().get_path()+'\\123.txt')
    sendemailutil().sendqq('1571754405@qq.com',path_util().get_path()+'\\123.txt')
    # sendemailutil().sendqq("980975647@qq.com",r"C:\Users\Administrator\PycharmProjects\test\123.txt")
    # sendemailutil().sendqq("1571754405@qq.com",r"C:\Users\Administrator\PycharmProjects\test\123.txt")
    print("配置文件调试成功")








