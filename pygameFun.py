import pygame
import random
import spriteClass
import menuText

# a sprite class to create different size of sprites with different movement

pygame.init()
pygame.font.init()
buddha = spriteClass.Sprite(0, 30, 40, 60, 28, 28, 0)
coin = spriteClass.Sprite(random.randint(2, 490), 500, 15, 15, -26, -26, 500)
menu1 = menuText.menu()


def main():
    # initialize windows
    points = 0
    win = pygame.display.set_mode((750, 500))
    run = False
    end = False
    domaPic = pygame.image.load("doma.jpg").convert()
    templePic = pygame.image.load("temple.jpg").convert()
    theBuddha = pygame.image.load("theBuddha.png").convert_alpha()
    budBackground = pygame.image.load("buddhaBackground.jpg").convert()
    coinSound = pygame.mixer.Sound("coinWav.wav")

    # menu loop
    while not run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
        win.blit(domaPic, [0, 0])
        pygame.draw.rect(win, (0, 255, 0), (0, 50, 750, 125))
        pygame.draw.rect(win, (255, 0, 0), (0, 0, 750, 50))
        pygame.draw.rect(win, (255, 0, 0), (250, 440, 240, 50))
        win.blit(menu1.line1, (0, 0))
        win.blit(menu1.line2, (0, 50))
        win.blit(menu1.line3, (0, 75))
        win.blit(menu1.line4, (0, 100))
        win.blit(menu1.line6, (250, 440))

        pygame.display.update()

    # main game loop
    while run:
        pygame.time.delay(100)
        # allows user to quit with the x button in the corner of the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Code for Buddha movement
        buddhaMov()
        # Code for coin movement and collisions
        coin.y += coin.delta
        if coin.y <= buddha.y + buddha.height:
            if coin.x in range(buddha.x, buddha.x +buddha.width):
                coin.y = 490
                coin.x = random.randint(2, 490)
                points += 10
                pygame.mixer.Sound.play(coinSound)
        coin.y += coin.delta

        if coin.y <= 0:
            coin.y = 490
            coin.x = random.randint(2, 490)
        coin.y += coin.delta

        if points >= 100:
            run = False
            end = True

        # this is the attempted but currently broken code to throw the coin
        # This is where everything is drawn on the window
        # textPoints is instantiated at the end of the loop since it is ever changing
        textPoints = menu1.myfont.render('Karma: ' + str(points), False, (0, 0, 0))
        win.blit(templePic, [0, 0])
        pygame.draw.rect(win, (0, 0, 0), (buddha.x, buddha.y, buddha.width, buddha.height))
        win.blit(theBuddha, [buddha.x, buddha.y])
        pygame.draw.rect(win, (255, 215, 0), (coin.x, coin.y, coin.width, coin.height))
        win.blit(textPoints, (630, 0))
        pygame.display.update()
        while end:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
            win.blit(budBackground, [0, 0])
            pygame.draw.rect(win, (0, 255, 0), (0, 0, 750, 125))
            win.blit(menu1.endLine1, (0, 0))
            win.blit(menu1.endLine2, (0, 25))
            win.blit(menu1.endLine3, (0, 50))
            win.blit(menu1.endLine4, (0, 75))


            pygame.display.update()

    pygame.quit()


def buddhaMov():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        buddha.x -= buddha.vel
        if buddha.x <= 0:
            buddha.x = 0
    if keys[pygame.K_RIGHT]:
        buddha.x += buddha.vel
        if buddha.x >= 750:
            buddha.x = 710


main()
