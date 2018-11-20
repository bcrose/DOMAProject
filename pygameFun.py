import pygame


class Sprite:
    def __init__(self, x, y, width, height, vel, delta, u):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.delta = delta
        self.u = u

        
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 25)
textsurface = myfont.render('Doma Games', False, (255, 0, 255))
textsurface1 = myfont.render('Welcome! Throw coins to the Buddha', False, (255, 0, 255))
textsurface2 = myfont.render('Build Karma for each coin he catches', False, (255, 0, 255))
textsurface3 = myfont.render('Earn 100 karma for a museum secret', False, (255, 0, 255))
textsurface5 = myfont.render('Press spacebar to throw', False, (255, 0, 255))
textsurface4 = myfont.render('Press Enter to Begin', False, (255, 0, 255))
sprite1 = Sprite(0, 0, 40, 60, 20, 20, 0)

sprite2 = Sprite(0, 470, 30, 30, 11, 11, 0)


def main():

    win = pygame.display.set_mode((500, 500))
    win1 = pygame.display.set_mode((500, 500))
    run = False
    background_image = pygame.image.load("doma.jpg").convert()

    while not run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
        win1.blit(background_image, [0, 0])
        win1.blit(textsurface, (0, 0))
        win1.blit(textsurface1, (0, 50))
        win1.blit(textsurface2, (0, 75))
        win1.blit(textsurface3, (0, 100))
        win1.blit(textsurface5, (0, 125))
        win1.blit(textsurface4, (250, 440))

        pygame.display.update()

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
        sprite3 = Sprite(sprite2.x, sprite2.y, 5, 5, 40, 40, sprite2.x)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and sprite3.y > 0:
                sprite3.y -= sprite3.vel

        win.fill((255, 0, 255))
        pygame.draw.rect(win, (255, 255, 0), (sprite3.x, sprite3.y, sprite3.width, sprite3.height))
        pygame.draw.rect(win, (0, 255, 0), (sprite1.x, sprite1.y, sprite1.width, sprite1.height))
        pygame.draw.rect(win, (0, 255, 255), (sprite2.x, sprite2.y, sprite2.width, sprite2.height))

        pygame.display.update()
        pygame.event.pump()
    pygame.quit()


main()
