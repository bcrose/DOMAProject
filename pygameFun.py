import pygame


class Sprite:
    def __init__(self, x, y, width, height, vel, delta, u):
        self.x =x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.delta = delta
        self.u = u


def main():
    pygame.init()

    win = pygame.display.set_mode((500,500))

    run = True
    sprite1 = Sprite(0, 0, 40, 60, 20, 20, 0)
    sprite2 = Sprite(0, 470, 30, 30, 11, 11, 0)
    while run:
        pygame.time.delay(100)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        sprite1.u += sprite1.delta
        if sprite1.u >= 500:
           sprite1.delta = -sprite1.vel
        elif sprite1.u < sprite1.width:
           sprite1.delta = sprite1.vel
        sprite1.x += sprite1.delta

        sprite2.u += sprite2.delta
        if sprite2.u >= 500:
            sprite2.delta = -sprite2.vel
        elif sprite2.u < sprite2.width:
            sprite2.delta = sprite2.vel
        sprite2.x += sprite2.delta
        #keys = pygame.get_pressed()
        # if keys(pygame.K_UP):

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 255, 0), (sprite1.x, sprite1.y, sprite1.width, sprite1.height))
        pygame.draw.rect(win, (0, 255, 255), (sprite2.x, sprite2.y, sprite2.width, sprite2.height))
        pygame.display.update()
        pygame.event.pump()
    pygame.quit()


main()
