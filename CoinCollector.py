import pygame
from Player import Player
#pygame.init()

#Create the window and tick rate
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Coin Collector v0.1")
WINDOW_COLOUR = (234,126,84)
FPS = 60


def handle_movement(keys_pressed,player):
    player.move(keys_pressed,WIN)
    




def draw_window(player):
    WIN.fill(WINDOW_COLOUR)
    #WIN.blit(player.rect, (player.position[0],player.position[1]))
    #pygame.draw.rect(WIN,player.colour, player)
    player.draw(WIN)
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

        #update display
        draw_window(player)


if __name__ == "__main__":
    run()