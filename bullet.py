# 创建存储子弹的Bullet类

import pygame
from pygame.sprite import Sprite

# 继承pygame.sprite 的 sprite类,此类可以将游戏中的元素进行编组，可以同时操作编组中的所有元素
class Bullet(Sprite):
    '''子弹的管理'''

    def __init__(self, setting, screen, plane):
        super.__init__()
        self.screen = screen

        # pygame.Rect 用于存储直角坐标的pygame对象
        self.rect = pygame.Rect(0,0,setting.bullet_width, setting.bullet_height) #在（0,0）出创建一个子弹的矩形

        # 让子弹的位置跟小飞机重叠，当子弹飞出去以后，就显得跟从飞机里面射出来一样
        self.rect.centerx = plane.rect.centerx # 设置显示的位置
        self.rect.top = plane.rect.top

        # 将子弹的坐标转为浮点数
        self.y = float(self.rect.y)

        # 设置子弹的颜色和速度
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed

    # 控制子弹的移动
    def update(self):
        self.y = self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        # pygame.draw.rect() 画一个矩形
        pygame.draw.rect(self.screen, self.color, self.rect)
