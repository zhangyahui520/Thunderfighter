#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : buttom.py
    Author      : Charles zhang
    Created date: 2020/6/7 12:16
    Description :
       
"""
import pygame.font


class Button:
    def __init__(self, setting, screen, msg):
        '''初始化按钮的属性'''

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的大小
        self.width = 200
        self.height = 20

        self.button_color = (0, 255, 0)  # 按钮的颜色
        self.text_color = (200, 200, 200)  # 文字的颜色
        self.font = pygame.font.SysFont('SimHei', 48)  # 字体为黑体大小为48PX


        # 创建按钮的rect对象， 并居中
        self.rect = pygame.Rect((0, 0, self.width, self.height))
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    # 将msg渲染成图像
    def prep_msg(self, msg):
        '''
        font.reder方法是将msg中的文本转换为图像
        * 参数True是开启抗锯齿模式
        * self.text_color是文本的颜色
        * self.button_color是背景颜色
        :param msg:
        :return:
        '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # 使其在按钮上居中
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 绘制按钮
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)  # 用一个填充按钮
        self.screen.blit(self.msg_image, self.msg_image_rect)  # 绘制文本
