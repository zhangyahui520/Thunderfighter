#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : scoreboard.py
    Author      : Charles zhang
    Created date: 2020/6/7 14:31
    Description :
       
"""
import pygame.font


class Scoreboard:
    '''显示得分信息的类'''

    def __init__(self, setting, screen, stats):
        '''初始化得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 设置得分的字体设置
        self.text_color = (255, 0, 0)  # 设置字体颜色
        self.font = pygame.font.SysFont('SimHei', 40)  # 设置字体大小

        # 初始化得分图像
        self.prep_score()
        # 初始化最高得分图像
        self.prep_high_score()

    def prep_score(self):
        '''将得分转为图像'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 将得分放到屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 与右边差20px
        self.score_rect.top = 20  # 与上面差20px

    def prep_high_score(self):
        '''将最高得分转化为图像'''
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # 将最高得分放在屏幕中间顶部
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10


    def show_score(self):
        '''在屏幕显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        # 显示最高分
        self.screen.blit(self.high_score_image, self.high_score_rect)
