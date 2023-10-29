import pygame
# This module contains various constants used by pygame.
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110,110,5)

class Apple:

    def __init__(self,parent_screen):
        self.parent_screen = parent_screen 
        # Load new image from a file (or file-like object)
        self.image = pygame.image.load('resources/apple.jpg').convert()
        self.x = 120
        self.y = 120

    def draw_apple(self):
        # Draw one image onto another
        self.parent_screen.blit(self.image,(self.x,self.y))

        # Update the full display Surface to the screen
        pygame.display.flip()    

    def move(self):
        self.x = random.randint(0,19)*SIZE    # 20 times increments => 800/40 = 20 => (0,20)*40
        self.y = random.randint(0,14)*SIZE    # 15 times increments =>600/40 = 15 (0,15)*40

class Snake:

    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        # Load new image from a file (or file-like object)
        self.block = pygame.image.load('resources/block.jpg').convert() 
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)    

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def draw_snake(self):
        #self.parent_screen.fill(BACKGROUND_COLOR)    # For clearing screen
        for i in range(self.length):
            # Draw one image onto another
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))

        # Update the full display Surface to the screen
        pygame.display.flip()

    def walk(self):
        # For updating body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw_snake()               

class Game:

    def __init__(self):
        pygame.init()      # Initialize the whole module which was used in program
        pygame.display.set_caption('Snake And Apple Game...')
        pygame.mixer.init()

        self.play_background_music()
        # Initialize a window or screen for display
                           # set_mode(screen_width,screen_height)
        self.surface = pygame.display.set_mode((800,600)) 
        # Fill Surface with a solid color
        # self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,1)
        self.snake.draw_snake()
        self.apple = Apple(self.surface)
        self.apple.draw_apple()

    def is_collision(self,x1,y1,x2,y2):     # For Apple and Block collision together
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return  False
   
    def render_background(self):
        bg = pygame.image.load('resources/background.jpg')
        self.surface.blit(bg,(0,0))

    # Music is long time playing load
    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play()

    # Sound is a short time playing or play only once a time
    def play_sound(self,sound_name):
        if sound_name == 'crash':
            sound = pygame.mixer.Sound('resources/crash.mp3')
        elif sound_name == 'ding':
            sound = pygame.mixer.Sound('resources/ding.mp3')

        pygame.mixer.Sound.play(sound)

    # def play_sound(self,sound):
    #     sound = pygame.mixer.Sound(f"resources/{sound}.mp3")  # Format string in python
    #     pygame.mixer.Sound.play(sound)

    def play(self):
        self.render_background()

        # Objects
        self.snake.walk()   
        self.apple.draw_apple()
        self.display_score()

        pygame.display.flip()

        # Snake eating apple scenario
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            # Mixer is a class which supports the playing the sound
            # Pygame module for loading and playing sounds
            # sound = pygame.mixer.Sound('resources/ding.mp3')
            # pygame.mixer.Sound.play(sound)
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # Snake colliding with Apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            #print('Collision Ocurred')   # If find collision
            self.snake.increase_length()   # incrementing snake length
            self.apple.move()

        # Snake colliding with Itself
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                # print('Game Over')
                # exit(0)
                # sound = pygame.mixer.Sound('resources/crash.mp3')
                # pygame.mixer.Sound.play(sound)
                self.play_sound("crash")
                raise "Game Over"
            
        # Snake colliding with window boundry
        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 800 and 0<= self.snake.y[0] <= 600):
            self.play_sound('crash')
            raise('Hit the boundry error')    
            
    def show_game_over(self):
        # self.surface.fill(BACKGROUND_COLOR) 
        self.render_background()
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game is Over!  Your score is : {self.snake.length}",True,(255,255,255))  # Python format string
        self.surface.blit(line1,(200,300))
        line2 = font.render("To play again press - Enter. To exit press - Escape",True,(255,255,255))
        self.surface.blit(line2,(200,350))
        
        pygame.display.flip()   # Refresh the UI
        pygame.mixer.music.pause()

    def display_score(self):
        #For displaying arial font type with 30px font size
        font = pygame.font.SysFont('arial',30)
        # Draw text on a new Surface
        score = font.render(f"Score : {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(600,10))

    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)    

    def run(self):
        running = True
        pause = False

        while running:
            # Get events from the queue
            for event in pygame.event.get():
                # pygame constants
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:   
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
    
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()    # Class instance
    game.run()