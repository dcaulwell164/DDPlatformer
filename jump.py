import pygame

# Initialize Pygame
pygame.init()

# Set up the display
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Jumping Player")

# Set up the player
player_width = 50
player_height = 50
player_x = 100
player_y = win_height - player_height
player_vel = 10
is_jumping = False
jump_vel = 10
jump_height = 100
jump_count = jump_height

# Set up the game loop
clock = pygame.time.Clock()
run = True

while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jumping = True
    
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < win_width - player_width:
        player_x += player_vel
    
    # Handle player jumping
    if is_jumping:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = jump_height
    
    # Draw the player and update the display
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.display.update()
    
    # Set the FPS and update the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
