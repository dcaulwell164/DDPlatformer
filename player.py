import pygame
class Player:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.color = (255, 0, 0)
        self.rect = (x,y,width,height)
        self.isJumping = False
        self.isFalling = False
        self.initialY = y
        self.jumpVel = 10
        self.fallVel = 5
        self.jump_height = 100
        self.jump_count = self.jump_height

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if self.isJumping:
            self.jump()

        if keys[pygame.K_SPACE]:
            if not self.isJumping:
                self.isJumping = True

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def jump(self):
        if self.y != (self.initialY - self.jump_height) and not self.isFalling:
            self.y -= self.jumpVel
        
        if self.y > self.initialY:
            self.y = self.initialY
            self.isJumping = False
            self.isFalling = False
            return

        if self.y == (self.initialY - self.jump_height):
            self.isFalling = True
        
        if self.isFalling:
            self.y += self.fallVel


        
        
