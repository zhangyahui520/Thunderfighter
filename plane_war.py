import pygame
from pygame.sprite import Group

import sys  # 用于退出游戏
from settings import Settings
from plane import Plane
import game_func as gf
from spaceship import Spaceship





def run_game():
    # 初始化游戏
    pygame.init()
    setting = Settings()
    # 设置屏幕分辨率
    screen = pygame.display.set_mode((setting.screen_width, setting.height))  # 大小为1000px * 600px
    # 设置标题
    pygame.display.set_caption(setting.title)  # 标题

    # 打印其类型
    print(type(screen))  # <class 'pygame.Surface'>

    plane = Plane(screen, setting)  # 创建战机
    bullets = Group()  # 创建一个存储子弹的编组
    spaceship = Spaceship(setting, screen) # 创建飞船

    # 开始游戏的主循环
    while True:

        # 不关闭窗口
        gf.check_events(plane, setting, screen, bullets)

        plane.update() # 控制飞机移动
        gf.update_bullets(bullets) # 控制子弹飞行
        print(len(bullets))  # 用于测试子弹是否删除

        gf.update_screen(screen, setting.bg_img, plane, bullets)



if __name__ == '__main__':
    run_game()
