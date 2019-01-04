import pygame, time, random, sys
from intro import *
from pygame.locals import *  
from GAMEOVER import *


#設定視窗大小
display_width = 600
display_height = 600

#設定要使用的顏色的RGB
black	= (0, 0, 0)
white	= (255, 255, 255)
red		= (255, 0, 0)
gray	= (60,60,60)
green	= (108,248,101)
blue	= (99,148,248)

#設定汽車寬度(查圖片像素)
car_height = 75
car_width = 135

#設定星球大小
planet_height = 75
planet_width = 135

#設定icon
pygame.display.set_icon(menu_UFO)


#設定跑道x軸大小
runway = [display_width/6 - planet_width/2 , display_width/6 * 3 - planet_width/2, display_width/6 * 5 - planet_width/2]

#讀入飛碟圖片
carImg = pygame.image.load("ufo.png")
# carImg = pygame.transform.scale(carImg,(car_width, car_height))

#讀入星球圖片
Picture = []
g0 = pygame.image.load("g0.png")
# g0 = pygame.transform.scale(g0,(planet_width, planet_height))
Picture.append(g0)
g1 = pygame.image.load("g1.png")
# g1 = pygame.transform.scale(g1,(planet_width, planet_height))
Picture.append(g1)
g2 = pygame.image.load("g2.png")
# g2 = pygame.transform.scale(g2,(planet_width, planet_height))
Picture.append(g2)
g3 = pygame.image.load("g3.png")
# g3 = pygame.transform.scale(g3,(planet_width, planet_height))
Picture.append(g3)
r0 = pygame.image.load("r0.png")
# r0 = pygame.transform.scale(r0,(planet_width, planet_height))
Picture.append(r0)
r1 = pygame.image.load("r1.png")
# r1 = pygame.transform.scale(r1,(planet_width, planet_height))
Picture.append(r1)
r2 = pygame.image.load("r2.png")
# r2 = pygame.transform.scale(r2,(planet_width, planet_height))
Picture.append(r2)
r3 = pygame.image.load("r3.png")
# r3 = pygame.transform.scale(r3,(planet_width, planet_height))
Picture.append(r3)
y0 = pygame.image.load("y0.png")
# y0 = pygame.transform.scale(y0,(yellow_planet_width, planet_height))
Picture.append(y0)
y1 = pygame.image.load("y1.png")
# y1 = pygame.transform.scale(y1,(yellow_planet_width, planet_height))
Picture.append(y1)
y2 = pygame.image.load("y2.png")
# y2 = pygame.transform.scale(y2,(yellow_planet_width, planet_height))
Picture.append(y2)
y3 = pygame.image.load("y3.png")
# y3 = pygame.transform.scale(y3,(yellow_planet_width, planet_height))
Picture.append(y3)
b0 = pygame.image.load("b0.png")
# b0 = pygame.transform.scale(b0,(blue_planet_width, planet_height))
Picture.append(b0)
b1 = pygame.image.load("b1.png")
# b1 = pygame.transform.scale(b1,(blue_planet_width, planet_height))
Picture.append(b1)
b2 = pygame.image.load("b2.png")
# b2 = pygame.transform.scale(b2,(blue_planet_width, planet_height))
Picture.append(b2)
b3 = pygame.image.load("b3.png")
# b3 = pygame.transform.scale(b3,(blue_planet_width, planet_height))
Picture.append(b3)


#建立障礙物
def things(thingx, thingy, word):
	gameDisplay.blit(word, (thingx, thingy))

	
#設定汽車位置，注意：越右邊X越大，越上面Y越小，視窗的左上方是(0,0)
def car(x,y):
	gameDisplay.blit(carImg, (x,y))	

def eat(x, y):
    pygame.mixer.music.load("eat.mp3")
    pygame.mixer.music.play(0)

def highscore(count):
	font = pygame.font.SysFont(None,50)
	text = font.render("Score : "+str(count),True,white)
	gameDisplay.blit(text,(0,0))	

def main():	 
	global SnakespeedCLOCK, gameDisplay, BASICFONT	
	pygame.init()  
	SnakespeedCLOCK = pygame.time.Clock()  
	gameDisplay = pygame.display.set_mode((display_height, display_width))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)  
	pygame.display.set_caption('Stroop UFO')
	
	#顯示首頁
	intro()
	while True:	 
		runGame()  	
		showGameOverScreen()

