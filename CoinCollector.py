import pygame, time
from Player import Player
from Coin import Coin
pygame.font.init()

#Create the window and tick rate
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Coin Collector v0.1")
WINDOW_COLOUR = (234,126,84)
FONT_COLOUR = (255,255,255)
FPS = 60
MONEY_FONT = pygame.font.SysFont("comicsans", 40)
BTN_TEXT = pygame.font.SysFont("comicsans", 30) 

#Coin stuff
MAX_COINS = 5
coins = []



#game variables
ROUND_TIME = 15
startTime = time.time()
endTime = startTime + ROUND_TIME
inRound = False
timeLeft = 0
player = None
mouse = pygame.mouse.get_pos()

#gui buttons
BTN_COLOUR = (145,67,40)
increaseSpeedBtn = pygame.Rect(10,50,220,35)
increaseMaxCoinsBtn = pygame.Rect(10,90,260,35)
startRoundBtn = pygame.Rect(WIDTH-150,10,130,35)
increaseValueSmallBtn = pygame.Rect(10,130,280,35)
increaseValueMediumBtn = pygame.Rect(10,170,280,35)
increaseValueLargeBtn = pygame.Rect(10,210,280,35)
increaseTimerSmallBtn = pygame.Rect(10,250,280,35)
increaseTimerMediumBtn = pygame.Rect(10,290,280,35)
increaseTimerLargeBtn = pygame.Rect(10,330,280,35)


def handle_movement(keys_pressed,player):
    player.move(keys_pressed,WIN)
    index = pygame.Rect.collidelist(player.rect,coins)
    if index != -1:
        coin_hit = coins[index]
        player.hit_coin(coin_hit)
        coins.remove(coin_hit)


def try_generate_coins():
    if len(coins) < MAX_COINS:
        for i in range(len(coins),MAX_COINS,1):
            coin = Coin(WIN)
            if pygame.Rect.collidelist(coin.rect,coins) == -1:
                coins.append(coin)



