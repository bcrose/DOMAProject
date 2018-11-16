import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
x = 0
y = 0
width = 40
height = 60
vel = 20
delta = 20
u =0
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    u += delta
    if u >= 500: 
       delta = -20
    elif u < 40:
       delta = 20
    x += delta

    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()

