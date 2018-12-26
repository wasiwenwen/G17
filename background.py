import random  
import pygame  
import sys	
from pygame.locals import *	 

# UFOspeed = 17
Window_Width = 600	
Window_Height = 600	 
# Cell_Size = 30

# Defining element colors for the program
White = (255, 255, 255)	 
Black = (0, 0, 0)  
Red = (255, 0, 0)  
Green = (0, 255, 0)	 
DARKGreen = (0, 155, 0)	 
DARKGRAY = (40, 40, 40)		
YELLOW = (255, 255, 0)	
Red_DARK = (150, 0, 0)	
BLUE = (0, 0, 255)	
BLUE_DARK = (0, 0, 150)

# Defining keyboard keys	   
# LEFT = 'left'  
# RIGHT = 'right'	

def main():	 
	global SnakespeedCLOCK, DISPLAYSURF, BASICFONT	
  
	pygame.init()  
	SnakespeedCLOCK = pygame.time.Clock()  
	DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)  
	pygame.display.set_caption('Stroop UFO')	 
  
	# showStartScreen()  
	while True:	 
		runGame()  
		
 

def runGame():	
	global Window_Width
	
	# 讓背景動起來(1/2) - 設定背景的位置參數初始值
	bg_speed = 10
	bg_x1 = 0
	bg_x2 = 0
	bg_y1 = 0
	bg_y2 = -600
	DISPLAYSURF.fill(Black)
	background_image = pygame.image.load("star.png").convert()
	background_image = pygame.transform.scale(background_image,(Window_Width,Window_Width))
	
	while True:	 # main game loop  
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		DISPLAYSURF.blit(background_image,(bg_x1,bg_y1))
		DISPLAYSURF.blit(background_image,(bg_x2,bg_y2))	
		pygame.display.update()
		
		#讓背景動起來(2/2) - 改變位置參數
		bg_y1 += bg_speed
		bg_y2 += bg_speed
		if bg_y1 >= Window_Height:
			bg_y1 = -600
			
		if bg_y2 >= Window_Height:
			bg_y2 = -600
		pygame.display.update()
		SnakespeedCLOCK.tick(17)
		
if __name__ == '__main__':	
	try:  
		main()	
	except SystemExit:	
		pass 