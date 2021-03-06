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

# =============================================================================

def intro():
    '''首頁'''
    intro       = True
    # 音樂
    # pygame.mixer.music.play(-1)
    # 首頁按鈕配置
    rungame1_x     	= 100
    rungame1_y     	= 380
    high1_x 		= rungame1_x + 220
    high1_y     	= rungame1_y
    rungame2_x     	= rungame1_x
    rungame2_y     	= rungame1_y + 70
    high2_x 		= high1_x
    high2_y     	= rungame2_y
    exit_x     		= (rungame1_x+high1_x)/2
    exit_y     		= rungame2_y+70
    menu_width  	= 180
    menu_height 	= 50
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
        pygame.draw.rect(gameDisplay,blue,  (rungame1_x,rungame1_y,menu_width,menu_height))
        pygame.draw.rect(gameDisplay,green,  (rungame2_x,rungame2_y,menu_width,menu_height))
        pygame.draw.rect(gameDisplay,red,   (exit_x,exit_y,menu_width,menu_height))
        pygame.draw.rect(gameDisplay,blue,   (high1_x,high1_y,menu_width,menu_height))
        pygame.draw.rect(gameDisplay,green,   (high2_x,high2_y,menu_width,menu_height))
        message_display("mode1"    , 38 , rungame1_x + menu_width / 2 , rungame1_y + menu_height / 2)
        message_display("high1"  , 38 , high1_x + menu_width / 2 , high1_y + menu_height / 2)
        message_display("mode2"    , 38 , rungame2_x + menu_width / 2 , rungame2_y + menu_height / 2)
        message_display("high2"  , 38 , high2_x + menu_width / 2 , high2_y + menu_height / 2)
        message_display("Exit"  , 38 , exit_x + menu_width / 2 , exit_y + menu_height / 2)
        # 碰到的時候變顏色
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (rungame1_x < mouse[0] < rungame1_x + menu_width) and (rungame1_y < mouse[1] < rungame1_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(rungame1_x,rungame1_y,menu_width,menu_height))
            if click[0] == 1: return 'runGame1'
        if (high1_x < mouse[0] < high1_x + menu_width) and (high1_y < mouse[1] < high1_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(high1_x,high1_y,menu_width,menu_height))
            if click[0] == 1: high1()
        if (rungame2_x < mouse[0] < rungame2_x + menu_width) and (rungame2_y < mouse[1] < rungame2_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(rungame2_x,rungame2_y,menu_width,menu_height))
            if click[0] == 1: return 'runGame2'
        if (high2_x < mouse[0] < high2_x + menu_width) and (high2_y < mouse[1] < high2_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(high2_x,high2_y,menu_width,menu_height))
            if click[0] == 1: high2()
        if (exit_x < mouse[0] < exit_x + menu_width) and (exit_y < mouse[1] < exit_y + menu_height):
            pygame.draw.rect(gameDisplay,gray,(exit_x,exit_y,menu_width,menu_height))
            if click[0] == 1:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(50)
