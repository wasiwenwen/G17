import pygame
import time
import random 
import sys
from pygame.locals import *  

pygame.init()
pygame.mixer.init()
# =============================================================================
# 基礎設定

# track time
clock = pygame.time.Clock()

# 視窗大小設定
display_width   = 600
display_height  = 600
gameDisplay     = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Stroop UFO")

# 顏色設定
black   = (0,0,0)
gray    = (60,60,60)
white   = (255,255,255)
green   = (108,248,101)
red     = (248,99,117)
blue    = (99,148,248)

# 音樂設定
pygame.mixer.music.load("starwar.mp3")

# 圖片設定
# 1.首頁/icon
menu_UFO    = pygame.image.load("menu_ufo.png")
menu_UFO_m  = pygame.image.load("menu_ufo_m.png")
# 遊戲主頁面圖片

# =============================================================================



def intro():
    '''首頁'''
    intro       = True
    # icon，不確定設在這會不會有問題！！！！！！！！！！
    pygame.display.set_icon(menu_UFO)
    # 音樂
    pygame.mixer.music.play(-1)
    # 首頁按鈕配置
    menu1_x     = 150
    menu1_y     = 400
    menu2_x     = 350
    menu2_y     = 400
    menu_width  = 100
    menu_height = 50
    # 背景
    bg_speed            = 1
    bg_x1               = 0
    bg_x2               = 0
    bg_y1               = 0
    bg_y2               = - 600
    background_image    = pygame.image.load("bg.png").convert()
    background_image    = pygame.transform.scale(background_image , (display_width , display_height))
    # ------------------------------------------------------------------------
    # 首頁迴圈
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # 背景移動
        gameDisplay.blit(background_image , (bg_x1 , bg_y1))
        gameDisplay.blit(background_image , (bg_x2 , bg_y2))
        bg_y1 += bg_speed
        bg_y2 += bg_speed
        if bg_y1 >= display_height:bg_y1 = -600
        if bg_y2 >= display_height:bg_y2 = -600
        # 圖片/主視覺/按鈕
        gameDisplay.blit(menu_UFO_m ,((display_width / 2) - 130 , 30))
        message_display("stroop ufo" , 60 , display_width / 2 , display_height / 2 + 30)
        pygame.draw.rect(gameDisplay,blue,  (menu1_x,menu1_y,menu_width,menu_height))
        pygame.draw.rect(gameDisplay,red,   (menu2_x,menu2_y,menu_width,menu_height))
        
        # 碰到的時候變顏色
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (menu1_x < mouse[0] < menu1_x + menu_width) and (menu1_y < mouse[1] < menu1_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(menu1_x,menu1_y,menu_width,menu_height))
            if click[0] == 1:
                intro = False
        if (menu2_x < mouse[0] < menu2_x + menu_width) and (menu2_y < mouse[1] < menu2_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(menu2_x,menu2_y,menu_width,menu_height))
            if click[0] == 1:
                pygame.quit()
                quit()

        message_display("Go"    , 38 , menu1_x + menu_width / 2 , menu1_y + menu_height / 2)
        message_display("Exit"  , 38 , menu2_x + menu_width / 2 , menu2_y + menu_height / 2)

        pygame.display.update()
        # track time
        clock.tick(50)
def text_objects(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def message_display(text,size,x,y):
    font = pygame.font.Font("Star_Jedi_Rounded.ttf",size)
    text_surface , text_rectangle = text_objects(text,font)
    text_rectangle.center = (x,y)
    gameDisplay.blit(text_surface , text_rectangle)
# =============================================================================

intro()

