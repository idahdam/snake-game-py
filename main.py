# learning day 2
import pygame, time, random, sys

pygame.init()
sys.setrecursionlimit(10000)

# color can be tuple can be list
white = (255,255,255)
black = (0,0,0)
red = (150,0,0)
light_red = (255, 0, 0)
fav = (84, 213, 233)
#green = (0, 175, 0)
green = (0, 75, 0)
light_green = (0, 255, 0)
yellow = (170, 170, 0)
light_yellow = (255, 255, 0)
light_white = (255, 219, 219)

# calling sprite
head_img = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/head.png')
apple = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/apple.png')
icon = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/icon.png')
tail = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/tail.png')
back_menu = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/back-menu.png')
back_pause = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/back-pause.png')
back_game = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/back-game.png')
back_about = pygame.image.load('C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/images/back-about.png')

# variabele display
display_width = 800
display_height = 600
borderX = 550
borderY = 750
pinggirkiri = 22
pinggirbawah = 120

# block_size hehehe
block_size = 20

# apple thickness
appleThickness = 25

# str direction
direction = "up"

# snake func, expanding snake if it eats an apple
def snake(block_size, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(head_img, 270)
    
    if direction == "left":
        head = pygame.transform.rotate(head_img, 90)
    
    if direction == "up":
        head = head_img
    
    if direction == "down":
        head = pygame.transform.rotate(head_img, 180)

    # below will add to  list for everything but the head
    for XnY in snakeList[:-1]:
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))


# set screen, title, and icon
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake 1.0')
pygame.display.set_icon(icon)

# pygame clock for fps
clock = pygame.time.Clock()

# fps default 30
FPS = 20

# font, (font, size)
smallfont = pygame.font.Font("C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/ARCADE_N.ttf", 25)
mediumfont = pygame.font.Font("C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/ARCADE_N.ttf", 30)
bigfont = pygame.font.Font("C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/ARCADE_N.ttf", 50)  
verysmallfont = pygame.font.Font("C:/Users/idahdam/Documents/proyek pribadi/GUI/studying/ARCADE_N.ttf", 19) 

# size = 25 is a default value --> def text_objects(text, color, size = 25)
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    if size == "large":
        textSurface = bigfont.render(text, True, color)  
    if size == "verysmall":         
        textSurface = verysmallfont.render(text, True, color)   
    return textSurface, textSurface.get_rect()

