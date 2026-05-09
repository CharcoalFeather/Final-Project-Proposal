import pygame
from pygame.locals import * 

pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Unicorn's Wander")

#Game Variables
tile_size = 60

#Load images
Background = pygame.image.load('assets/Background/Mountains.png')
grass_img = pygame.image.load('assets/Terrain/grass.png')


class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('assets/Terrain/dirt.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class Player(): 
    def __init__(self, x,y):
        self.images_right = []
        self.images_left = []
        self.index = 0 
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'assets/MainCharacters/Unicorn/Unicorn{num}.png')
            img_right = pygame.transform.scale(img_right, (60, 50))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
    
    def update(self):
        dx = 0 
        dy = 0
        walk_cooldown = 5

        #Keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]: 
            dx -= 5
            self. counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]: 
            dx += 5
            self. counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]


        #animatiopn
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.images_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]
        

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        

        #Check for collision

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        #Draws our Unicorn
        screen.blit(self.image, self.rect)

#Determines block placements
world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 2, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
[0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 2, 2, 2, 1, 1, 2, 2, 2, 1]
]

world = World(world_data)
player = Player(100, HEIGHT - 130)

#Game loop
run = True
while run:


    clock.tick(fps)

    #Displays our images
    screen.blit(Background, (0,0))
    world.draw()
    player.update()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()