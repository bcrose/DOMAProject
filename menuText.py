import pygame


class menu:

    pygame.init()
    pygame.font.init()

    # initialize the sprites needed for the game and text objects  for the menu
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    line1 = myfont.render('Karma Catcher', False, (0, 0, 0))
    line2 = myfont.render('Welcome! Catch coins as the Buddha with the arrow keys', False, (0, 0, 0))
    line3 = myfont.render('Build Karma for each coin you catch', False, (0, 0, 0))
    line4 = myfont.render('Earn 100 karma for a museum secret', False, (0, 0, 0))
    line6 = myfont.render('Press Enter to Begin', False, (0, 0, 0))
    endLine1 = myfont.render('Congratulations here is your museum secret!', False, (0, 0, 0))
    endLine2 = myfont.render('Similar to frog baby, if you visit the ', False, (0, 0, 0))
    endLine3 = myfont.render('Buddha, he can give you good luck.', False, (0, 0, 0))
    endLine4 = myfont.render('Instead of rubbing his nose just leave him a penny', False, (0, 0, 0))
