import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 50

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("C:/Users/Public/Documents/ACP PYTHON/Pygame/Lesson 4/bg3.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)
small_font = pygame.font.SysFont("Arial", 25)

WHITE = (255, 255, 255)
BLUE = (84, 130, 209)
LAVENDER = (234, 229, 252)
DARK_BLUE = (46, 69, 125)
PURPLE = (87, 73, 143)
YELLOW = (242, 205, 85)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Collection Game!")

all_sprites = pygame.sprite.Group()

pet = Sprite(PURPLE, 45, 45)
pet.rect.x = 30
pet.rect.y = 180
all_sprites.add(pet)

food_rect = pygame.Rect(0, 0, 30, 30)
food_rect.center = (random.randint(100, SCREEN_WIDTH - 30), random.randint(30, SCREEN_HEIGHT - 30))

running = True
food_collected = False
score = 0

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    if not food_collected:
        keys = pygame.key.get_pressed()
        x_change = (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])) * MOVEMENT_SPEED
        y_change = (int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) * MOVEMENT_SPEED
        pet.move(x_change, y_change)

        if pet.rect.colliderect(food_rect):
            food_collected = True
            score = 1

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if not food_collected:
        pygame.draw.circle(screen, YELLOW, food_rect.center, 15)

    score_text = small_font.render("Food: " + str(score), True, DARK_BLUE)
    screen.blit(score_text, (10, 10))

    if food_collected:
        win_text = font.render("Food Collected!", True, DARK_BLUE)
        text_x = (SCREEN_WIDTH - win_text.get_width()) // 2
        text_y = (SCREEN_HEIGHT - win_text.get_height()) // 2
        screen.blit(win_text, (text_x, text_y))

        happy_text = small_font.render("Your pet is happy!", True, PURPLE)
        screen.blit(happy_text, (145, 260))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()