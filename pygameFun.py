import pygame
import random

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
points = 0
textPoints = myfont.render('Karma: ' + str(points), False, (0, 0, 0))
buddha = Sprite(0, 30, 40, 60, 20, 20, 0)
coin = Sprite(random.randint(2, 490), 500, 5, 5, -40, -40, 500)


def main():
    # initialize windows
    win = pygame.display.set_mode((500, 500))
    win1 = pygame.display.set_mode((500, 500))
    run = False
    domaPic = pygame.image.load("doma.jpg").convert()
    templePic = pygame.image.load("temple.jpg").convert()
    theBuddha = pygame.image.load("theBuddha.jpg").convert_alpha()

    # menu loop
    while not run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
        win1.blit(domaPic, [0, 0])
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            buddha.x -= buddha.vel
        if keys[pygame.K_RIGHT]:
            buddha.x += buddha.vel
        # Code for hand movement
        coin.y += coin.delta
        if coin.y <= 0:
            coin.y = 490
            coin.x = random.randint(2, 490)
        coin.y += coin.delta

        # this is the attempted but currently broken code to throw the coin
        # This is where everything is drawn on the window
        win1.blit(templePic, [0, 0])
        pygame.draw.rect(win, (0, 0, 0), (buddha.x, buddha.y, buddha.width, buddha.height))
        win1.blit(theBuddha, [buddha.x, buddha.y])
        pygame.draw.rect(win, (255, 255, 0), (coin.x, coin.y, coin.width, coin.height))
        win1.blit(textPoints, (380, 0))
        pygame.display.update()
        pygame.event.pump()
    pygame.quit()


main()
