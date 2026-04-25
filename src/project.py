import os 
import random
import math 
import pygame

#Gameloop
pygame.init()
pygame.display.set_caption("A Unicorn's Wander")

#Global Variables
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
FPS = 60 
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Player Class

#Background 

def main(window):
    clock = pygame.time.Clock()    
    run = True 

    while run:
        clock.tick(FPS)
    #This while loop ensure our game runs at 60 fps.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 

    pygame.quit()
    quit()


    pass
    #Inside of main will be our event loop. 


if __name__ =="__main__":
    main(window)