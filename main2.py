#Treasure Hunt
import pygame, time, random

pygame.init()

pygame.display.set_caption("Treasure Hunt !")

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

#Background
def change_background():
    BLUE = (0, 105, 148)
    screen.fill(BLUE)

#Classes
class Pirate_ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pirate_ship.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Treasure(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy_pirate_ship.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("key.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

#Sprite groups
allsprites = pygame.sprite.Group()
item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
bonus_list = pygame.sprite.Group()

#Objects
pirate_ship = Pirate_ship()
allsprites.add(pirate_ship)

for i in range(20):
    plastic = Obstacle()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

images = ["gold_coin.png", "jewels.png"]

for i in range(50):
    item = Treasure(random.choice(images))
    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)
    item_list.add(item)
    allsprites.add(item)

for i in range(5):
    bonus = Bonus()
    bonus.rect.x = random.randrange(screen_width)
    bonus.rect.y = random.randrange(screen_height)
    bonus_list.add(bonus)
    allsprites.add(bonus)
    
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

    #Win or lose
    if total_time >= 60:
        if score >= 20:
            screen.fill(GREEN)
            text1 = myFont.render("Treasure loot successful",True, BLACK)

        else:
            screen.fill(RED)
            text1 = myFont.render("Treasure loot unsuccessful", True, BLACK)

        screen.blit(text1, (250, 40))

    else:
        change_background()
        countdown = myFont.render("Time Left: " + str(60 - int(total_time)), True, BLACK)
        screen.blit(countdown, (20, 20))

        #Control pirate_ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate_ship.rect.y > 0:
                pirate_ship.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if pirate_ship.rect.y < 630:
                pirate_ship.rect.y += 5

        if keys[pygame.K_RIGHT]:
            if pirate_ship.rect.x < 850:
                pirate_ship.rect.x += 5

        if keys[pygame.K_LEFT]:
            if pirate_ship.rect.x > 0:
                pirate_ship.rect.x -= 5

        #If pirate_ship hits recyclable items
        item_hit_list = pygame.sprite.spritecollide(pirate_ship, item_list, True)

        for item in item_hit_list:
            score += 1
            text = myFont.render("Score = "+ str(score), True, BLACK)

        #If pirate_ship hits non-recyclable items
        plastic_hit_list = pygame.sprite.spritecollide(pirate_ship, plastic_list, True)

        for plastic in plastic_hit_list:
            score = score - 5
            text = myFont.render("Score = "+ str(score), True, BLACK)

        #If pirate ship hits bonus items
        bonus_hit_list = pygame.sprite.spritecollide(pirate_ship, bonus_list, True)

        for bonus in bonus_hit_list:
            score = score + 10
            text = myFont.render("Score = "+ str(score), True, BLACK)


    screen.blit(text, (20,50))

    allsprites.draw(screen)
    pygame.display.update()

pygame.quit()