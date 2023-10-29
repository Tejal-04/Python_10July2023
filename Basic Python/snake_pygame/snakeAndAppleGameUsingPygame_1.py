import pygame
# This module contains various constants used by pygame.
from pygame.locals import *

def draw_block():
    surface.fill((110,110,5))    # For clearing screen
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()      # Initialize the whole module which was used in program

    # Initialize a window or screen for display
                           # set_mode(screen_width,screen_height)
    surface = pygame.display.set_mode((500,500)) 
    # Fill Surface with a solid color
    surface.fill((110,110,5))

    # Load new image from a file (or file-like object)
    block = pygame.image.load('resources/block.jpg').convert()
    block_x = 100
    block_y = 100
    # Draw one image onto another
    surface.blit(block,(block_x,block_y))

    # Update the full display Surface to the screen
    pygame.display.flip()

    running = True
    while running:
        # Get events from the queue
        for event in pygame.event.get():
            # pygame constants
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y +=10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -=10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
