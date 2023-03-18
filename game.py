import pygame
from window import Window
from player import Player
import os

class Game:
    


    def __init__(self, width, height):
        pygame.init()
        self.init_music()
        self.windowWidth = width
        self.WindowHeight = height
        self.window = Window(width, height, "My Platformer Game")
        self.clock = pygame.time.Clock()
        self.player = Player(width/2-50, height-150, 10, 10, self.window)

    def init_music(self):
        pygame.mixer.init()
        music_file = os.path.join("./musiq.mp3")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

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

        
