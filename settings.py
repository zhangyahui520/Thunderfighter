import pygame


class Settings:
    '''存储雷霆战机的所有设置'''

    def __init__(self):
        self.screen_width = 1000
        self.screent_height = 600

        self.bg_img = pygame.image.load('')  # 相对路径
        self.title = '雷霆战机'

        self.plane_speed = 2.5  # 控制飞机的移动速度

        # 子弹的设置
        self.bullet_speed = 3  # 速度
        self.bullet_width = 3  # 子弹的宽
        self.bullet_height = 15  # 子弹的高
        self.bullet_color = (100, 100, 100)  # 子弹的颜色
        self.bullet_allowed = 5 # 限制子弹的数量