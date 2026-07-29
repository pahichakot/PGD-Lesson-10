#Recycle Marathon
import pygame, time, random

pygame.init()

pygame.display.set_caption("Recycle Marathon")

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

#Backgrounds
def change_background(image):
    background = pygame.image.load(image)
    bg = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(bg, (0,0))

#Classes
class Bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__(self)
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

#Sprite groups
allsprites = pygame.sprite.Group()
item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

#Objects
bin = Bin()
allsprites.add(bin)

for i in range(20):
    plastic = Non_recyclable()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

images = ["item1.png", "item2.png", "item3.png"]

for i in range(50):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

playing = True
score = 0

#Initialize time
clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score =" + str(0), True, BLACK)

while playing:
    #Control game speed
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False

    total_time = time.time() - start_time

    if total_time >= 60:
        if score >= 20:
            screen.fill(GREEN)
            text1 = myFont.render("Bin loot successful",True, BLACK)

        else:
            screen.fill(RED)
            text1 = myFont.render("Bin loot unsuccessful", True, BLACK)

        screen.blit(text1, (250, 40))

    else:
        change_background("bground.png")
        countdown = myFont.render("Time Left: " + str(60 - int(total_time)), True, BLACK)
        screen.blit(countdown, (20, 20))