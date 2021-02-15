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
MAX_COINS = 20
coins = []



#game variables
ROUND_TIME = 4
startTime = time.time()
endTime = startTime + ROUND_TIME
inRound = False
timeLeft = 0
player = None
mouse = pygame.mouse.get_pos()

#gui buttons
increaseSpeedBtn = pygame.Rect(10,50,220,35)

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

def end_round():
    global inRound, timeLeft, player
    inRound = False
    timeLeft = 0
    

    #buttons    
    pygame.draw.rect(WIN, (145,67,40),increaseSpeedBtn)
    increaseSpeedBtn_text = BTN_TEXT.render("Increase Speed (£50)" , 1, FONT_COLOUR)
    WIN.blit(increaseSpeedBtn_text, (increaseSpeedBtn.x +5, increaseSpeedBtn.y+5) )
    pygame.display.update()


def handle_mouse_click(mousePos):
    if not inRound:
        if pygame.Rect.collidepoint(increaseSpeedBtn, mousePos):
            if player.money >= 50:
                player.increase_speed()
                draw_window(player,coins,0.0)


def run():
    global inRound,timeLeft,player, mouse
    run = True
    clock = pygame.time.Clock()
    #Create the player
    player = Player((WIDTH/2,HEIGHT/2), money=35)
    
    
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
        else:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_q]:
                start_round()

        

        timeLeft = endTime - time.time()
        if timeLeft <= 0:
            end_round()


if __name__ == "__main__":
    run()