
#其中有一个Plane类，来存储飞机的各种行为

import pygame

class Plane:
    def __init__(self, screen, setting):
        # 初始化小飞机并设置其初始位置
        self.screen = screen
        self.setting = setting

        self.img_plane = pygame.image.load(self.setting.plane_img)
        self.rect = self.img_plane.get_rect()   # 得到小飞机的矩形区域
        self.screen_rect = self.screen.get_rect() # 得到screen的矩形区域

        #get_rect会返回Surface的矩形的区域，.centerx和.bottom是其两个属性

        # 将小飞机放到底部中央
        self.rect.centerx = self.screen_rect.centerx #水平居中
        self.rect.bottom = self.screen_rect.bottom #底部

        # 标志位
        self.mv_right = False

    def blitme(self):
        # 在指定位置绘制小飞机
        self.screen.blit(self.img_plane, self.rect)

    # 定义一个调整战机位置的方法
    def update(self):
        '''根据标志位来调整战机的位置'''
        if self.mv_right <= self.setting.screen_width: # 当未接触到边缘时，允许移动
            self.rect.centerx += self.setting.plane_speed

        if self.mv_left >= 0:
            self.rect.centerx -= self.setting.plane_speed