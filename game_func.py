

# 为了不使plane_war.py太长而影响阅读，
# 来创建一个名为game_func.py的模块，
# 用其飞机大战运行的函数，使其逻辑更容易理解

import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, plane, setting, screen, bullets):
    '''捕捉用户按下操作， 控制飞机移动'''
    if event.key == pygame.K_RIGHT:
        # 当用户按下键位时标志位为True，开始移动
        plane.mv_right = True
    elif event.key == pygame.K_LEFT:
        plane.mv_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并将其加入到编组bullets中

        new_bullet = Bullet(setting, screen, plane)
        if len(bullets) < setting.bullet_allowed: # 限制子弹数量
            bullets.add(new_bullet)

def check_keyup_events(event, plane):
    '''捕捉用户松开操作，控制飞机暂停移动'''
    if event.key == pygame.K_RIGHT:
        # 当用户松开键位为false， 停止移动
        plane.mv_right = False
    elif event.key == pygame.K_LEFT:
        plane.mv_left = False

def check_events(plane, setting, screen, bullets):
    '''为了防止游戏窗口启动会立马关闭，在其中增加一个游戏循环（无限循环）'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT用户请求程序关闭
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, plane, setting, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, plane)
        '''
        当用户按键时，都会在pygame中注册一个事件，
        任何一个事件都是通过pygame.event.get()获取的，
        因此可以在函数体内，为每个按键都注册一个KEYDOWN事件。
        '''




def update_screen(screen, bg_img, plane, bullets, spaceship):
    '''更新屏幕的图像'''

    # 每次循环都会重新绘制屏幕
    screen.blit(bg_img, [0,0]) # 绘制图像

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    plane.blitme()  # 将战机绘制到屏幕中
    spaceship.blitme() # 将飞船绘制到屏幕中

    # 将完整显示surface更新到屏幕中
    pygame.display.flip()


def update_bullets(bullets):
    '''控制子弹的移动更新'''
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

