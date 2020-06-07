#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.

    Editor      : PyCharm
    File name   : plane.py
    Author      : Charles zhang
    Created date: 2020/6/7 11:04
    Description :

"""


class Plane:
    def __init__(self, screen, setting):
        # 初始化小飞机并设置其初始位置
        self.screen = screen
        self.setting = setting

        self.img_plane = setting.plane_img  # 得到小飞机的图像
        self.rect = self.img_plane.get_rect()  # 得到小飞机的矩形区域
        self.screen_rect = self.screen.get_rect()  # 得到screen的矩形区域

        # get_rect会返回Surface的矩形的区域，.centerx和.bottom是其两个属性

        # 将小飞机放到底部中央
        self.rect.centerx = self.screen_rect.centerx  # 水平居中
        self.rect.bottom = self.screen_rect.bottom  # 底部

        # 标志位
        self.mv_right = False
        self.mv_left = False

    def blitme(self):
        # 在指定位置绘制小飞机
        self.screen.blit(self.img_plane, self.rect)

    # 定义一个调整战机位置的方法
    def update(self):
        '''根据标志位来调整战机的位置'''
        screen_rect = self.screen.get_rect()
        if self.mv_right and self.rect.right <= screen_rect.right:  # 当未接触到边缘时，允许移动
            self.rect.centerx += self.setting.plane_speed

        if self.mv_left and self.rect.left >= 0:
            self.rect.centerx -= self.setting.plane_speed

    # 让战机居中
    def center_plane(self):
        self.rect.centerx = self.screen_rect.centerx
