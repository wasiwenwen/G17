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
# 圖片設定
menu_UFO    = pygame.image.load("menu_ufo.png")
menu_UFO_m  = pygame.image.load("menu_ufo_m.png")
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

        pygame.draw.rect(gameDisplay,blue,  (btn1_x,btn1_y,btn_width,btn_height))
        pygame.draw.rect(gameDisplay,red,   (btn2_x,btn2_y,btn_width,btn_height))
        message_display("again" , 34 , btn1_x + btn_width / 2 , btn1_y + btn_height / 2)
        message_display("intro" , 34 , btn2_x + btn_width / 2 , btn2_y + btn_height / 2)
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
                return 'intro'
                over_run = False
        pygame.display.update()



    # drawPressKeyMsg()
    # pygame.display.update()
    # pygame.time.wait(500)
    # checkForKeyPress()  # clear out any key presses in the event queue  
  
    # while True:  
    #     if checkForKeyPress():  
    #         pygame.event.get()  # clear event queue
    #         return  
def drawPressKeyMsg():
    FONT1 = pygame.font.Font('Star_Jedi_Rounded.ttf', 14)  
    pressKeySurf = FONT1.render('press a key to play.', True, white)  
    pressKeyRect = pressKeySurf.get_rect()  
    pressKeyRect.topleft = (display_width - 200, display_height - 30)  
    gameDisplay.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():  
    if len(pygame.event.get(QUIT)) > 0:  
        terminate()  
    keyUpEvents = pygame.event.get(KEYUP)  
    if len(keyUpEvents) == 0:  
        return None  
    if keyUpEvents[0].key == K_ESCAPE:  
        terminate()  
    return keyUpEvents[0].key

def terminate():  
    pygame.quit()  
    sys.exit()
def text_objects(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def message_display(text,size,x,y):
    font = pygame.font.Font("Star_Jedi_Rounded.ttf",size)
    text_surface , text_rectangle = text_objects(text,font)
    text_rectangle.center = (x,y)
    gameDisplay.blit(text_surface , text_rectangle)
# =============================================================================

