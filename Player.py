import pygame


PLAYER_COLOUR = (186,232,78)

class Player:

    def __init__(self, position, money = 0):
        self.money = money
        self.colour = PLAYER_COLOUR
        self.position =  position
        self.size = 27
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

    def draw(self,window):
        pygame.draw.rect(window,self.colour, self)

    def hit_coin(self, coin):
        self.money += coin.get_value()

    def increase_speed(self):
        self.speed += 1
        self.money -= 50