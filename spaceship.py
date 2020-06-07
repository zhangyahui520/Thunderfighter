"""
-*- coding:uft-8 -*-
author: 小甜
date:2020/6/4
"""
import pygame
from pygame.sprite import Sprite


class Spaceship(Sprite):
    '''表示飞船的类'''

    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        # 添加飞船图像
        self.img = pygame.image.load("./imgs/enemy.png")
        # 获取rect属性
        self.rect = self.img.get_rect()

        # 每个飞船最初都在屏幕左上角附近
        self.rect.x = self.rect.width  # 飞船图像的左边距等于图像的宽度

        self.rect.y = self.rect.height  # 飞船图书的上边距等于图像的高度

        self.x = float(self.rect.x)

    def blitme(self):
        # 绘制飞船图像
        self.screen.blit(self.img, self.rect)
