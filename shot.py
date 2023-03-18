import pygame
class Shot:

    def __init__(self,x,y, active):
        self.shoot_image = pygame.image.load('sperm.png')
        self.vel = 5
        self.x = x
        self.y = y
        self.rect = self.shoot_image.get_rect(x=x, y=y)
        self.active = active

    def move(self):
        if self.y < 600:
            self.y -= self.vel
        else:
            self.active = False

        self.update()

    def draw(self, win):
        win.screen.blit(self.shoot_image, self.rect)

    def update(self):
        self.rect = self.shoot_image.get_rect(x=self.x, y=self.y)
