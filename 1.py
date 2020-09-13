import pygame

pygame.init()
win = pygame.display.set_mode((800, 500))

pygame.display.set_caption("My Game")

x = 50
y = 430
width = 50
height = 50
speed = 20

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 800 - width - speed:
        x += speed
    if isJump is False:
        if keys[pygame.K_UP] and y > speed:
            y -= speed
        elif keys[pygame.K_DOWN] and y < 450 - speed:
            y += speed
        elif keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount * 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
