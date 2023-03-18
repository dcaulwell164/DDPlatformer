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

        if keys[pygame.K_SPACE]:
            self.isJumping = True

        if self.isJumping:
            self.jump()

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def jump(self):
        if self.jump_count >= -self.jump_height:
            neg = 1
            if self.jump_count < 0:
                neg = -1
            self.y -= (self.jump_count ** 2) * 0.5 * neg
            self.jump_count -= 1
        else:
            self.is_jumping = False
            self.jump_count = self.jump_height
        
