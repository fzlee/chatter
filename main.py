#!/usr/bin/env python
# coding: utf-8
"""
    main.py
    ~~~~~~~~~~

"""
import config
from wechat import itchat
from robot import robot


@itchat.msg_register([itchat.content.TEXT])
def text_reply(msg):
    response = robot.get_response(msg["Text"])
    itchat.send(str(response), msg["FromUserName"])


@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def group_text_reply(msg):
    """
    group response:

    """
    response = msg["Text"]
    import json
    print(json.dumps(msg, indent=2))

    # 如果是@一个人的，将@的内容取消, @nickname 后面或者是空格，或者是\u2005
    if response.startswith("@"):
        if "\u2005" in response:
            content = response.split("\u2005")[-1]
        else:
            content = response.split(" ", 1)[-1]
    else:
        content = response

    reply = robot.get_response(content)
    # 如果是@我们机器人，则回复一段数据
    if response.startswith("@{}".format(config.robot_name)):
        reply = "@{}\u2005{}".format(msg["ActualNickName"], reply)
        itchat.send(str(reply), msg["FromUserName"])


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run(debug=config.verbose)
