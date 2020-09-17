import pygame

pygame.init()
win = pygame.display.set_mode((1400, 700))
WHITE = (255, 255, 255)
win.fill(WHITE)
w, h = pygame.display.get_surface().get_size()

pygame.display.set_caption("My Game")

yura_width = 150
yura_height = 147
yura_speed = 20
x = w / 2 - (yura_width / 2)
y = h - yura_height


isJump = False
jumpCount = 10

image = pygame.image.load('yura.png')
background = pygame.image.load('screen.png')

run = True
while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > yura_speed:
        x -= yura_speed
    elif keys[pygame.K_RIGHT] and x < w - yura_width - yura_speed:
        x += yura_speed
    if isJump is False:
        if keys[pygame.K_UP] and y > yura_speed:
            y -= yura_speed
        elif keys[pygame.K_DOWN] and y < h - yura_height - yura_speed:
            y += yura_speed
        elif keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount * 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.blit(background, (0, 0))
    win.blit(image, (x, y))
    pygame.display.update()

pygame.quit()
