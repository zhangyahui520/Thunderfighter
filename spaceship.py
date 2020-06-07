#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.

    Editor      : PyCharm
    File name   : spacheship.py
    Author      : Charles zhang
    Created date: 2020/6/7 14:31
    Description :

"""
from pygame.sprite import Sprite


class Spaceship(Sprite):
    '''表示飞船的类'''

    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        # 添加飞船图像
        self.img = setting.spaceship_img
        # 获取rect属性
        self.rect = self.img.get_rect()

        # 每个飞船最初都在屏幕左上角附近
        self.rect.x = self.rect.width  # 飞船图像的左边距等于图像的宽度

        self.rect.y = self.rect.height  # 飞船图书的上边距等于图像的高度

        self.rect.w = self.rect.width
        self.rect.h = int(self.rect.height / 2)  # 将高度设置为一半

        self.x = float(self.rect.x)

    def blitme(self):
        # 绘制飞船图像
        self.screen.blit(self.img, self.rect)

    def check_edges(self):
        '''如果飞船位于屏幕边缘， 就返回true'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''移动飞船，通过spaceship_direction控制方向'''
        self.x += (self.setting.spaceship_speed * self.setting.spaceship_direction)
        self.rect.x = self.x
