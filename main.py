#!/usr/bin/env python
# coding: utf-8
"""
    main.py
    ~~~~~~~~~~

"""
from wechat import itchat
from robot import robot


@itchat.msg_register([itchat.content.TEXT, itchat.content.MAP, itchat.content.CARD,
                      itchat.content.NOTE, itchat.content.SHARING])
def text_reply(msg):
    response = robot.get_response(msg["Text"])
    itchat.send(str(response), msg["FromUserName"])

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(True)
