import pygame
from shot import Shot
class Player:

    def __init__(self, x, y, width, height, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.color = (255, 0, 0)
        self.player_image = pygame.image.load('player.png')
        self.rect = self.player_image.get_rect(x=x, y=y)
        self.shot = Shot(x, y, False)
        self.window = window

    def draw(self, win):
        # pygame.draw.rect(win, self.color, self.rect)
        image = pygame.transform.scale(self.player_image, (self.player_image.get_width() * 3, self.player_image.get_height() * 3))
        win.blit(image, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < 800:
            self.x += self.vel

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.update()
        self.shot.move()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def shoot(self):
        if not self.shot.active:
            self.shot = Shot(self.x, self.y, True)
            self.shot.draw(self.window)
        




        
        
