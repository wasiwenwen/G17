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

# =====================================================
# 歷史紀錄
def his_high(): #紀錄目前最高分
	import csv
	fh1 = open('his_high1.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
	list = []
	for aline in csv1:
		tuple = (aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip())
		list.append(tuple)

	his_high = list[0][2]
	fh1.close()
	return int(his_high)


def his_high_3(): #紀錄前三高分
	import csv
	fh1 = open('his_high1.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱

	list = []
	for aline in csv1:
		list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
		list.append(list1)
	his_high = (list[0][1],list[0][2])
	fh1.close()
	return list


def break_record():
	global score,user
	import csv
	if score > int(his_list[2][2]):
		if score > int(his_list[1][2]):
			if score > int(his_list[0][2]):
				his_list[2] = [3,his_list[1][1],his_list[1][2]]
				his_list[1] = [2,his_list[0][1],his_list[0][2]]
				his_list[0] = [1,user,score]
			else:
				his_list[2] = [3,his_list[1][1],his_list[1][2]]
				his_list[1] = [2,user,score]
				
		else:
			his_list[2] = [3,user,score]

	with open('his_high.csv1', 'w', newline='', encoding = 'utf-8') as csvfile:
		# 建立 CSV 檔寫入器
		writer = csv.writer(csvfile)

		# 寫入一列資料
		writer.writerow(['#', 'user', 'score'])

		# 寫入另外幾列資料
		writer.writerow(his_list[0])
		writer.writerow(his_list[1])
		writer.writerow(his_list[2])
	csvfile.close()

# ----------------------------------------------
# 歷史紀錄2
def his_high2(): #紀錄目前最高分
	import csv
	fh1 = open('his_high2.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱
	list = []
	for aline in csv1:
		tuple = (aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip())
		list.append(tuple)

	his_high = list[0][2]
	fh1.close()
	return int(his_high)


def his_high_32(): #紀錄前三高分
	import csv
	fh1 = open('his_high2.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
	csv1 = csv.DictReader(fh1) 
	cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱

	list = []
	for aline in csv1:
		list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
		list.append(list1)
	his_high = (list[0][1],list[0][2])
	fh1.close()
	return list


def break_record2():
	global score2,user
	import csv
	if score2 > int(his_list2[2][2]):
		if score2 > int(his_list2[1][2]):
			if score2 > int(his_list2[0][2]):
				his_list2[2] = [3,his_list2[1][1],his_list2[1][2]]
				his_list2[1] = [2,his_list2[0][1],his_list2[0][2]]
				his_list2[0] = [1,user,score2]
			else:
				his_list2[2] = [3,his_list2[1][1],his_list2[1][2]]
				his_list2[1] = [2,user,score2]
				
		else:
			his_list2[2] = [3,user,score2]

	with open('his_high2.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
		# 建立 CSV 檔寫入器
		writer = csv.writer(csvfile)

		# 寫入一列資料
		writer.writerow(['#', 'user', 'score'])

		# 寫入另外幾列資料
		writer.writerow(his_list2[0])
		writer.writerow(his_list2[1])
		writer.writerow(his_list2[2])
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

#設定汽車寬度(查圖片像素)
car_height = 75
car_width = 135
car_width2 = 200 #for hardgame

#設定星球大小
planet_height = 75
planet_width = 135

#設定icon
pygame.display.set_icon(menu_UFO)

#設定跑道x軸大小
runway = [display_width/6 - planet_width/2 , display_width/6 * 3 - planet_width/2, display_width/6 * 5 - planet_width/2]

#讀入飛碟圖片
carImg = pygame.image.load("ufo.png")
carImg2 = pygame.image.load("ufo2.png") #發光的
carImg_blue = pygame.image.load("ufo_b.png")
carImg_green = pygame.image.load("ufo_g.png")
carImg_red = pygame.image.load("ufo_r.png")

#讀入星球圖片
Picture = [] #for easygame
g0 = pygame.image.load("g0.png")
Picture.append(g0)
g1 = pygame.image.load("g1.png")
Picture.append(g1)
g2 = pygame.image.load("g2.png")
Picture.append(g2)
g3 = pygame.image.load("g3.png")
Picture.append(g3)
r0 = pygame.image.load("r0.png")
Picture.append(r0)
r1 = pygame.image.load("r1.png")
Picture.append(r1)
r2 = pygame.image.load("r2.png")
Picture.append(r2)
r3 = pygame.image.load("r3.png")
Picture.append(r3)
y0 = pygame.image.load("y0.png")
Picture.append(y0)
y1 = pygame.image.load("y1.png")
Picture.append(y1)
y2 = pygame.image.load("y2.png")
Picture.append(y2)
y3 = pygame.image.load("y3.png")
Picture.append(y3)
b0 = pygame.image.load("b0.png")
Picture.append(b0)
b1 = pygame.image.load("b1.png")
Picture.append(b1)
b2 = pygame.image.load("b2.png")
Picture.append(b2)
b3 = pygame.image.load("b3.png")
Picture.append(b3)
Picture.append(g0)
Picture.append(r0)
Picture.append(y0)
Picture.append(b0)

yellow = [b2, g2, r1, y0, y0]
Picture2 = Picture.copy() #for hardgame
for i in yellow:
	Picture2.remove(i)
# print(Picture2)

#最高分與排行榜
his_high_score = his_high()
his_list = his_high_3()
his_high_score2 = his_high2()
his_list2 = his_high_32()
#======================================================================

#建立障礙物
def things(thingx, thingy, word):
	gameDisplay.blit(word, (thingx, thingy))

	
#設定汽車位置，注意：越右邊X越大，越上面Y越小，視窗的左上方是(0,0)
def car(x, y , score):
	global his_high_score
	if score >= his_high_score:
		gameDisplay.blit(carImg2, (x,y))
	else:
		gameDisplay.blit(carImg, (x,y))

def car2(x, y , score2, ufo):
	global his_high_score2
	gameDisplay.blit(ufo, (x,y))
	
#產生下個東西
def random_things(planet_height, PlanetRange):
	planet = random.choice(Picture2)
	thing_starty = 0 - planet_height - PlanetRange
	thing_startx = display_width/2 - planet_width/2 - 10
	return thing_startx, thing_starty, planet
		
#設定障礙物
def set_things(planet_height, PlanetRange):
	thing_startx = random.choice(runway) #X座標從跑道中任選一條
	thing_starty = 0 - planet_height - PlanetRange #因為如果從零開始的話，0會出現在畫面上
	word2 = random.choice(Picture)
	return thing_startx, thing_starty, word2

#檢查物品要吃與否 for easygame
def check_correct(word1):
	global Picture
	if (Picture.index(word1) == 0) or (Picture.index(word1) == 4) or (Picture.index(word1) == 8) or (Picture.index(word1) == 12) or (16 <=(Picture.index(word1)) <= 19):
		return True
	else:
		return False

#檢查物品要吃與否 for hardgame
def check_correct2(word1):
	global Picture2
	blue_list = [2, 5, 8, 9, 14]
	green_list = [0, 4, 7, 11, 12]
	red_list = [1, 3, 6, 10, 13]
	if Picture2.index(word1) in blue_list:
		return "blue"
	elif Picture2.index(word1) in green_list:
		return "green"
	elif Picture2.index(word1) in red_list:
		return "red"

#產生下個東西		
def make_next_things(thing_starty1, thing_starty2, display_height):
	global PlanetRange
	thing_starty1 = thing_starty2 - PlanetRange
	thing_startx1 = random.choice(runway)
	word_next = random.choice(Picture)
	return thing_startx1, thing_starty1, word_next

#吃到東西加分後重新生成新的	for easygame
def check_eat(thing_startx, thing_starty, thing_D_starty, channel1):
	global score
	channel1.play(pygame.mixer.Sound("eat.wav"))
	thing_startx += 10000
	score += 100
	pygame.display.update()
	thing_starty = thing_D_starty - PlanetRange 
	thing_startx = random.choice(runway)
	word = random.choice(Picture)
	return thing_starty, thing_startx, word

#吃到東西加分後重新生成新的	for hardgame	
def check_eat2(thing_startx, thing_starty, thing_D_starty, channel1): 
	global score2
	channel1.play(pygame.mixer.Sound("eat.wav"))
	thing_startx += 10000
	score2 += 100
	pygame.display.update()
	thing_starty = thing_D_starty - PlanetRange
	thing_startx = display_width/6 * 3 - planet_width/2 - 10
	word = random.choice(Picture2)
	return thing_starty, thing_startx, word
#=========================================================================================	
def main():  
	global SnakespeedCLOCK, gameDisplay, BASICFONT, user, his_high_score, score, his_high_score2, score2

	pygame.init()  
	SnakespeedCLOCK = pygame.time.Clock()  
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
				break_record()
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
				break_record2()
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
	x = (display_width/2 - car_width/2) #一開始設計在畫面正中央
	y = (display_height * 0.8)
	

	channel1 = pygame.mixer.Channel(0)
	#設定分數
	score = 0

	#設定初始值
	thing_speed = 5
	max_thing_speed = 7
	PlanetRange = 600
	
	
	#設定障礙物(五個)
	thing_startx, thing_starty, word = set_things(planet_height, (PlanetRange * 0))
	thing_A_startx, thing_A_starty, word_A = set_things(planet_height, (PlanetRange * 1))
	thing_B_startx, thing_B_starty, word_B = set_things(planet_height, (PlanetRange * 2))
	thing_C_startx, thing_C_starty, word_C = set_things(planet_height, (PlanetRange * 3))
	thing_D_startx, thing_D_starty, word_D = set_things(planet_height, (PlanetRange * 4))
	

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
		
		#檢查要吃與否
		checkTrue = check_correct(word)
		checkTrue_A = check_correct(word_A)
		checkTrue_B = check_correct(word_B)
		checkTrue_C = check_correct(word_C)
		checkTrue_D = check_correct(word_D)

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


		#things(thingx, thingy, word)
		things(thing_startx, thing_starty, word)
		thing_starty += thing_speed
		things(thing_A_startx, thing_A_starty, word_A)
		thing_A_starty += thing_speed
		things(thing_B_startx, thing_B_starty, word_B)
		thing_B_starty += thing_speed
		things(thing_C_startx, thing_C_starty, word_C)
		thing_C_starty += thing_speed
		things(thing_D_startx, thing_D_starty, word_D)
		thing_D_starty += thing_speed
				
		#設定汽車的位置
		car(x,y, score)
		
		#check_eat
		deadline = display_height - car_height
		if checkTrue == True:
			if (y < (thing_starty) and y + car_height >= thing_starty) and x == thing_startx:
				thing_starty, thing_startx, word = check_eat(thing_startx, thing_starty, thing_D_starty, channel1)
			elif thing_starty > deadline:
				return
			
		if checkTrue_A == True:
			if (y < (thing_A_starty) and y + car_height >= thing_A_starty) and x == thing_A_startx:
				thing_A_starty, thing_A_startx, word_A = check_eat(thing_A_startx, thing_A_starty, thing_starty, channel1)
			elif thing_A_starty > deadline:
				return
			
		if checkTrue_B == True:
			if (y < (thing_B_starty) and y + car_height >= thing_B_starty) and x == thing_B_startx:
				thing_B_starty, thing_B_startx, word_B = check_eat(thing_B_startx, thing_B_starty, thing_A_starty, channel1)
			elif thing_B_starty > deadline:
				return
			
		if checkTrue_C == True:
			if (y < (thing_C_starty) and y + car_height >= thing_C_starty) and x == thing_C_startx:
				thing_C_starty, thing_C_startx, word_C = check_eat(thing_C_startx, thing_C_starty, thing_B_starty, channel1)
			elif thing_C_starty > deadline:
				return
			
		if checkTrue_D == True:
			if (y < (thing_D_starty) and y + car_height >= thing_D_starty) and x == thing_D_startx:
				thing_D_starty, thing_D_startx, word_D = check_eat(thing_D_startx, thing_D_starty, thing_C_starty, channel1)
			elif thing_D_starty > deadline:
				return

		# 是否超越歷史紀錄
		if int(score) > int(his_high_score):
			his_high_score = score
			his_high_user = user

		#check crash
		if (y < (thing_starty) and y + car_height >= thing_starty) and checkTrue == False:
			if x == thing_startx:
				return #吃到錯誤的GAMOVER
				
		if (y < (thing_A_starty) and y + car_height >= thing_A_starty) and checkTrue_A == False:
			if x == thing_A_startx:
				return #吃到錯誤的GAMOVER
    
		if (y < (thing_B_starty) and y + car_height >= thing_B_starty) and checkTrue_B == False:
			if x == thing_B_startx:
				return #吃到錯誤的GAMOVER
		        
		if (y < (thing_C_starty) and y + car_height >= thing_C_starty) and checkTrue_C == False:
			if x == thing_C_startx:
				return #吃到錯誤的GAMOVER
				
		if (y < (thing_D_starty) and y + car_height >= thing_D_starty) and checkTrue_D == False:
			if x == thing_D_startx:
				return #吃到錯誤的GAMOVER
		
		#星球超過下界，就再生成一個新的
		if thing_starty > display_height:
			thing_startx, thing_starty, word = make_next_things(thing_starty, thing_D_starty, display_height)	
		if thing_A_starty > display_height:
			thing_A_startx, thing_A_starty, word_A = make_next_things(thing_A_starty, thing_starty, display_height)
		if thing_B_starty > display_height:
			thing_B_startx, thing_B_starty, word_B = make_next_things(thing_B_starty, thing_A_starty, display_height)
		if thing_C_starty > display_height:			
			thing_C_startx, thing_C_starty, word_C = make_next_things(thing_C_starty, thing_B_starty, display_height)
		if thing_D_starty > display_height:
			thing_D_startx, thing_D_starty, word_D = make_next_things(thing_D_starty, thing_C_starty, display_height)		
			
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


def runGame2():
	global his_high_score2, score2, PlanetRange, planet_height
	x = (display_width/2 - car_width2/2) #一開始設計在畫面正中央
	y = (display_height * 0.8)
	
	channel1 = pygame.mixer.Channel(0)
	#設定分數
	score2 = 0
	#設定一開始的ufo
	ufo = carImg_blue
	ufo_color = "blue"
	
	#設定初始值
	thing_speed = 5
	max_thing_speed = 7	
	PlanetRange = 600
	
	#設定障礙物(五個)
	thing_startx, thing_starty, word = random_things(planet_height, (PlanetRange * 0))
	thing_A_startx, thing_A_starty, word_A = random_things(planet_height, (PlanetRange * 1))
	thing_B_startx, thing_B_starty, word_B = random_things(planet_height, (PlanetRange * 2))
	thing_C_startx, thing_C_starty, word_C = random_things(planet_height, (PlanetRange * 3))
	thing_D_startx, thing_D_starty, word_D = random_things(planet_height, (PlanetRange * 4))
	
	
	# 讓背景動起來(1/2) - 設定背景的位置參數初始值
	bg_speed = 3
	bg_x1 = 0
	bg_x2 = 0
	bg_y1 = 0
	bg_y2 = - display_height    
	word = random.choice(Picture2)
	
	#while迴圈
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
			#設定按按鍵時汽車會位移
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ufo = carImg_blue
					ufo_color = "blue"
				elif event.key == pygame.K_RIGHT:
					ufo = carImg_green
					ufo_color = "green"
				elif event.key == pygame.K_DOWN:
					ufo = carImg_red
					ufo_color = "red"
		
		#檢查要吃與否
		checkTrue = check_correct2(word)
		checkTrue_A = check_correct2(word_A)
		checkTrue_B = check_correct2(word_B)
		checkTrue_C = check_correct2(word_C)
		checkTrue_D = check_correct2(word_D)

		#設定背景顏色，需特別注意，此條為將螢幕刷成同一顏色，若物件的函數寫在這之前，就會被刷成同一顏色而無法辨認
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
			PlanetRange = 500
			thing_speed = 5 #用來加速 

		elif 300 <= score2 < 500:
			PlanetRange = 400
			thing_speed = 6 #用來加速 

			
		elif 500 <= score2 < 1000:
			PlanetRange = 300
			thing_speed = 7 #用來加速 

			
		elif score2 >= 1000:
			PlanetRange = 200
			thing_speed = 8 #用來加速 


		#things(thingx, thingy, word)
		things(thing_startx, thing_starty, word)
		thing_starty += thing_speed
		things(thing_A_startx, thing_A_starty, word_A)
		thing_A_starty += thing_speed
		things(thing_B_startx, thing_B_starty, word_B)
		thing_B_starty += thing_speed
		things(thing_C_startx, thing_C_starty, word_C)
		thing_C_starty += thing_speed
		things(thing_D_startx, thing_D_starty, word_D)
		thing_D_starty += thing_speed
				
		#設定汽車的位置
		car2(x,y, score2, ufo)
		
		#check_eat
		deadline = display_height - car_height
		if checkTrue == ufo_color:
			if (y < (thing_starty) and y + car_height >= thing_starty):
				thing_starty, thing_startx, word = check_eat2(thing_startx, thing_starty, thing_D_starty, channel1)

			
		if checkTrue_A == ufo_color:
			if (y < (thing_A_starty) and y + car_height >= thing_A_starty):
				thing_A_starty, thing_A_startx, word_A = check_eat2(thing_A_startx, thing_A_starty, thing_starty, channel1)

			
		if checkTrue_B == ufo_color:
			if (y < (thing_B_starty) and y + car_height >= thing_B_starty):
				thing_B_starty, thing_B_startx, word_B = check_eat2(thing_B_startx, thing_B_starty, thing_A_starty, channel1)
			
		if checkTrue_C == ufo_color:
			if (y < (thing_C_starty) and y + car_height >= thing_C_starty):
				thing_C_starty, thing_C_startx, word_C = check_eat2(thing_C_startx, thing_C_starty, thing_B_starty, channel1)
			
		if checkTrue_D == ufo_color:
			if (y < (thing_D_starty) and y + car_height >= thing_D_starty):
				thing_D_starty, thing_D_startx, word_D = check_eat2(thing_D_startx, thing_D_starty, thing_C_starty, channel1)

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
		SnakespeedCLOCK.tick(50)
		pygame.display.update()
	
#啟動主遊戲迴圈        
if __name__ == '__main__':  
	try:  
		main()  
	except SystemExit:  
		pass        
