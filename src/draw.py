import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 10)
    object_list.append(kinetic)
    #top blocks
    tblock = KineticBlock(Vector2(50,50), 50, 10, [0, 0, 255])
    object_list.append(tblock)
    tblock1 = KineticBlock(Vector2(150,50), 50, 10, [0, 0, 255])
    object_list.append(tblock1)
    tblock2 = KineticBlock(Vector2(250,50), 50, 10, [0, 0, 255])
    object_list.append(tblock2)
    tblock3 = KineticBlock(Vector2(350,50), 50, 10, [0, 0, 255])
    object_list.append(tblock3)
    #middle blocks
    mblock = KineticBlock(Vector2(100,100), 50, 10, [0, 150, 255])
    object_list.append(mblock)
    mblock1 = KineticBlock(Vector2(200,100), 50, 10, [0, 150, 255])
    object_list.append(mblock1)
    mblock2 = KineticBlock(Vector2(300,100), 50, 10, [0, 150, 255])
    object_list.append(mblock2)
    #bottom blocks
    block = KineticBlock(Vector2(50,150), 50, 10, [0, 200, 255])
    object_list.append(block)
    block1 = KineticBlock(Vector2(150,150), 50, 10, [0, 200, 255])
    object_list.append(block1)
    block2 = KineticBlock(Vector2(250,150), 50, 10, [0, 200, 255])
    object_list.append(block2)
    block3 = KineticBlock(Vector2(350,150), 50, 10, [0, 200, 255])
    object_list.append(block3)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # Do something
            pass
        if keys[pygame.K_RIGHT]:
            # Do something
            pass

        for object in object_list:
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
