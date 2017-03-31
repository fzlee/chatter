#!/usr/bin/env python
# coding: utf-8
"""
    wechat.py
    ~~~~~~~~~~

"""
import itchat


@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
