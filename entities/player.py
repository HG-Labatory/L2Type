import pygame

class Player:

    def __init__(self, x, y, width, height, color) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def get_rect(self):
        #create rectangle
        return pygame.Rect(self.x,self.y, self.width, self.height)

    def draw(self, screen):
        #draw rectangle
        return pygame.draw.rect(screen, self.color, self.get_rect())
