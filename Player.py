import pygame


PLAYER_COLOUR = (186,232,78)

class Player:

    def __init__(self, position, money = 0):
        self.money = 0
        self.colour = PLAYER_COLOUR
        self.position =  position
        self.size = 20
        self.rect = pygame.Rect((self.position), (self.size,self.size))
        self.speed = 5
    
    def move(self,keys_pressed,window):
        if keys_pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d] and self.rect.x + self.size < window.get_size()[0]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_w] and self.rect.y  > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.y + self.size  < window.get_size()[1] :
            self.rect.y += self.speed