import pygame, random

YELLOW = (252,186,3)
CYAN = (3,252,236)
PURPLE = (182,3,252)

SMALL_SIZE = 12,12
MEDIUM_SIZE = 18,18
LARGE_SIZE = 24,24

class Coin:

    def __init__(self, window):
        self.randomType = self.get_type()
        self.type = self.randomType
        self.value = self.get_value()
        self.size = 10
        self.position = (random.randint(0,window.get_size()[0]), random.randint(0,window.get_size()[1]-self.size))
        self.rect = pygame.Rect((self.position), self.get_size())

    def get_size(self):
        if self.type == "small":
            return LARGE_SIZE
        elif self.type == "medium":
            return MEDIUM_SIZE
        elif self.type == "large":
            return SMALL_SIZE
        else:
            return None
    
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

    def get_type(self):
        types = ["small", "medium", "large"]
        return types[random.randrange(0,len(types))]
            