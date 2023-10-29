import pygame
# This module contains various constants used by pygame.
from pygame.locals import *
import time

SIZE = 40

class Apple:
    def __init__(self,surface):
        self.parent_screen = surface
        # Load new image from a file (or file-like object)
        self.image = pygame.image.load('resources/apple.jpg').convert()
        self.x = SIZE + 3
        self.y = SIZE + 3

    def draw(self):
        # Draw one image onto another
        self.parent_screen.blit(self.image,(self.x,self.y))
        # Update the full display Surface to the screen
        pygame.display.flip()    

class Snake:
    def __init__(self,surface,length):
        self.length = length
        self.parent_screen = surface
        # Load new image from a file (or file-like object)
        self.block = pygame.image.load('resources/block.jpg').convert() 
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'right'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((110,110,5))    # For clearing screen
        for i in range(self.length):
            # Draw one image onto another
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        # Update the full display Surface to the screen
        pygame.display.flip()

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()               

class Game:
    def __init__(self):
        pygame.init()      # Initialize the whole module which was used in program
        # Initialize a window or screen for display
                           # set_mode(screen_width,screen_height)
        self.surface = pygame.display.set_mode((800,600)) 
        # Fill Surface with a solid color
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        # Objects
        self.snake.walk()   
        self.apple.draw()

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
    
            self.play()

            time.sleep(.3)

if __name__ == '__main__':
    game = Game()    # Class instance
    game.run()