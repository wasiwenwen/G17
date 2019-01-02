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
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue  
  
    while True:  
        if checkForKeyPress():  
            pygame.event.get()  # clear event queue  
def drawPressKeyMsg():
    FONT1 = pygame.font.Font('Star_Jedi_Rounded.ttf', 14)  
    pressKeySurf = FONT1.render('press a key to play.', True, white)  
    pressKeyRect = pressKeySurf.get_rect()  
    pressKeyRect.topleft = (display_width - 200, display_height - 30)  
    gameDisplay.blit(pressKeySurf, pressKeyRect)
def checkForKeyPress():  
    if len(pygame.event.get(QUIT)) > 0:  
        pygame.quit()
        sys.exit()
    keyUpEvents = pygame.event.get(KEYUP)  
    if len(keyUpEvents) == 0:  
        return None  
    if keyUpEvents[0].key == K_ESCAPE:  
        pygame.quit()  
        sys.exit()  
    return keyUpEvents[0].key
# =============================================================================

showGameOverScreen()

