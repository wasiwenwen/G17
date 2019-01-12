import pygame
import sys
from pygame.locals import *
pygame.init()
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
# =============================================================================
def showGameOverScreen():  
    gameOverFont = pygame.font.Font('Star_Jedi_Rounded.ttf', 100)  
    gameSurf = gameOverFont.render('game', True, white)  
    overSurf = gameOverFont.render('over', True, white)  
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (display_width / 2, 20)
    overRect.midtop = (display_width / 2, 100)
    gameDisplay.blit(gameSurf, gameRect)
    gameDisplay.blit(overSurf, overRect)

    btn1_x     = 100
    btn1_y     = 300
    btn2_x     = 350
    btn2_y     = 300
    btn_width  = 150
    btn_height = 50

    over_run = True
    while over_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(btn1_x,btn1_y,btn_width,btn_height, blue, "again" , 34)
        button(btn2_x,btn2_y,btn_width,btn_height, red , "home" , 34)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (btn1_x < mouse[0] < btn1_x + btn_width) and (btn1_y < mouse[1] < btn1_y + btn_height):
            pygame.draw.rect(gameDisplay,gray,(btn1_x,btn1_y,btn_width,btn_height))
            if click[0] == 1:
                return "again"
                over_run = False
        if (btn2_x < mouse[0] < btn2_x + btn_width) and (btn2_y < mouse[1] < btn2_y + btn_height):
            pygame.draw.rect(gameDisplay,gray,(btn2_x,btn2_y,btn_width,btn_height))
            if click[0] == 1:
                return 'home'
                over_run = False
        pygame.display.update()

def text_objects(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def message_display(text,size,x,y):
    font = pygame.font.Font("Star_Jedi_Rounded.ttf",size)
    text_surface , text_rectangle = text_objects(text,font)
    text_rectangle.center = (x,y)
    gameDisplay.blit(text_surface , text_rectangle)
def button(x , y , width , height ,color ,word,w_size):
    pygame.draw.rect(gameDisplay,color,(x,y,width,height))
    message_display(word, w_size , x + width / 2 , y + height / 2)
# =============================================================================