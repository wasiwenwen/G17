import pygame, time, random, sys
from intro import *
from pygame.locals import *  
from GAMEOVER import *
from get_user import *

# =====================================================
# 使用者名稱
user = ""

# 單一使用者分數
score = 0
score2 = 0

# 檔案輸入
file1 = 'his_high1.csv'
file2 = 'his_high2.csv'
# =====================================================
# 歷史紀錄
def HisHighShowInGame(file): #紀錄目前最高分，呈現在主遊戲畫面
	import csv
	fh1 = open(file, 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
	list = []
	for aline in csv1:
		tuple = (aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip())
		list.append(tuple)

	his_highNO1 = list[0][2]
	fh1.close()
	return int(his_highNO1)
def break_record(file , s , user):
	import csv
	fh1 = open(file, 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
	his_list = []
	for aline in csv1:
		list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
		his_list.append(list1)
	fh1.close()

	if s > int(his_list[2][2]):
		if s > int(his_list[1][2]):
			if s > int(his_list[0][2]):
				his_list[2] = [3,his_list[1][1],his_list[1][2]]
				his_list[1] = [2,his_list[0][1],his_list[0][2]]
				his_list[0] = [1,user,s]
			else:
				his_list[2] = [3,his_list[1][1],his_list[1][2]]
				his_list[1] = [2,user,s]
				
		else:
			his_list[2] = [3,user,s]

	with open(file, 'w', newline='', encoding = 'utf-8') as csvfile:
		# 建立 CSV 檔寫入器
		writer = csv.writer(csvfile)

		# 寫入一列資料
		writer.writerow(['#', 'user', 'score'])

		# 寫入另外幾列資料
		writer.writerow(his_list[0])
		writer.writerow(his_list[1])
		writer.writerow(his_list[2])
	csvfile.close()
# =====================================================
#基本設定

#設定視窗大小
display_width = 600
display_height = 600

#設定要使用的顏色的RGB
black   = (0, 0, 0)
white   = (255, 255, 255)
red  = (255, 0, 0)
gray    = (60,60,60)
green   = (108,248,101)
blue    = (99,148,248)

#設定汽車寬度
ufo_height = 75
ufo_width = 135
ufo_width2 = 200 #for mode2

#設定星球大小
planet_height = 75
planet_width = 135

#設定icon
pygame.display.set_icon(menu_UFO)

#設定跑道x軸大小
runway = [display_width/6 - planet_width/2 , display_width/6 * 3 - planet_width/2, display_width/6 * 5 - planet_width/2]

#讀入飛碟圖片
ufoImg = pygame.image.load("ufo.png")
ufoImg2 = pygame.image.load("ufo2.png") #發光的
ufoImg_blue = pygame.image.load("ufo_b.png") 
ufoImg_green = pygame.image.load("ufo_g.png")
ufoImg_red = pygame.image.load("ufo_r.png")

#讀入星球圖片
Picture = [] #for mode1
g0 = pygame.image.load("g0.png")
g1 = pygame.image.load("g1.png")
g2 = pygame.image.load("g2.png")
g3 = pygame.image.load("g3.png")
r0 = pygame.image.load("r0.png")
r1 = pygame.image.load("r1.png")
r2 = pygame.image.load("r2.png")
r3 = pygame.image.load("r3.png")
y0 = pygame.image.load("y0.png")
y1 = pygame.image.load("y1.png")
y2 = pygame.image.load("y2.png")
y3 = pygame.image.load("y3.png")
b0 = pygame.image.load("b0.png")
b1 = pygame.image.load("b1.png")
b2 = pygame.image.load("b2.png")
b3 = pygame.image.load("b3.png")
Picture.extend([g0, g1, g2, g3, r0, r1, r2, r3, y0, y1, y2, y3, b0, b1, b2, b3])
#增加正確星球的出現機率
Picture.extend([g0, r0, y0, b0])
#for mode2
yellow = [b2, g2, r1, y0, y0]
Picture2 = Picture.copy() 
for i in yellow:
	Picture2.remove(i)


#最高分與排行榜
his_high_score = HisHighShowInGame(file1)
# his_list = his_high_3()
his_high_score2 = HisHighShowInGame(file2)
# his_list2 = his_high_32()
#======================================================================

#建立障礙物
def things(thingx, thingy, planet):
	gameDisplay.blit(planet, (thingx, thingy))

#設定UFO位置
def ufo(x, y , score):
	global his_high_score
	if score >= his_high_score:
		gameDisplay.blit(ufoImg2, (x,y))
	else:
		gameDisplay.blit(ufoImg, (x,y))

def ufo2(x, y , score2, ufo):
	gameDisplay.blit(ufo, (x,y))
	
#產生隨機產生東西
def random_things(planet_height, PlanetRange):
	planet = random.choice(Picture2)
	thing_starty = 0 - planet_height - PlanetRange
	thing_startx = display_width/2 - planet_width/2 - 10
	return thing_startx, thing_starty, planet
		
#設定障礙物
def set_things(planet_height, PlanetRange):
	thing_startx = random.choice(runway) #X座標從跑道中任選一條
	thing_starty = 0 - planet_height - PlanetRange #因為如果從零開始的話，0會出現在畫面上
	planet2 = random.choice(Picture)
	return thing_startx, thing_starty, planet2

#檢查物品要吃與否 for mode1
def check_correct(planet1):
	global Picture
	if (Picture.index(planet1) == 0) or (Picture.index(planet1) == 4) or (Picture.index(planet1) == 8) or (Picture.index(planet1) == 12) or (16 <=(Picture.index(planet1)) <= 19):
		return True
	else:
		return False

#檢查物品要吃與否 for mode2
def check_correct2(planet1):
	global Picture2
	blue_list = [2, 5, 8, 9, 14]
	green_list = [0, 4, 7, 11, 12]
	red_list = [1, 3, 6, 10, 13]
	if Picture2.index(planet1) in blue_list:
		return "blue"
	elif Picture2.index(planet1) in green_list:
		return "green"
	elif Picture2.index(planet1) in red_list:
		return "red"

#產生下個東西		
def make_next_things(thing_starty1, thing_starty2, display_height):
	global PlanetRange
	thing_starty1 = thing_starty2 - PlanetRange
	thing_startx1 = random.choice(runway)
	planet_next = random.choice(Picture)
	return thing_startx1, thing_starty1, planet_next

#吃到東西加分後重新生成新的	for mode1
def check_eat(thing_startx, thing_starty, thing_D_starty, channel1):
	global score
	channel1.play(pygame.mixer.Sound("eat.wav"))
	thing_startx += 10000
	score += 100
	pygame.display.update()
	thing_starty = thing_D_starty - PlanetRange 
	thing_startx = random.choice(runway)
	planet = random.choice(Picture)
	return thing_starty, thing_startx, planet

#吃到東西加分後重新生成新的	for mode2	
def check_eat2(thing_startx, thing_starty, thing_D_starty, channel1): 
	global score2
	channel1.play(pygame.mixer.Sound("eat.wav"))
	thing_startx += 10000
	score2 += 100
	pygame.display.update()
	thing_starty = thing_D_starty - PlanetRange
	thing_startx = display_width/6 * 3 - planet_width/2 - 10
	planet = random.choice(Picture2)
	return thing_starty, thing_startx, planet
#=========================================================================================	
def main():  
	global speedCLOCK, gameDisplay, BASICFONT, user, his_high_score, score, his_high_score2, score2

	pygame.init()  
	speedCLOCK = pygame.time.Clock()  
	gameDisplay = pygame.display.set_mode((display_height, display_width))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18) 
	pygame.display.set_caption('Stroop UFO')

	#設定音樂
	channel1 = pygame.mixer.Channel(0)
	pygame.mixer.music.load("for final.mp3")
	pygame.mixer.music.play(-1)
	
	while True:
		intro_call = intro()
		user = get_user()
		if intro_call == 'runGame1':
			while True:
				runGame1()
				pygame.mixer.music.pause()
				break_record(file1,score,user)
				call = showGameOverScreen()
				if call =='again':
					pygame.mixer.music.play(-1)
					continue
				elif call == 'home':
					pygame.mixer.music.play(-1)
					break
		elif intro_call == 'runGame2':
			while True:
				runGame2()
				pygame.mixer.music.pause()
				break_record(file2,score2,user)
				call = showGameOverScreen()
				if call =='again':
					pygame.mixer.music.play(-1)
					continue
				elif call == 'home':
					pygame.mixer.music.play(-1)
					break


#主遊戲迴圈
def runGame1():
	global his_high_score, score, PlanetRange
	x = (display_width/2 - ufo_width/2) #一開始設計在畫面正中央
	y = (display_height * 0.8)
	
	channel1 = pygame.mixer.Channel(0)
	#設定分數
	score = 0

	#設定初始值
	thing_speed = 7
	max_thing_speed = 7
	PlanetRange = 500
	
	
	#設定障礙物(五個)
	thing_startx, thing_starty, planet = set_things(planet_height, (PlanetRange * 0))
	thing_A_startx, thing_A_starty, planet_A = set_things(planet_height, (PlanetRange * 1))
	thing_B_startx, thing_B_starty, planet_B = set_things(planet_height, (PlanetRange * 2))
	thing_C_startx, thing_C_starty, planet_C = set_things(planet_height, (PlanetRange * 3))
	thing_D_startx, thing_D_starty, planet_D = set_things(planet_height, (PlanetRange * 4))
	

	# 讓背景動起來(1/2) - 設定背景的位置參數初始值
	bg_speed = 3
	bg_x1, bg_x2 = 0, 0
	bg_y1, bg_y2= 0, (- display_height) 
	planet = random.choice(Picture)
	
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
			
		#檢查要吃與否
		checkTrue = check_correct(planet)
		checkTrue_A = check_correct(planet_A)
		checkTrue_B = check_correct(planet_B)
		checkTrue_C = check_correct(planet_C)
		checkTrue_D = check_correct(planet_D)

		#設定背景顏色，需特別注意，此條為將螢幕刷成同一顏色，若物件的函數寫在這之前，就會被刷成同一顏色而無法辨認
		gameDisplay.fill(black)
		background_image = pygame.image.load("bg.png").convert()
		background_image = pygame.transform.scale(background_image,(display_height, display_width))
		gameDisplay.blit(background_image,(bg_x1,bg_y1))
		gameDisplay.blit(background_image,(bg_x2,bg_y2))
		
		# scoresreen
		scoreFont = pygame.font.Font('Starjhol.ttf', 22)
		scoreSurf = scoreFont.render('your score:'+str(score), True, white)
		highscoreSurf = scoreFont.render('high score:'+str(his_high_score), True, white)
		scoreRect = scoreSurf.get_rect()
		highscoreRect = highscoreSurf.get_rect()
		scoreRect.midtop = (display_width - 170, 550)
		highscoreRect.midtop = (150, 550) 
		gameDisplay.blit(scoreSurf, scoreRect)
		gameDisplay.blit(highscoreSurf, highscoreRect)
		
		#依分數增加速度
		if score < 300:
			PlanetRange = 500
			thing_speed = 5 #用來加速 

		elif 300 <= score < 500:
			PlanetRange = 400
			thing_speed = 6 #用來加速 

			
		elif 500 <= score < 1000:
			PlanetRange = 300
			thing_speed = 7 #用來加速 

			
		elif score >= 1000:
			PlanetRange = 200
			thing_speed = 8 #用來加速 


		#things(thingx, thingy, planet)
		things(thing_startx, thing_starty, planet)
		thing_starty += thing_speed
		things(thing_A_startx, thing_A_starty, planet_A)
		thing_A_starty += thing_speed
		things(thing_B_startx, thing_B_starty, planet_B)
		thing_B_starty += thing_speed
		things(thing_C_startx, thing_C_starty, planet_C)
		thing_C_starty += thing_speed
		things(thing_D_startx, thing_D_starty, planet_D)
		thing_D_starty += thing_speed
				
		#設定汽車的位置
		ufo(x,y, score)
		
		#check_eat
		deadline = display_height - ufo_height
		if checkTrue == True:
			if (y < (thing_starty) and y + ufo_height >= thing_starty) and x == thing_startx:
				thing_starty, thing_startx, planet = check_eat(thing_startx, thing_starty, thing_D_starty, channel1)
			elif thing_starty > deadline:
				return
			
		if checkTrue_A == True:
			if (y < (thing_A_starty) and y + ufo_height >= thing_A_starty) and x == thing_A_startx:
				thing_A_starty, thing_A_startx, planet_A = check_eat(thing_A_startx, thing_A_starty, thing_starty, channel1)
			elif thing_A_starty > deadline:
				return
			
		if checkTrue_B == True:
			if (y < (thing_B_starty) and y + ufo_height >= thing_B_starty) and x == thing_B_startx:
				thing_B_starty, thing_B_startx, planet_B = check_eat(thing_B_startx, thing_B_starty, thing_A_starty, channel1)
			elif thing_B_starty > deadline:
				return
			
		if checkTrue_C == True:
			if (y < (thing_C_starty) and y + ufo_height >= thing_C_starty) and x == thing_C_startx:
				thing_C_starty, thing_C_startx, planet_C = check_eat(thing_C_startx, thing_C_starty, thing_B_starty, channel1)
			elif thing_C_starty > deadline:
				return
			
		if checkTrue_D == True:
			if (y < (thing_D_starty) and y + ufo_height >= thing_D_starty) and x == thing_D_startx:
				thing_D_starty, thing_D_startx, planet_D = check_eat(thing_D_startx, thing_D_starty, thing_C_starty, channel1)
			elif thing_D_starty > deadline:
				return

		# 是否超越歷史紀錄
		if int(score) > int(his_high_score):
			his_high_score = score
			his_high_user = user

		#check crash
		if (y < (thing_starty) and y + ufo_height >= thing_starty) and checkTrue == False:
			if x == thing_startx:
				return #吃到錯誤的GAMOVER
				
		if (y < (thing_A_starty) and y + ufo_height >= thing_A_starty) and checkTrue_A == False:
			if x == thing_A_startx:
				return #吃到錯誤的GAMOVER
    
		if (y < (thing_B_starty) and y + ufo_height >= thing_B_starty) and checkTrue_B == False:
			if x == thing_B_startx:
				return #吃到錯誤的GAMOVER
		        
		if (y < (thing_C_starty) and y + ufo_height >= thing_C_starty) and checkTrue_C == False:
			if x == thing_C_startx:
				return #吃到錯誤的GAMOVER
				
		if (y < (thing_D_starty) and y + ufo_height >= thing_D_starty) and checkTrue_D == False:
			if x == thing_D_startx:
				return #吃到錯誤的GAMOVER
		
		#星球超過下界，就再生成一個新的
		if thing_starty > display_height:
			thing_startx, thing_starty, planet = make_next_things(thing_starty, thing_D_starty, display_height)	
		if thing_A_starty > display_height:
			thing_A_startx, thing_A_starty, planet_A = make_next_things(thing_A_starty, thing_starty, display_height)
		if thing_B_starty > display_height:
			thing_B_startx, thing_B_starty, planet_B = make_next_things(thing_B_starty, thing_A_starty, display_height)
		if thing_C_starty > display_height:			
			thing_C_startx, thing_C_starty, planet_C = make_next_things(thing_C_starty, thing_B_starty, display_height)
		if thing_D_starty > display_height:
			thing_D_startx, thing_D_starty, planet_D = make_next_things(thing_D_starty, thing_C_starty, display_height)		
			
		#讓背景動起來(2/2) - 改變位置參數
		bg_y1 += bg_speed
		bg_y2 += bg_speed
		if bg_y1 >= display_height:
			bg_y1 = - display_height
			
		if bg_y2 >= display_height:
			bg_y2 = - display_height
		pygame.display.update() #pygame.display.flip()也可以
		
				
		#設定每秒多少動畫窗格。若要有增加速度的感覺，可以增加數字
		speedCLOCK.tick(50)
		pygame.display.update()


def runGame2():
	global his_high_score2, score2, PlanetRange, planet_height
	x = (display_width/2 - ufo_width2/2) #一開始設計在畫面正中央
	y = (display_height * 0.8)
	
	channel1 = pygame.mixer.Channel(0)
	#設定分數
	score2 = 0
	#設定一開始的ufo
	ufo = ufoImg_blue
	ufo_color = "blue"
	
	#設定初始值
	thing_speed = 5
	PlanetRange = 500
	
	#設定障礙物(五個)
	thing_startx, thing_starty, planet = random_things(planet_height, (PlanetRange * 0))
	thing_A_startx, thing_A_starty, planet_A = random_things(planet_height, (PlanetRange * 1))
	thing_B_startx, thing_B_starty, planet_B = random_things(planet_height, (PlanetRange * 2))
	thing_C_startx, thing_C_starty, planet_C = random_things(planet_height, (PlanetRange * 3))
	thing_D_startx, thing_D_starty, planet_D = random_things(planet_height, (PlanetRange * 4))
	
	
	# 讓背景動起來(1/2) - 設定背景的位置參數初始值
	bg_speed = 3
	bg_x1, bg_x2= 0, 0
	bg_y1, bg_y2= 0, (- display_height) 
	planet = random.choice(Picture2)
	
	#while迴圈
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
			#設定按按鍵時汽車會位移
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ufo = ufoImg_blue
					ufo_color = "blue"
				elif event.key == pygame.K_RIGHT:
					ufo = ufoImg_green
					ufo_color = "green"
				elif event.key == pygame.K_DOWN:
					ufo = ufoImg_red
					ufo_color = "red"
		
		#檢查要吃與否
		checkTrue = check_correct2(planet)
		checkTrue_A = check_correct2(planet_A)
		checkTrue_B = check_correct2(planet_B)
		checkTrue_C = check_correct2(planet_C)
		checkTrue_D = check_correct2(planet_D)

		#設定背景顏色
		gameDisplay.fill(black)
		background_image = pygame.image.load("bg.png").convert()
		background_image = pygame.transform.scale(background_image,(display_height, display_width))
		gameDisplay.blit(background_image,(bg_x1,bg_y1))
		gameDisplay.blit(background_image,(bg_x2,bg_y2))
		
		# scoresreen
		scoreFont = pygame.font.Font('Starjhol.ttf', 22)
		scoreSurf = scoreFont.render('your score:'+str(score2), True, white)
		highscoreSurf = scoreFont.render('high score:'+str(his_high_score2), True, white)
		scoreRect = scoreSurf.get_rect()
		highscoreRect = highscoreSurf.get_rect()
		scoreRect.midtop = (display_width - 170, 550)
		highscoreRect.midtop = (150, 550) 
		gameDisplay.blit(scoreSurf, scoreRect)
		gameDisplay.blit(highscoreSurf, highscoreRect)
		
		#依分數增加速度
		if score2 < 300:
			PlanetRange = 400
			thing_speed = 7 

		elif 300 <= score2 < 500:
			PlanetRange = 350
			thing_speed = 7.5

			
		elif 500 <= score2 < 1000:
			PlanetRange = 300
			thing_speed = 8

			
		elif score2 >= 1000:
			PlanetRange = 200
			thing_speed = 8.5 

		#設定planet的位置與移動
		things(thing_startx, thing_starty, planet)
		thing_starty += thing_speed
		things(thing_A_startx, thing_A_starty, planet_A)
		thing_A_starty += thing_speed
		things(thing_B_startx, thing_B_starty, planet_B)
		thing_B_starty += thing_speed
		things(thing_C_startx, thing_C_starty, planet_C)
		thing_C_starty += thing_speed
		things(thing_D_startx, thing_D_starty, planet_D)
		thing_D_starty += thing_speed
				
		#設定ufo的位置
		ufo2(x,y, score2, ufo)
		
		#check_eat
		deadline = display_height - ufo_height
		if checkTrue == ufo_color:
			if (y < (thing_starty) and y + ufo_height >= thing_starty):
				thing_starty, thing_startx, planet = check_eat2(thing_startx, thing_starty, thing_D_starty, channel1)	
		if checkTrue_A == ufo_color:
			if (y < (thing_A_starty) and y + ufo_height >= thing_A_starty):
				thing_A_starty, thing_A_startx, planet_A = check_eat2(thing_A_startx, thing_A_starty, thing_starty, channel1)
		if checkTrue_B == ufo_color:
			if (y < (thing_B_starty) and y + ufo_height >= thing_B_starty):
				thing_B_starty, thing_B_startx, planet_B = check_eat2(thing_B_startx, thing_B_starty, thing_A_starty, channel1)
		if checkTrue_C == ufo_color:
			if (y < (thing_C_starty) and y + ufo_height >= thing_C_starty):
				thing_C_starty, thing_C_startx, planet_C = check_eat2(thing_C_startx, thing_C_starty, thing_B_starty, channel1)
		if checkTrue_D == ufo_color:
			if (y < (thing_D_starty) and y + ufo_height >= thing_D_starty):
				thing_D_starty, thing_D_startx, planet_D = check_eat2(thing_D_startx, thing_D_starty, thing_C_starty, channel1)

		# 是否超越歷史紀錄
		if int(score2) > int(his_high_score2):
			his_high_score2 = score2
			his_high_user = user

		#check crash
		if (thing_starty + planet_height - 40 >= y) and checkTrue != ufo_color:
			return 	
		if (thing_A_starty + planet_height - 40 >= y) and checkTrue_A != ufo_color:
			return 
		if (thing_B_starty + planet_height - 40 >= y) and checkTrue_B != ufo_color:
			return       
		if (thing_C_starty + planet_height - 40 >= y) and checkTrue_C != ufo_color:
			return	
		if (thing_D_starty + planet_height - 40 >= y) and checkTrue_D != ufo_color:
			return 
		
		#讓背景動起來(2/2) - 改變位置參數
		bg_y1 += bg_speed
		bg_y2 += bg_speed
		if bg_y1 >= display_height:
			bg_y1 = - display_height
			
		if bg_y2 >= display_height:
			bg_y2 = - display_height
		pygame.display.update() #pygame.display.flip()也可以
		
				
		#設定每秒多少動畫窗格。若要有增加速度的感覺，可以增加數字
		speedCLOCK.tick(50)
		pygame.display.update()
	
#啟動主遊戲迴圈        
if __name__ == '__main__':  
	try:  
		main()  
	except SystemExit:  
		pass        
