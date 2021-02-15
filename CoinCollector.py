import pygame
from Player import Player
from Coin import Coin
#pygame.init()

#Create the window and tick rate
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Coin Collector v0.1")
WINDOW_COLOUR = (234,126,84)
FPS = 60

#Coin stuff
MAX_COINS = 7
coins = []


def handle_movement(keys_pressed,player):
    player.move(keys_pressed,WIN)
    
def try_generate_coins():
    if len(coins) < MAX_COINS:
        for i in range(len(coins),MAX_COINS,1):
            coin = Coin(WIN)
            if pygame.Rect.collidelist(coin.rect,coins) == -1:
                coins.append(coin)



def draw_window(player, coins):
    WIN.fill(WINDOW_COLOUR)    
    player.draw(WIN)

    for coin in coins:
        coin.draw(WIN)


    pygame.display.update()

def run():
    run = True
    clock = pygame.time.Clock()
    #Create the player
    player = Player((WIDTH/2,HEIGHT/2), money=35)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        #handle key presses
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed,player)

        #generate coins
        try_generate_coins()

        #update display
        draw_window(player,coins)


if __name__ == "__main__":
    run()