# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from util.alert import Alert


class EmailUtil:
    def __init__(self):
        self.alert = Alert()
        self.sender = "1589369708@qq.com"
        self.receiver = "qing.li@moji.com, 13263106808@163.com"
        self.server = "smtp.qq.com"
        self.username = "1589369708@qq.com"
        # 使用的是token不是password
        self.password = "fbgsrzbjtxlgffag"
        self.mail_title = "接口自动化测试报告"

    def send_email(self, path):
        # 打开文件
        with open(path, 'rb') as f:
            content = f.read()
        message = MIMEText(content, 'html', 'utf-8')
        message["From"] = self.sender
        message["To"] = self.receiver
        message["Subject"] = Header(self.mail_title, 'tf-8')

        try:
            smtp = smtplib.SMTP_SSL(self.server, 465)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receiver.split(","), message.as_string())
            smtp.quit()
        except smtplib.SMTPException as e:
            # 报警
            self.alert.send_text("邮件发送失败，请检查")