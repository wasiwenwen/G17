import pygame, time, random

#啟動
pygame.init() 

#設定視窗大小
display_width = 800
display_height = 600

#設定要使用的顏色的RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#設定汽車寬度(查圖片像素)
car_width = 74

#建立視窗(根據上面的基本設定)
gameDisplay = pygame.display.set_mode((display_width, display_height))

#設定跑道x軸大小
runway = [0, 300, 700]

#設定視窗標題
pygame.display.set_caption("Cars")

#設定時間
clock = pygame.time.Clock()

#讀入圖片
carImg = pygame.image.load("car1.gif")

Picture = []
pic1 = pygame.image.load("pic1.png")
Picture.append(pic1)
pic2 = pygame.image.load("pic2.png")
Picture.append(pic2)
pic3 = pygame.image.load("pic3.png")
Picture.append(pic3)
pic4 = pygame.image.load("pic4.png")
Picture.append(pic4)
pic5 = pygame.image.load("pic5.png")
Picture.append(pic5)
pic6 = pygame.image.load("pic6.png")
Picture.append(pic6)
pic7 = pygame.image.load("pic7.png")
Picture.append(pic7)
pic8 = pygame.image.load("pic8.png")
Picture.append(pic8)
pic9 = pygame.image.load("pic9.png")
Picture.append(pic9)



#建立障礙物
def things(thingx, thingy, word):
    gameDisplay.blit(word, (thingx, thingy))

    
#設定汽車位置，注意：越右邊X越大，越上面Y越小，視窗的左上方是(0,0)
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

    
#以下這三個def都是在定義crash()的狀況    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()    
    
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115) #設定要顯示的字型及大小
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect) 
    
    pygame.display.update()
    
    time.sleep(2)
    game_loop()
        
def crash():
    message_display("You Crashed!")


    
#主遊戲迴圈    
def game_loop():    
    x =(display_width * 0.45)
    y = (display_height * 0.8)

    #設定汽車位移    
    x_change = 0

    #設定障礙物
    thing_startx = random.choice(runway) #X座標從跑道中任選一條
    thing_starty = -600 #因為如果從零開始的話，0會出現在畫面上
    thing_speed = 7
    word = random.choice(Picture)
    word2 = word
        
    #預設汽車沒有撞到    
    gameExit = False

    #while迴圈
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            #設定按按鍵時汽車會位移
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        #加上x的變化值
        x += x_change
        
        #設定背景顏色，需特別注意，此條為將螢幕刷成同一顏色，若物件的函數寫在這之前，就會被刷成同一顏色而無法辨認
        gameDisplay.fill((0,255,0))
        
        
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, word2)
        thing_starty += thing_speed 
        

        #設定汽車的位置
        car(x,y)
        
        
        #判斷車子是否超過畫面限制(crash)
        if x > display_width - car_width or x < 0: #要剪掉car_width是因為，電腦是依據圖片「左上角」的點做判斷
            crash()
  
        #如果障礙物已超過畫面，就要再出現下一個障礙物
        if thing_starty > display_height : #注意，Y越下方越大
            thing_speed += 1  #用來加速
            thing_starty = 0 - 30
            thing_startx = random.choice(runway)
            word = random.choice(Picture)
            word2 = word
            
        pygame.display.update() #pygame.display.flip()也可以
        
        #設定每秒多少動畫窗格。若要有增加速度的感覺，可以增加數字
        clock.tick(60)

        
#啟動主遊戲迴圈        
game_loop()        

#結束    
pygame.quit()    
quit()