#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.

    Editor      : PyCharm
    File name   : plane_war.py
    Author      : Charles zhang
    Created date: 2020/6/7 11:04
    Description :

"""
import pygame
from pygame.sprite import Group

import Thunderfighter.game_func as gf
from Thunderfighter.button import Button
from Thunderfighter.plane import Plane
from Thunderfighter.scoreboard import Scoreboard
from Thunderfighter.settings import Settings
from Thunderfighter.game_stats import GameStats


def run_game():
    # 初始化游戏
    pygame.init()
    setting = Settings()
    # 设置屏幕分辨率
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))  # 大小为1000px * 600px
    # 设置标题
    pygame.display.set_caption(setting.title)  # 标题

    # 游戏对象的初始化
    play_button = Button(setting, screen, 'Play')

    stats = GameStats(setting)  # 创建存储游戏统计信息的实例
    score_board = Scoreboard(setting, screen, stats)  # 创建计分板实例
    plane = Plane(screen, setting)  # 创建战机
    bullets = Group()  # 创建一个存储子弹的编组
    spaceships = Group()  # 创建飞船编组

    # 开始游戏的主循环
    while True:
        # 不关闭窗口
        gf.check_events(plane, setting, screen, bullets, stats, play_button, spaceships, score_board)
        if stats.game_active:  # 根据游戏状态来判断是否需要创建其图像
            # 更新战机的位置
            plane.update()
            # 更新子弹的位置
            gf.update_bullets(bullets, spaceships, setting, screen, plane, stats, score_board)  # 控制子弹飞行
            # 更新飞船的位置
            gf.update_spaceships(setting, spaceships, plane, stats, screen, bullets)

        # 绘制图像
        gf.update_screen(screen, setting.bg_img, plane, bullets, spaceships, stats, play_button, score_board)


if __name__ == '__main__':
    run_game()
