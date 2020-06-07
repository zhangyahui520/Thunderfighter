#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.

    Editor      : PyCharm
    File name   : game_func.py
    Author      : Charles zhang
    Created date: 2020/6/7 12:16
    Description :
        用来存放各种功能函数的类
"""
import sys
import time

import pygame

from .bullet import Bullet
from .spaceship import Spaceship


def check_keydown_events(event, plane, setting, screen, bullets):
    '''捕捉用户按下操作， 控制飞机移动'''
    if event.key == pygame.K_RIGHT:
        # 当用户按下键位时标志位为True，开始移动
        plane.mv_right = True
    elif event.key == pygame.K_LEFT:
        plane.mv_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并将其加入到编组bullets中
        if len(bullets) < setting.bullet_allowed:  # 限制子弹数量
            new_bullet = Bullet(setting, screen, plane)
            bullets.add(new_bullet)


def check_keyup_events(event, plane):
    '''捕捉用户松开操作，控制飞机暂停移动'''
    if event.key == pygame.K_RIGHT:
        # 当用户松开键位为false， 停止移动
        plane.mv_right = False
    elif event.key == pygame.K_LEFT:
        plane.mv_left = False


def check_events(plane, setting, screen, bullets, stats, play_button, spaceships, score_board):
    '''为了防止游戏窗口启动会立马关闭，在其中增加一个游戏循环（无限循环）'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT用户请求程序关闭
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, plane, setting, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, plane)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y, spaceships, score_board)
        '''
        当用户按键时，都会在pygame中注册一个事件，
        任何一个事件都是通过pygame.event.get()获取的，
        因此可以在函数体内，为每个按键都注册一个KEYDOWN事件。
        '''


def check_play_button(plane, setting, screen, bullets, stats, play_button, mouse_x, mouse_y, spaceships, score_board):
    '''用于检测鼠标的坐标是否与按钮重合'''
    # 玩家单机play按钮开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  # collidepoint 检测单击的位置是否在按钮的rect内
        # 重置计分的所有图像
        score_board.prep_score()
        score_board.prep_high_score()

        # 重置游戏设置
        setting.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)  # 隐藏光标
        stats.game_active = True  # 游戏状态
        stats.reset_stats()  # 重置游戏统计信息

        # 清空飞船列表和子弹列表
        spaceships.empty()
        bullets.empty()

        # 让飞机居中
        plane.center_plane()


def update_screen(screen, bg_img, plane, bullets, spaceships, stats, play_button, score_board):
    '''更新屏幕的图像'''

    # 每次循环都会重新绘制屏幕
    screen.blit(bg_img, [0, 0])  # 绘制图像

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    plane.blitme()  # 将战机绘制到屏幕中
    # 将飞船绘制到屏幕中
    for spaceship in spaceships.sprites():
        spaceship.blitme()

    # 如果游戏处于非活动状态，绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 显示得分
    score_board.show_score()

    # 将完整显示surface更新到屏幕中
    pygame.display.flip()


def update_bullets(bullets, spaceships, setting, screen, plane, stats, score_board):
    '''控制子弹的移动更新'''
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))  # 用于测试子弹是否删除

    collisions = pygame.sprite.groupcollide(bullets, spaceships, True, True)
    '''
    # 方法game.sprite.groupcollide() 将每个子弹的rect和每个飞船的rect进行比较，返回一个字典，
    # 其中包含了发证碰撞的子弹和飞船。这个字典中每个键都是射中飞船的一颗子弹，相应的值为被击中的飞船
    '''  # pygame.sprite.groupcollide的注释

    if collisions:  # 当发生碰撞，会有返回值，才会True
        for spaceship in collisions.values():
            # 遍历字段，确保每个飞船的点数都计入得分
            stats.score += setting.spaceship_points * len(spaceship)  # 发生碰撞加分
            score_board.prep_score()  # 将分数绘制在屏幕上

        check_high_score(stats, score_board)  # 检测是否超过最高分

    if len(spaceships) == 0:
        bullets.empty()  # 删除编组中的所有子弹

        # 加快游戏节奏
        setting.increase_speed()
        create_fleet(setting, screen, spaceships, plane)  # 重新调用生成飞船


def check_high_score(stats, score_board):
    '''用于判断是否是最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score  # 如果得分大于最高分，则赋值给最高分
        score_board.prep_high_score()


# 计算每行可以容纳多少个飞船的函数
def get_number_spaceship_x(setting, spaceship_width):
    # 计算可以容纳多少飞船的宽度
    available_space_x = setting.screen_width - (2 * spaceship_width)  # 可用屏幕宽度
    number_spaceship_x = int(available_space_x / (2 * spaceship_width))
    return number_spaceship_x


# 计算可以容纳多少行飞船的函数
def get_number_spaceship_y(setting, plane_height, spaceship_height):
    '''计算可以容纳多少行飞船，同时要减去战机的高度'''
    # 计算可以容纳多少飞船的高度
    available_space_y = setting.screen_height - (7 * spaceship_height) - plane_height  # 可用屏幕高度
    number_rows = int(available_space_y / spaceship_height)
    return number_rows


def create_spaceship(setting, screen, spaceships, spaceship_number, number_rows):
    '''创建一个飞船编组'''

    # 创建一个飞船并加入当前行
    spaceship = Spaceship(setting, screen)
    spaceship_width = spaceship.rect.width  # 飞船的宽度
    spaceship.x = spaceship_width + 2 * spaceship_width * spaceship_number  # 计算飞船出现的起始位置
    spaceship.rect.x = spaceship.x
    spaceship.rect.y = spaceship.rect.height + 2 * spaceship.rect.height * number_rows
    spaceships.add(spaceship)


def create_fleet(setting, screen, spaceships, plane):
    spaceship = Spaceship(setting, screen)
    number_spaceship_x = get_number_spaceship_x(setting, spaceship.rect.width)
    number_rows = get_number_spaceship_y(setting, plane.rect.height, spaceship.rect.height)

    for row_number in range(number_rows):
        for spaceship_number in range(number_spaceship_x):
            create_spaceship(setting, screen, spaceships, spaceship_number, row_number)


def change_fleet_direction(setting, spaceships):
    '''将所有飞船下移，并改变方向'''
    for spaceship in spaceships.sprites():
        spaceship.rect.y += setting.spaceship_drop_speed
    setting.spaceship_direction *= -1  # 如果为1则相乘为-1， 如果为-1则相乘为1


def check_fleet_edges(setting, spaceships):
    '''有飞船到了边缘就采取的措施'''
    for spaceship in spaceships.sprites():
        if spaceship.check_edges():  # 如果为true， 已经到了边缘， 就执行change_fleet_direction改变方向
            change_fleet_direction(setting, spaceships)
            break


def plane_hit(setting, spaceships, plane, stats, screen, bullets):
    '''有飞船撞击到战机以后血量-1， 创建一批新的飞船，并将战机重新放置到屏幕的原始位置，
    引入time模块，实现暂停的效果'''

    if stats.planes_left > 0:
        stats.planes_left -= 1  # 将飞机的血量 -1

        # 清空飞船和子弹的编组
        spaceships.empty()
        bullets.empty()

        # 创建新的飞船和战机
        create_fleet(setting, screen, spaceships, plane)
        plane.center_plane()

        time.sleep(1)  # 暂停1S
    else:
        stats.game_active = False
        # 将光标设置为显示
        pygame.mouse.set_visible(True)


def check_spaceship_bottom(setting, spaceships, plane, stats, screen, bullets):
    '''检测是否有飞船触碰到底部'''
    screen_rect = screen.get_rect()

    for spaceship in spaceships.sprites():
        if spaceship.rect.bottom >= screen_rect.bottom:
            # 跟飞船碰撞一样处理
            plane_hit(setting, spaceships, plane, stats, screen, bullets)


def update_spaceships(setting, spaceships, plane, stats, screen, bullets):
    '''更新飞船的位置'''

    # 更新飞船的位置
    spaceships.update()
    # 检测是否有飞船处于边缘，并及时更新
    check_fleet_edges(setting, spaceships)

    # 检测飞船与战机的碰撞
    '''
    pygame.sprite.spritecollideany方法
    * 接受两个参数，一个精灵和一个编组，
    * 检测编组中的成员是否与碰撞，如果检测到碰撞则停止遍历编组
    * 如果没有发生碰撞则返回None
    '''  # pygame.sprite.spritecollideany的注释
    game_over = pygame.sprite.spritecollideany(plane, spaceships)
    if game_over:
        plane_hit(setting, spaceships, plane, stats, screen, bullets)

    check_spaceship_bottom(setting, spaceships, plane, stats, screen, bullets)
