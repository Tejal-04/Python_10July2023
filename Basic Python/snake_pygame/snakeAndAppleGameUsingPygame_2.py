import pygame
# This module contains various constants used by pygame.
from pygame.locals import *

class Snake:
    def __init__(self,surface):
        self.parent_screen = surface
        # Load new image from a file (or file-like object)
        self.block = pygame.image.load('resources/block.jpg').convert() 
        self.x = 100
        self.y = 100    

    def draw(self):
        self.parent_screen.fill((110,110,5))    # For clearing screen
        # Draw one image onto another
        self.parent_screen.blit(self.block,(self.x,self.y))
        # Update the full display Surface to the screen
        pygame.display.flip()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_left(self):
        self.x -= 10   
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()        

class Game:
    def __init__(self):
        pygame.init()      # Initialize the whole module which was used in program
        # Initialize a window or screen for display
                           # set_mode(screen_width,screen_height)
        self.surface = pygame.display.set_mode((500,500)) 
        # Fill Surface with a solid color
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            # Get events from the queue
            for event in pygame.event.get():
                # pygame constants
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False    
    

if __name__ == '__main__':
    game = Game()
    game.run()