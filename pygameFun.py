import pygame


class Buddha:
    x = 0
    y = 0
    width = 40
    height = 60
    vel = 20
    delta = 20
    u = 0


def main():
    pygame.init()

    win = pygame.display.set_mode((500,500))

    run = True
    sprite1 = Buddha()
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        sprite1.u += sprite1.delta
        if sprite1.u >= 500:
           sprite1.delta = -20
        elif sprite1.u < 40:
           sprite1.delta = 20
        sprite1.x += sprite1.delta

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 255, 0), (sprite1.x, sprite1.y, sprite1.width, sprite1.height))
        pygame.display.update()
    pygame.quit()


main()
