import pygame

YELLOW = (252,186,3)
CYAN = (3,252,236)
PURPLE = (182,3,252)

class Coin:

    def __init__(self, type):
        self.type = type
        self.value = self.get_value()
        self.position = (20,20)

    
    def get_value(self):
        if self.type == "small":
            return 2
        elif self.type == "medium":
            return 5
        elif self.type == "large":
            return 8
        else:
            return None
    
    def get_colour(self):
        if self.type == "small":
            return CYAN
        elif self.type == "medium":
            return PURPLE
        elif self.type == "large":
            return YELLOW
        else:
            return None

    def draw(self,window):
        pygame.draw.rect(window,self.get_colour(), self)
            