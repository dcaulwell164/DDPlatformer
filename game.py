import pygame
from window import Window
from player import Player

class Game:
    


    def __init__(self, width, height):
        pygame.init()
        self.windowWidth = width
        self.WindowHeight = height
        self.window = Window(width, height, "My Platformer Game")
        self.clock = pygame.time.Clock()
        self.player = Player(50, 300, 10, 10)

    def redrawWindow(self):
        self.window.fill()
        self.player.draw(self.window.screen)
        pygame.display.update()

    def run(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Call the game loop function
            self.game_loop()
            # Limit to 60 frames per second
            self.clock.tick(60)
        
        # Quit Pygame
        pygame.quit()
        
    def game_loop(self):
        self.player.move()
        self.redrawWindow()

        