def text_objects(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def message_display(text,size,x,y):
    font = pygame.font.Font("Star_Jedi_Rounded.ttf",size)
    text_surface , text_rectangle = text_objects(text,font)
    text_rectangle.center = (x,y)
    gameDisplay.blit(text_surface , text_rectangle)
def high1():
    import csv
    menu4_x         = 400
    menu4_y         = 510
    menu_width2     = 180
    menu_height2     = 50
    # 讀入排行榜資訊
    fh1     = open('his_high1.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
    csv1     = csv.DictReader(fh1) 
    cname1     = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
    list     = []
    for aline in csv1:
        list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
        list.append(list1)
    fh1.close()
    # 排行榜顯示
    gameDisplay.fill(black)
    titFont = pygame.font.Font('Starjhol.ttf', 50)
    titSurf = titFont.render('Leaderboard', True, red)
    titRect = titSurf.get_rect()
    titRect.midtop = (300, 20)
    gameDisplay.blit(titSurf, titRect)
    titFont2 = pygame.font.Font('Starjhol.ttf', 50)
    titSurf2 = titFont2.render('------------------------------', True, red)
    titRect2 = titSurf2.get_rect()
    titRect2.midtop = (300, 80)
    gameDisplay.blit(titSurf2, titRect2)
    titSurf3 = titFont2.render('------------------------------', True, red)
    titRect3 = titSurf3.get_rect()
    titRect3.midtop = (300, 420)
    gameDisplay.blit(titSurf3, titRect3)
    message_display(list[0][0], 38 , 100,200)
    message_display(list[0][1], 38 , 250,200)
    message_display(list[0][2], 38 , 450,200)
    message_display(list[1][0], 38 , 100,300)
    message_display(list[1][1], 38 , 250,300)
    message_display(list[1][2], 38 , 450,300)
    message_display(list[2][0], 38 , 100,400)
    message_display(list[2][1], 38 , 250,400)
    message_display(list[2][2], 38 , 450,400)
    high_run = True

    while high_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # 回主頁
        pygame.draw.rect(gameDisplay,gray,  (menu4_x,menu4_y,menu_width2,menu_height2))
        mouse1 = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
        if (menu4_x < mouse1[0] < menu4_x + menu_width2) and (menu4_y < mouse1[1] < menu4_y + menu_height2):
            pygame.draw.rect(gameDisplay,blue,(menu4_x,menu4_y,menu_width2,menu_height2))
            if click1[0] == 1:
                gameDisplay.fill(black)
                high_run = False
        message_display("return"    , 38 , menu4_x + menu_width2 / 2 , menu4_y + menu_height2 / 2)
        pygame.display.update()
    return
# =============================================================================
def high2():
    import csv
    menu4_x         = 400
    menu4_y         = 510
    menu_width2     = 180
    menu_height2     = 50
    # 讀入排行榜資訊
    fh1     = open('his_high2.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
    csv1     = csv.DictReader(fh1) 
    cname1     = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
    list     = []
    for aline in csv1:
        list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
        list.append(list1)
    fh1.close()
    # 排行榜顯示
    gameDisplay.fill(black)
    titFont = pygame.font.Font('Starjhol.ttf', 50)
    titSurf = titFont.render('Leaderboard', True, red)
    titRect = titSurf.get_rect()
    titRect.midtop = (300, 20)
    gameDisplay.blit(titSurf, titRect)
    titFont2 = pygame.font.Font('Starjhol.ttf', 50)
    titSurf2 = titFont2.render('------------------------------', True, red)
    titRect2 = titSurf2.get_rect()
    titRect2.midtop = (300, 80)
    gameDisplay.blit(titSurf2, titRect2)
    titSurf3 = titFont2.render('------------------------------', True, red)
    titRect3 = titSurf3.get_rect()
    titRect3.midtop = (300, 420)
    gameDisplay.blit(titSurf3, titRect3)
    message_display(list[0][0], 38 , 100,200)
    message_display(list[0][1], 38 , 250,200)
    message_display(list[0][2], 38 , 450,200)
    message_display(list[1][0], 38 , 100,300)
    message_display(list[1][1], 38 , 250,300)
    message_display(list[1][2], 38 , 450,300)
    message_display(list[2][0], 38 , 100,400)
    message_display(list[2][1], 38 , 250,400)
    message_display(list[2][2], 38 , 450,400)
    high_run = True

    while high_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # 回主頁
        pygame.draw.rect(gameDisplay,gray,  (menu4_x,menu4_y,menu_width2,menu_height2))
        mouse1 = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
        if (menu4_x < mouse1[0] < menu4_x + menu_width2) and (menu4_y < mouse1[1] < menu4_y + menu_height2):
            pygame.draw.rect(gameDisplay,blue,(menu4_x,menu4_y,menu_width2,menu_height2))
            if click1[0] == 1:
                gameDisplay.fill(black)
                high_run = False
        message_display("return"    , 38 , menu4_x + menu_width2 / 2 , menu4_y + menu_height2 / 2)
        pygame.display.update()
    return
# =============================================================================