#!/usr/bin/env python
# coding: utf-8
"""
    main.py
    ~~~~~~~~~~

"""
import config
from wechat import itchat
from robot import robot


@itchat.msg_register([itchat.content.TEXT, itchat.content.MAP, itchat.content.CARD,
                      itchat.content.NOTE, itchat.content.SHARING])
def text_reply(msg):
    response = robot.get_response(msg["Text"])
    itchat.send(str(response), msg["FromUserName"])


@itchat.msg_register([itchat.content.TEXT, itchat.content.MAP, itchat.content.CARD,
                      itchat.content.NOTE, itchat.content.SHARING], isGroupChat=True)
def group_text_reply(msg):
    """
    group response:

    """
    response = msg["Text"]

    # 如果是@一个人的，将@的内容取消
    if response.startswith("@") and "\u2005" in response:
        content = response.split("\u2005")[-1]
    else:
        content = response

    reply = robot.get_response(content)
    # 如果是@我们机器人，则回复一段数据
    if response.startswith("@{}\u2005".format(config.robot_name)):
        reply = "@{}\u2005{}".format(msg["ActualNickName"], reply)
        itchat.send(str(reply), msg["FromUserName"])


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(debug=config.verbose)
