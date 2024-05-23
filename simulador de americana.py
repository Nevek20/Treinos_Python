import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulador de motoristas de Americana")

GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
ORANGE = (255, 70, 0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = random.randint(6, 12)

def draw_screen():
    SCREEN.fill(GRAY)
    all_sprites.draw(SCREEN)
    draw_text(SCREEN, f"Pontos: {points}", 20, SCREEN_WIDTH // 20, 10)
    pygame.display.flip()

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def game_over(points):
    SCREEN.fill(RED)
    draw_text(SCREEN, "VOCÊ MORREU", 50, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(SCREEN, f"Pontuação: {points}", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(SCREEN, "Pressione qualquer tecla para tentar novamente", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.flip()

player = PlayerCar()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemies = pygame.sprite.Group()
for _ in range(10):
    enemy = EnemyCar()
    all_sprites.add(enemy)
    enemies.add(enemy)

points = 0
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
game_over_flag = False
while running:
    if game_over_flag:
        game_over(points)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for sprite in all_sprites:
                    sprite.kill()
                player = PlayerCar()
                all_sprites.add(player)
                for _ in range(10):
                    enemy = EnemyCar()
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                points = 0
                start_time = pygame.time.get_ticks()
                game_over_flag = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        if pygame.time.get_ticks() - start_time >= 1000:
            points += 10
            start_time = pygame.time.get_ticks()

        collisions = pygame.sprite.spritecollide(player, enemies, False)
        if collisions:
            game_over_flag = True

        draw_screen()

        clock.tick(60)

pygame.quit()