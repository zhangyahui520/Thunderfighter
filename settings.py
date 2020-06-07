#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.

    Editor      : PyCharm
    File name   : setting.py
    Author      : Charles zhang
    Created date: 2020/6/7 14:31
    Description :

"""
import pygame


class Settings:
    '''存储雷霆战机的所有设置'''

    def __init__(self):
        # 游戏的设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_img = pygame.image.load('./img/bgimg4.jpg')  # 相对路径
        self.title = '雷霆战机'

        # 飞机的设置
        self.plane_limit = 3  # 飞机的生命值
        self.plane_img = pygame.image.load('./img/plane1_mini.png')

        # 子弹的设置

        self.bullet_width = 3  # 子弹的宽
        self.bullet_height = 15  # 子弹的高
        self.bullet_color = (255, 255, 255)  # 子弹的颜色
        self.bullet_allowed = 5  # 限制子弹的数量

        # 飞船的设置
        self.spaceship_img = pygame.image.load("./img/spaceship1_mini.png")
        self.spaceship_drop_speed = 10  # 飞船下降的速度

        # 游戏升级设置
        self.speedup_scale = 1.2  # 游戏难度增加的系统
        self.score_scale = 1.5  # 提高分数增加速度
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''设置跟动态有关的参数'''
        self.plane_speed = 2.5  # 控制飞机的移动速度
        self.bullet_speed = 3  # 子弹的速度
        self.spaceship_speed = 1  # 飞船的速度
        # 标志位， 1表示右移， -1表示左移
        self.spaceship_direction = 1  # 默认右移

        self.spaceship_points = 10  # 击落一个飞船得分

    def increase_speed(self):
        '''提高游戏节奏'''
        self.plane_speed *= self.speedup_scale  # 增加飞机速度
        self.bullet_speed *= self.speedup_scale  # 增加子弹速度
        self.spaceship_speed *= self.speedup_scale  # 增加飞船的速度

        self.spaceship_points = int(self.spaceship_points * self.score_scale)  # 增加飞船的得分
