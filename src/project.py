import os 
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("A Unicorn's Wander")

#Global Variables
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
FPS = 60 
PLAYER_VEL = 5
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Player Class
class Player(pygame.sprite.Sprite):
    #using sprite allows us to do pixel perfect collision
    COLOR = (255, 0, 0) #class variable so its accesible 
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) # rect is a tuple storing values
        #We will move our player using a velocity in a direction
        self.x_vel = 0 
        self.y_vel = 0 
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        #we call the loop once every frame, and it will move the character.
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

#Background 
def get_background(name):
    #image code joins asset and background paths together. and loads the file name.
    image = pygame.image.load(join("assets", "Background", name))
    #we can ignore x & y size. we then set tiles to equal a width.
    _, _, width, height = image.get_rect()
    tiles = []
    #This code tells us how many tiles are needed to fill our screen.
    for i in range(WIDTH // width + 1 ):
        for j in range(HEIGHT // height + 1):
            #pos notes the pose of the top left hand corner tile. 
            #remember everything is anchored at the top left corner.
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image, player):
# We are looping through tiles and they will return determined by previously mentioned code.
    for tile in background:
        window.blit(bg_image, tile)
    
    player.draw(window)


    pygame.display.update()

def handle_move(player):
        keys = pygame.key.get_pressed()
        player.x_vel = 0
        if keys[pygame.K_LEFT]:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            player.move_right(PLAYER_VEL)

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")
    
    player = Player(100, 100, 50, 50)

    run = True 

    while run:
        clock.tick(FPS)
    #This while loop ensure our game runs at 60 fps.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
    
    player.loop(FPS)
    handle_move(player)
    draw(window, background, bg_image, player)

    pygame.quit()
    quit()


    pass
    #Inside of main will be our event loop. 


if __name__ =="__main__":
    main(window)