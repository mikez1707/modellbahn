import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

train_x = 100
train_y = 300
speed = 200  # Pixel pro Sekunde

running = True







class City:
    def __init__(self, name, x, y, population):
        self.name = name
        self.x = x
        self.y = y
        self.population = population

    def draw(self, screen, camera_x, camera_y):
        x = self.x - camera_x
        y = self.y - camera_y

        pygame.draw.circle(screen, (80, 120, 220), (x, y), 20)


berlin = City("Berlin", 5000, 3000, 3_500_000)
hamburg = City("Hamburg", 2000, 1000, 1_900_000)

class Train:
    def __init__(self, name, x, y, speed):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed

    def update(self, dt):
        self.x += self.speed * dt

    def draw(self, screen, camera_x, camera_y):
        x = self.x - camera_x
        y = self.y - camera_y

        pygame.draw.rect(screen, (200, 50, 50), (x, y, 80, 30))

train = Train("ICE 1", 100, 300, 100)


class Track:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Industry:
    def __init__(self, name, x, y, produces, consumes):
        self.name = name
        self.x = x
        self.y = y
        self.produces = produces
        self.consumes = consumes


savegame = {
    "money": 100000,
    "trains": [
        {
            "name": "ICE 1",
            "x": 500,
            "y": 300
        }
    ],
    "tracks": [
        {
            "start": "Berlin",
            "end": "Hamburg"
        }
    ]
}


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




    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        print("Klick:", mouse_x, mouse_y)



    """train.update(dt)
    train.draw(screen, camera_x, camera_y)"""



        
    camera_x = 1000
    camera_y = 500

    world_x = 1200
    world_y = 700

    screen_x = world_x - camera_x
    screen_y = world_y - camera_y


    pygame.draw.line(
        screen,
        (80, 80, 80),
        (100, 300),
        (700, 300),
        12
    )

    pygame.draw.line(
        screen,
        (180, 180, 180),
        (100, 294),
        (700, 294),
        2
    )

    pygame.draw.line(
        screen,
        (180, 180, 180),
        (100, 306),
        (700, 306),
        2
    )










    pygame.draw.rect(screen, (60, 60, 60), (0, 320, 800, 40))
    pygame.draw.rect(screen, (200, 50, 50), (train_x, train_y, 100, 40))

    pygame.display.flip()

pygame.quit()




"""
railway_game/
│
├── main.py
│
├── game/
│   ├── game.py
│   ├── camera.py
│   └── input.py
│
├── world/
│   ├── city.py
│   ├── industry.py
│   ├── track.py
│   └── map.py
│
├── trains/
│   ├── train.py
│   └── locomotive.py
│
├── economy/
│   ├── economy.py
│   └── cargo.py
│
├── ui/
│   ├── menu.py
│   └── information_panel.py
│
├── assets/
│   ├── trains/
│   └── graphics/
│
└── saves/
"""