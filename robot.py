#!/usr/bin/env python
# coding: utf-8
"""
    robot.py
    ~~~~~~~~~~

"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

robot = ChatBot("robot")
robot.set_trainer(ChatterBotCorpusTrainer)
robot.train("chatterbot.corpus.chinese")  # 语料库
