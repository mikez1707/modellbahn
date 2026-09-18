import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

train_x = 100
train_y = 300
speed = 200  # Pixel pro Sekunde

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        train_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        train_x += speed * dt

    screen.fill((50, 150, 70))

    pygame.draw.rect(screen, (60, 60, 60), (0, 320, 800, 40))
    pygame.draw.rect(screen, (200, 50, 50), (train_x, train_y, 100, 40))

    pygame.display.flip()

pygame.quit()