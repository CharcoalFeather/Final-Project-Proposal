import pygame
from pygame.locals import * 

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Unicorn's Wander")

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

world_data = [
[0, 0, 0, 0, 0],
[0, 0, 0, 2, 2],
[0, 2, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 2, 2, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 2, 2, 2, 1, 1, 2, 2, 2, 1]
]

world = World(world_data)



run = True
while run:

    screen.blit(Background, (0,0))
    world.draw()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()