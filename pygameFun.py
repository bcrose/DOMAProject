import pygame

# a sprite class to create different size of sprites with different movement


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

# initialize the sprites needed for the game and text objects  for the menu
myfont = pygame.font.SysFont('Comic Sans MS', 25)
textsurface = myfont.render('Doma Games', False, (255, 0, 255))
textsurface1 = myfont.render('Welcome! Throw coins to the Buddha', False, (255, 0, 255))
textsurface2 = myfont.render('Build Karma for each coin he catches', False, (255, 0, 255))
textsurface3 = myfont.render('Earn 100 karma for a museum secret', False, (255, 0, 255))
textsurface5 = myfont.render('Press spacebar to throw', False, (255, 0, 255))
textsurface4 = myfont.render('Press Enter to Begin', False, (255, 0, 255))
buddha = Sprite(0, 0, 40, 60, 20, 20, 0)
hand = Sprite(0, 470, 30, 30, 11, 11, 0)


def main():
    # initialize windows
    win = pygame.display.set_mode((500, 500))
    win1 = pygame.display.set_mode((500, 500))
    run = False
    background_image = pygame.image.load("doma.jpg").convert()

    # menu loop
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

    # main game loop
    while run:
        pygame.time.delay(100)
        # allows user to quit with the x button in the corner of the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Code for Buddha movement
        buddha.u += buddha.delta
        if buddha.u >= 500:
            buddha.delta = -buddha.vel
        elif buddha.u < buddha.width:
            buddha.delta = buddha.vel
        buddha.x += buddha.delta
        # Code for hand movement
        hand.u += hand.delta
        if hand.u >= 500:
            hand.delta = -hand.vel
        elif hand.u < hand.width:
            hand.delta = hand.vel
        hand.x += hand.delta

        # this is the attempted but currently broken code to throw the coin
        coin = Sprite(hand.x, hand.y, 5, 5, 40, 40, hand.x)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coin.y -= coin.vel
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                coin.y -= coin.vel

        # This is where everything is drawn on the window
        win.fill((255, 0, 255))
        pygame.draw.rect(win, (255, 255, 0), (coin.x, coin.y, coin.width, coin.height))
        pygame.draw.rect(win, (0, 255, 0), (buddha.x, buddha.y, buddha.width, buddha.height))
        pygame.draw.rect(win, (0, 255, 255), (hand.x, hand.y, hand.width, hand.height))
        pygame.display.update()
        pygame.event.pump()
    pygame.quit()


main()
