# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import requests

WEB_HOOK = ""


class Alert:
    def __init__(self):
        self.hook = WEB_HOOK
        self.header = {
            'Content-Type': 'application/json; charset=utf-8',
        }

    def send_text(self, msg):
        """
        钉钉发送文本消息
        :param msg:
        :return:
        """
        data = {'msgtype': "text"}
        if self._is_text_null(msg):
            data['text'] = {'content': msg}
        else:
            raise ValueError("消息不能为空")

    def send_picture(self, msg, path):
        pass

    def _is_text_null(self, msg):
        if not msg:
            return False
        else:
            return True

    def _ding_post(self, data):
        try:
            requests.post(self.hook, headers=self.header, json=data)
        except Exception as e:
            print("dingding报警消息发送失败，请检查", e)