# func text color, + # size = "small"
def message_to_screen(msg, color, y_displace = 0, size = "small", x_displace = 0):
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, (display_width/2, display_height/2))
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2)+x_displace, (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def randApple():
    # random position apple, we make em move 10px each with round
    randAppleX = round(random.randrange(50, display_width-appleThickness-30)/10.0)*10.0
    randAppleY = round(random.randrange(50, display_height-appleThickness-140)/10.0)*10.0

    return randAppleX, randAppleY

#def score(score):
 #   text = smallfont.render("Score: " + str(score), True, red)
  #  gameDisplay.blit(text, (0, 0))

def pausemenu():
    pause = True
    if pause == True:
        gameDisplay.blit(back_pause, (0,0))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_b:
                    mainmenu()
        
        #gameDisplay.fill(fav)
        pygame.display.update()
        clock.tick(5)
                
def mainmenu():

    intro = True
    while intro:
        gameDisplay.blit(back_menu, (0,0))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    gameLoop()

        
        #print(cursor)

        #if 150+150 > cursor[0] > 150 and 400+50 > cursor[1] > 400:
        #    pygame.draw.rect(gameDisplay, light_green, (150, 400, 150, 50))
        #else:
        #    pygame.draw.rect(gameDisplay, green, (150, 400, 150, 50))

        #pygame.draw.rect(gameDisplay, red, (350, 400, 150, 50))
        #pygame.draw.rect(gameDisplay, yellow, (550, 400, 150, 50))


        def button(msg, color, buttonx, buttony, buttonwidth, buttonheight, aftercolor, beforecolor, size="small", action=None):
            #cursor!!!
            cursor = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #print(click, cursor)
            if buttonx + buttonwidth > cursor[0] > buttonx and buttony + buttonheight > cursor[1] > buttony:
                #pygame.draw.rect(gameDisplay, beforecolor, (buttonx, buttony, buttonwidth, buttonheight))
                pygame.draw.rect(gameDisplay, beforecolor, (buttonx, buttony, buttonwidth, buttonheight))
                if click[0] == 1 and action != None:
                    if action == "play":
                        gameLoop()
                    elif action == "quit":
                        pygame.quit()
                        quit()
                    elif action == "About":
                        about()
            else:
                #pygame.draw.rect(gameDisplay, aftercolor, (buttonx, buttony, buttonwidth, buttonheight))
                pygame.draw.rect(gameDisplay, aftercolor, (buttonx, buttony, buttonwidth, buttonheight))
            #you can still make func of these statements below
            textSurf, textRect = text_objects(action, color, size)
            textRect.center = ((buttonx+(buttonwidth/2)),  (buttony+(buttonheight/2)))
            gameDisplay.blit(textSurf, textRect)
            #gameDisplay.blit(smallfont.render(action, True, black), (buttonx+buttonwidth,buttony+buttonheight))



        button("Play", black, 71, 169, 225, 65,  white, light_white, size="small", action="play")
        button("About", black, 71, 264, 225, 65, white, light_white, size="small", action="About")
        button("Exit", black, 71, 362, 225, 65, white, light_white, size="small", action="quit")

        #cmessage_to_screen("Start", white, x_displace=-200, y_displace=120, size='small')
        #message_to_screen("Start", white, x_displace=-200, y_displace=120, size='small')
        #message_to_screen("About", white, x_displace=0, y_displace=120, size='small')
        #message_to_screen("Exit", white, x_displace=200, y_displace=120, size='small')

        pygame.display.update()
        clock.tick(FPS)

def about():

    about = True
    while about:
        gameDisplay.blit(back_about, (0,0))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    gameLoop()

        
        #print(cursor)

        #if 150+150 > cursor[0] > 150 and 400+50 > cursor[1] > 400:
        #    pygame.draw.rect(gameDisplay, light_green, (150, 400, 150, 50))
        #else:
        #    pygame.draw.rect(gameDisplay, green, (150, 400, 150, 50))

        #pygame.draw.rect(gameDisplay, red, (350, 400, 150, 50))
        #pygame.draw.rect(gameDisplay, yellow, (550, 400, 150, 50))


        def button(msg, color, buttonx, buttony, buttonwidth, buttonheight, aftercolor, beforecolor, size="small", action=None):
            #cursor!!!
            cursor = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            #print(click, cursor)
            if buttonx + buttonwidth > cursor[0] > buttonx and buttony + buttonheight > cursor[1] > buttony:
                #pygame.draw.rect(gameDisplay, beforecolor, (buttonx, buttony, buttonwidth, buttonheight))
                pygame.draw.rect(gameDisplay, beforecolor, (buttonx, buttony, buttonwidth, buttonheight))
                if click[0] == 1 and action != None:
                    if action == "play":
                        gameLoop()
                    elif action == "quit":
                        pygame.quit()
                        quit()
                    elif action == "main":
                        mainmenu()
            else:
                #pygame.draw.rect(gameDisplay, aftercolor, (buttonx, buttony, buttonwidth, buttonheight))
                pygame.draw.rect(gameDisplay, aftercolor, (buttonx, buttony, buttonwidth, buttonheight))
            #you can still make func of these statements below
            textSurf, textRect = text_objects(action, color, size)
            textRect.center = ((buttonx+(buttonwidth/2)),  (buttony+(buttonheight/2)))
            gameDisplay.blit(textSurf, textRect)
            #gameDisplay.blit(smallfont.render(action, True, black), (buttonx+buttonwidth,buttony+buttonheight))



        button("Play", black, 71, 169, 225, 65,  white, light_white, size="small", action="play")
        button("Main", black, 71, 264, 225, 65, white, light_white, size="small", action="main")
        button("Exit", black, 71, 362, 225, 65, white, light_white, size="small", action="quit")
        button("April 22nd 2020", black, 271, 500, 225, 65, white, light_white, size="small", action="April 22nd 2020")

        #cmessage_to_screen("Start", white, x_displace=-200, y_displace=120, size='small')
        #message_to_screen("Start", white, x_displace=-200, y_displace=120, size='small')
        #message_to_screen("About", white, x_displace=0, y_displace=120, size='small')
        #message_to_screen("Exit", white, x_displace=200, y_displace=120, size='small')

        pygame.display.update()
        clock.tick(FPS)


def gameLoop():
    global direction

    randAppleX, randAppleY = randApple()

    lead_x = display_width/2
    lead_y = display_height/2
    snakeLength = 1
    snakeList = [] 

    
    # block pos


    # random position apple, we make em move 10px each with round
    #andAppleX = round(random.randrange(0, display_width-appleThickness))#10.0)*10.0
    #randAppleY = round(random.randrange(0, display_height-appleThickness))#10.0)*10.0

    # jadi fungsi
    #randApple()

     #--showapple
    def show_apple(appleThickness):
        gameDisplay.blit(apple, (randAppleX, randAppleY))
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])

    # block position change
    lead_x_change = 0
    lead_y_change = 0

    #--score
    score = 0

    # condition
    gameExit = True
    gameOver = False

    #if gameExit:
        
    while gameExit:

        while gameOver == True:
            #gameDisplay.fill(fav)
            message_to_screen("Game over", 
                                red, 
                                -50,
                                size="large")
            message_to_screen("Press C to play again or Q to quit",
                                black,
                                10,
                                size="verysmall")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = False
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausemenu()
                elif event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0 
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0 
                    direction = "right"
                elif event.key == pygame.K_UP:
                    
                    lead_y_change = -block_size
                    lead_x_change = 0 
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
        
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(cursor)
                
        #--score
        # score 
            #if event.type == pygame.KEYUP:
            #   if event.key == pygame.K_LEFT:
            #       lead_x_change = 0
            #   elif event.key == pygame.K_RIGHT:
            #       lead_x_change = 0
            #   elif event.key == pygame.K_UP:
            #       lead_y_change = 0 
            #   elif event.key == pygame.K_DOWN:
            #       lead_y_change = 0 
        
        # border
        if lead_x +block_size >= display_width - 10 or lead_x < 20 or lead_y + block_size>= display_height - 90 - 22 or lead_y<20:  
        #if lead_x >= pinggirkiri and lead_x + block_size < display_width - pinggirkiri or lead_y >= display_height - pinggirbawah - 22 or lead_y<22:  
            del snakeList[:]
            lead_x, lead_y = (1000, 1000) #hilang
            randAppleX, randAppleY = (1000, 1000)
            gameOver = True

        def score(score):
            text = smallfont.render("Score: " + str(score), True, black)
            a = text.get_rect(center=(150, 540))
            gameDisplay.blit(text, a)
            print(score)

        
        lead_x += lead_x_change
        lead_y += lead_y_change

        # .fill param(color, rect=[xpos, ypos, width, height])
        # if theres no rect, pygame assuming fullscreen color
        #gameDisplay.fill(fav)
        gameDisplay.blit(back_game, (0,0))

        # for each in range (:-1) segment of a snake
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                lead_x, lead_y = (1000,1000)
                gameOver = True
                print("game over! c to continue/q to quit")

        # snakelist
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # kerjaan besok <D
        snakeTail = []

        #limiting snakelength
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # param for .draw.rect(where to draw, color, [xpos, ypos, width, height])
        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])
        show_apple(appleThickness)
        snake(block_size, snakeList)
        
        score(snakeLength-1)
        
        # first crossover
         #if lead_x == randAppleX and lead_y == randAppleY:
         #   randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
         #   randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
         #   snakeLength += 1

        # 2nd crossover, with custom made apple thickness
        #if lead_x > randAppleX and lead_x < randAppleX + appleThickness:
        #    if lead_y > randAppleY and lead_y < randAppleY + appleThickness:
        #        randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        #        randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        #        snakeLength += 1
        #        show_apple(appleThickness)


        # 3rd crossover full, hayo bayangin
        if lead_x >= randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size >= randAppleX and lead_x + block_size < randAppleX + appleThickness:
            #print("x crossover!")
            if lead_y >= randAppleY and lead_y < randAppleY + appleThickness or lead_y + block_size >= randAppleY and lead_y + block_size < randAppleY + appleThickness:
                #print("x and y crossover!")
                randAppleX = round(random.randrange(50, display_width-appleThickness-30)/10.0)*10.0
                randAppleY = round(random.randrange(50, display_height-block_size-140)/10.0)*10.0
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                #print("x and y crossover!")
                randAppleX = round(random.randrange(50, display_width-appleThickness-30))#/10.0)*10.0
                randAppleY = round(random.randrange(50, display_height-block_size-140)/10.0)*10.0
                snakeLength += 1

        #update screen
        pygame.display.update()
    
        # calling the clock func
        clock.tick(FPS)

    pygame.quit()
    quit()

# game loop truly starts here
mainmenu()
gameLoop()