#主遊戲迴圈
def runGame():
	x = (display_width/2 - car_width/2) #一開始設計在畫面正中央
	y = (display_height * 0.8)
	score = 0
	#設定汽車位移
	x_change = 0

	#設定第一個障礙物
	thing_startx = random.choice(runway) #X座標從跑道中任選一條
	thing_starty = - planet_height #因為如果從零開始的話，0會出現在畫面上
	thing_speed = 10
	max_thing_speed = 10

	
	# 讓背景動起來(1/2) - 設定背景的位置參數初始值
	bg_speed = 3
	bg_x1 = 0
	bg_x2 = 0
	bg_y1 = 0
	bg_y2 = - display_height	
	word = random.choice(Picture)
	
	#while迴圈
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
			#設定按按鍵時汽車會位移
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and (x != display_width/6 - planet_width/2):
					x -= display_width/3
				elif event.key == pygame.K_RIGHT and (x != display_width/6 * 5 - planet_width/2):
					x += display_width/3
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		
		checkTrue = False
		if (Picture.index(word) == 0) or (Picture.index(word) == 4) or (Picture.index(word) == 8) or (Picture.index(word) == 12):
			checkTrue = True
		
		#設定背景顏色，需特別注意，此條為將螢幕刷成同一顏色，若物件的函數寫在這之前，就會被刷成同一顏色而無法辨認
		gameDisplay.fill(black)
		background_image = pygame.image.load("bg.png").convert()
		background_image = pygame.transform.scale(background_image,(display_height, display_width))
		gameDisplay.blit(background_image,(bg_x1,bg_y1))
		gameDisplay.blit(background_image,(bg_x2,bg_y2))
	
		
		#things(thingx, thingy, thingw, thingh, color)
		things(thing_startx, thing_starty, word)
		thing_starty += thing_speed

		
		#設定汽車的位置
		car(x,y)
		
		#判斷車子是否超過畫面限制(crash)
		# if x > display_width - car_width or x < 0: #要剪掉car_width是因為，電腦是依據圖片「左上角」的點做判斷
			# return #GAMOVER
		
		#check eat 
		if checkTrue == True:
			if (y < (thing_starty) and y + car_height >= thing_starty) and x == thing_startx:
				eat(x, y)
				thing_startx += 10000
				score += 100
				highscore(score)
				pygame.display.update()
				# clock.tick(60)
				if thing_speed <= max_thing_speed: thing_speed += 0.5 #用來加速 
				else: thing_speed = max_thing_speed	
				thing_starty = 0 - planet_height
				thing_startx = random.choice(runway)
				word = random.choice(Picture)
			elif thing_starty > display_height:
				return
				
		#check crash
		if (y < (thing_starty) and y + car_height >= thing_starty) and checkTrue == False:
			if x == thing_startx:
				# crash(x, y)
				# pygame.display.update()
				return #吃到錯誤的GAMOVER
				
 		# 如果正確的超過畫面，GAMEOVER
		# if and checkTrue == True:
			# return
		
		#如果障礙物已超過畫面，就要再出現下一個障礙物
		if thing_starty > display_height: #注意，Y越下方越大
			if thing_speed <= max_thing_speed: thing_speed += 0.5 #用來加速 
			else: thing_speed = max_thing_speed	
			thing_starty = 0 - planet_height
			thing_startx = random.choice(runway)
			word = random.choice(Picture)

			
		#讓背景動起來(2/2) - 改變位置參數
		bg_y1 += bg_speed
		bg_y2 += bg_speed
		if bg_y1 >= display_height:
			bg_y1 = - display_height
			
		if bg_y2 >= display_height:
			bg_y2 = - display_height
		pygame.display.update() #pygame.display.flip()也可以
		
				
		#設定每秒多少動畫窗格。若要有增加速度的感覺，可以增加數字
		SnakespeedCLOCK.tick(50)
		pygame.display.update()

		
		
#啟動主遊戲迴圈        
if __name__ == '__main__':	
	try:  
		main()	
	except SystemExit:	
		pass        

#結束    
# pygame.quit()    
# quit()