import pygame, random, time

YELLOW = (252,186,3)
CYAN = (3,252,236)
PURPLE = (182,3,252)

SMALL_SIZE = 12,12
MEDIUM_SIZE = 18,18
LARGE_SIZE = 24,24

SMALL_TIMER = 3
MEDIUM_TIMER = 6
LARGE_TIMER = 10

SMALL_VALUE = 10
MEDIUM_VALUE = 5
LARGE_VALUE = 3

class Coin:

    def __init__(self, window):
        self.randomType = self.get_type()
        self.type = self.randomType
        self.value = self.get_value()
        self.size = 10
        self.position = random.randint(0,window.get_size()[0] - self.size), random.randint(0,window.get_size()[1]-self.size)
        self.rect = pygame.Rect((self.position), self.get_size())
        self.destroy = time.time() + self.set_timer()

    def set_timer(self):
        if self.type == "large":
            return LARGE_TIMER
        elif self.type == "medium":
            return MEDIUM_TIMER
        elif self.type == "small":
            return SMALL_TIMER
        else:
            return None

    def get_size(self):
        if self.type == "large":
            return LARGE_SIZE
        elif self.type == "medium":
            return MEDIUM_SIZE
        elif self.type == "small":
            return SMALL_SIZE
        else:
            return None
    
    def get_value(self):
        if self.type == "small":
            return SMALL_VALUE
        elif self.type == "medium":
            return MEDIUM_VALUE
        elif self.type == "large":
            return LARGE_VALUE
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

            