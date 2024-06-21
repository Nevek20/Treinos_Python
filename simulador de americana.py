import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 1540
SCREEN_HEIGHT = 818
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Americana Driver Simulator")

GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
ORANGE = (255, 70, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(BLUE)
        pygame.draw.rect(self.image, BLACK, [0, 60, 10, 20])
        pygame.draw.rect(self.image, BLACK, [40, 60, 10, 20])
        pygame.draw.rect(self.image, BLACK, [0, 0, 10, 20])
        pygame.draw.rect(self.image, BLACK, [40, 0, 10, 20])
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 8
        self.wheel_angle = 0  # ângulo inicial das rodas

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.wheel_angle = 45  # girar as rodas para a esquerda
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.wheel_angle = -45  # girar as rodas para a direita
        else:
            self.wheel_angle = 0  # manter as rodas retas quando não estiver virando

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.original_image, self.wheel_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)

class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(55, 55)
        pygame.draw.rect(self.image, BLACK, [0, 50, 10, 20])
        pygame.draw.rect(self.image, BLACK, [30, 50, 10, 20])
        pygame.draw.rect(self.image, BLACK, [0, 0, 10, 20])
        pygame.draw.rect(self.image, BLACK, [30, 0, 10, 20])
        

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
    draw_text(SCREEN, "GAME OVER", 50, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(SCREEN, f"Sua pontuação: {points}", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(SCREEN, "Aperte qualquer botão para reiniciar", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
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

        if pygame.time.get_ticks() - start_time >= 100:
            points += 1
            start_time = pygame.time.get_ticks()

        collisions = pygame.sprite.spritecollide(player, enemies, False)
        if collisions:
            game_over_flag = True

        draw_screen()

        clock.tick(60)

pygame.quit()