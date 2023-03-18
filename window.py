import pygame

class Window:

    def __init__(self, width, height, caption):
        
        self.width = width
        self.height = height
        self.caption = caption
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.fill()

    def fill(self):
        self.screen.fill(self.WHITE)
        # self.drawMap()

    def drawMap(self):
        rect = (0,350, self.width, self.height-310)
        pygame.draw.rect(self.screen, (0,255, 0), rect)
        
    
        

