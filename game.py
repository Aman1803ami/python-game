import pygame
import random


pygame.init()


WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


clock = pygame.time.Clock()


player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
enemy_x = random.randint(0, WIDTH)
enemy_y = random.randint(0, HEIGHT)
enemy_speed = 2


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    
    if enemy_x < player_x:
        enemy_x += enemy_speed
    else:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    else:
        enemy_y -= enemy_speed
    
    
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        running = False
    
    
    window.fill((255, 255, 255))
    
    
    pygame.draw.rect(window, (0, 255, 0), (player_x, player_y, 50, 50))
    pygame.draw.rect(window, (255, 0, 0), (enemy_x, enemy_y, 50, 50))
    
    
    pygame.display.update()
    

    clock.tick(60)