def draw_window(player, coins, timeLeft):
    WIN.fill(WINDOW_COLOUR)    
    money_text = MONEY_FONT.render("Money: £" + str(player.money), 1, FONT_COLOUR)
    
    timer_text = MONEY_FONT.render("" + str(timeLeft // 1), 1, FONT_COLOUR)
    WIN.blit(money_text, (10,10))
    WIN.blit(timer_text, (WIDTH-200,10))
    player.draw(WIN)
    for coin in coins:
        coin.draw(WIN)


    pygame.display.update()



def start_round():
    global inRound, startTime, endTime, timeLeft
    startTime = time.time()
    endTime = startTime + ROUND_TIME
    inRound = True
    timeLeft = endTime - time.time()
    player.rect.x = WIDTH/2
    player.rect.y = HEIGHT/2
    player.draw(WIN) 

def draw_end_of_round():
    #draw buttons       
    pygame.draw.rect(WIN, BTN_COLOUR,increaseSpeedBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseMaxCoinsBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, startRoundBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseValueSmallBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseValueMediumBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseValueLargeBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseTimerSmallBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseTimerMediumBtn)
    pygame.draw.rect(WIN, BTN_COLOUR, increaseTimerLargeBtn)

    #text on buttons
    increaseSpeedBtn_text = BTN_TEXT.render("Increase Speed (£50)" , 1, FONT_COLOUR)
    increaseMaxCoinsBtn_text = BTN_TEXT.render("Increase Max Coins (£75)" , 1, FONT_COLOUR)
    startRoundBtn_text = BTN_TEXT.render("Next Round" , 1, FONT_COLOUR)
    increaseValueSmall_text = BTN_TEXT.render("Increase small value (£80)" , 1, FONT_COLOUR)
    increaseValueMedium_text = BTN_TEXT.render("Increase medium value (£50)" , 1, FONT_COLOUR)
    increaseValueLarge_text = BTN_TEXT.render("Increase large value (£35)" , 1, FONT_COLOUR)
    increaseTimerSmall_text = BTN_TEXT.render("Increase small timer (£100)" , 1, FONT_COLOUR)
    increaseTimerMedium_text = BTN_TEXT.render("Increase medium timer (£80)" , 1, FONT_COLOUR)
    increaseTimerLarge_text = BTN_TEXT.render("Increase large timer (£55)" , 1, FONT_COLOUR)

    WIN.blit(increaseSpeedBtn_text, (increaseSpeedBtn.x +5, increaseSpeedBtn.y+5) )
    WIN.blit(increaseMaxCoinsBtn_text, (increaseMaxCoinsBtn.x +5, increaseMaxCoinsBtn.y+5) )
    WIN.blit(startRoundBtn_text, (startRoundBtn.x +5, startRoundBtn.y+5) )
    WIN.blit(increaseValueSmall_text, (increaseValueSmallBtn.x +5, increaseValueSmallBtn.y+5) )
    WIN.blit(increaseValueMedium_text, (increaseValueMediumBtn.x +5, increaseValueMediumBtn.y+5) )
    WIN.blit(increaseValueLarge_text, (increaseValueLargeBtn.x +5, increaseValueLargeBtn.y+5) )
    WIN.blit(increaseTimerSmall_text, (increaseTimerSmallBtn.x +5, increaseTimerSmallBtn.y+5) )
    WIN.blit(increaseTimerMedium_text, (increaseTimerMediumBtn.x +5, increaseTimerMediumBtn.y+5) )
    WIN.blit(increaseTimerLarge_text, (increaseTimerLargeBtn.x +5, increaseTimerLargeBtn.y+5) )
    pygame.display.update()

def end_round():
    global inRound, timeLeft, player
    inRound = False
    timeLeft = 0
    draw_end_of_round()
    

    


def handle_mouse_click(mousePos):
    if not inRound:
        if pygame.Rect.collidepoint(startRoundBtn, mousePos):
            start_round()
        if pygame.Rect.collidepoint(increaseSpeedBtn, mousePos):
            if player.money >= 50:
                player.increase_speed()
        if pygame.Rect.collidepoint(increaseMaxCoinsBtn, mousePos):
            if player.money >= 75:
                global MAX_COINS
                MAX_COINS += 1
                player.money -= 75
        if pygame.Rect.collidepoint(increaseValueSmallBtn, mousePos):
            if player.money >= 80:
                player.money -= 80
                Coin.SMALL_VALUE += 2
        if pygame.Rect.collidepoint(increaseValueMediumBtn, mousePos):
            if player.money >= 50:
                player.money -= 50
                Coin.MEDIUM_VALUE += 2
        if pygame.Rect.collidepoint(increaseValueLargeBtn, mousePos):
            if player.money >= 35:
                player.money -= 35
                Coin.LARGE_VALUE += 2
        if pygame.Rect.collidepoint(increaseTimerSmallBtn, mousePos):
            if player.money >= 100:
                player.money -= 100
                Coin.SMALL_TIMER += 2
        if pygame.Rect.collidepoint(increaseTimerMediumBtn, mousePos):
            if player.money >= 80:
                player.money -= 80
                Coin.MEDIUM_TIMER += 2
        if pygame.Rect.collidepoint(increaseTimerLargeBtn, mousePos):
            if player.money >= 55:
                player.money -= 55
                Coin.LARGE_TIMER += 2
                
        draw_window(player,coins,0.0)
        draw_end_of_round()
        

def check_for_coin_destroy():
    for coin in coins:
        if time.time() >= coin.destroy:
            coins.remove(coin)
            try_generate_coins()

def run():
    global inRound,timeLeft,player, mouse
    run = True
    clock = pygame.time.Clock()
    #Create the player
    player = Player((WIDTH/2,HEIGHT/2), money=1500)
    
    
    #start the first round
    start_round()
    

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                handle_mouse_click(mouse)
            

        if inRound:
            #handle key presses
            keys_pressed = pygame.key.get_pressed()
            handle_movement(keys_pressed,player)

            #generate coins
            try_generate_coins()
            #update display
            draw_window(player,coins,timeLeft)

            #check to see if any coins have reached their destroy time
            check_for_coin_destroy()

        timeLeft = endTime - time.time()
        if inRound and timeLeft <= 0:
            end_round()


if __name__ == "__main__":
    run()