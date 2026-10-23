
import pygame

def main():
    pygame.init()

    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cute Wildlife World")

    green = pygame.Color("green")
    black = pygame.Color("black")
    white = pygame.Color("white")

    title_font = pygame.font.SysFont("Impact", 27)
    fact_font = pygame.font.SysFont("Impact", 17)
    small_font = pygame.font.SysFont("arial", 12)

    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (500, 500))

    tiger = pygame.image.load("tiger.png")
    tiger = pygame.transform.scale(tiger, (100, 100))

    bunny = pygame.image.load("bunny.png")
    bunny = pygame.transform.scale(bunny, (75, 75))

    cat = pygame.image.load("cat.png")
    cat = pygame.transform.scale(cat, (75, 75))

    fox = pygame.image.load("fox.png")
    fox = pygame.transform.scale(fox, (75, 75))

    panda = pygame.image.load("panda.png")
    panda = pygame.transform.scale(panda, (75, 75))

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(background, (0, 0))
        Blue = (173, 216, 230)
        heading = title_font.render("Wildlife World!", True, Blue)
        screen.blit(heading, heading.get_rect(center=(250, 30)))

        screen.blit(bunny, (135, 270))
        screen.blit(cat, (280, 280))
        screen.blit(tiger, (200, 260))
        screen.blit(fox, (55, 270))
        screen.blit(panda, (385, 260))

        names = [
            ("Bunny", 155, 360),
            ("Cat", 310, 360),
            ("Tiger", 230, 360),
            ("Fox", 75, 360),
            ("Panda", 410, 360)
        ]

        for name, x, y in names:
            label = fact_font.render(name, True, white)
            screen.blit(label, label.get_rect(center=(x, y)))

        pygame.draw.rect(screen, white, (25, 380, 450, 85))
        Yellow = (218, 165, 32)
        fact1 = fact_font.render("Fun Animal Fact!", True, Yellow)
        fact2 = small_font.render("Pandas can eat 20-38 kg of bamboo daily!", True, black)
        fact3 = small_font.render("Rabbits can run between 25-45 miles per hour!", True, black)

        screen.blit(fact1, (40, 390))
        screen.blit(fact2, (40, 415))
        screen.blit(fact3, (40, 440))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

main()
