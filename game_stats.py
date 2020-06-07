#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : game_stats.py
    Author      : Charles zhang
    Created date: 2020/6/7 11:04
    Description :
       
"""


class GameStats:
    '''跟踪统计游戏信息'''

    def __init__(self, setting):
        self.setting = setting
        self.reset_stats()
        self.game_active = False

        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        # 初始化在游戏运行期间可能发生变化的统计信息
        self.planes_left = self.setting.plane_limit

        # 统计得分
        self.score = 0
