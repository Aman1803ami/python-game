import pygame
import random

# initialize pygame
pygame.init()

# set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the game title
pygame.display.set_caption("My Game")

# set the game clock
clock = pygame.time.Clock()

# set the font
font = pygame.font.Font(None, 36)

# define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
        elif keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

# define the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
        self.speed = random.randint(1, 5)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            self.speed = random.randint(1, 5)

# create the sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# create the player sprite
player = Player()
all_sprites.add(player)

# create the enemy sprites
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# set the initial score
score = 0

# set the game loop flag
running = True

# game loop
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update the sprites
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemies.update()
    
    # check for collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
    
    # draw the sprites
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    
    # update the score
    score += 1
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # update the screen
    pygame.display.flip()
    
    # tick the clock
    clock.tick(60)

# clean up pygame
pygame.quit()
print("you scored ",score)