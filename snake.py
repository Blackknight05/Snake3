import os
import pygame
import random
from pygame.locals import *

# Set up the virtual display with Xvfb
os.environ['SDL_VIDEODRIVER'] = 'x11'
os.environ['DISPLAY'] = ':0'

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed = 15

# Food
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Score
score = 0

# Game Over
def game_over():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Game Over! Your score: ' + str(score), True, BLACK)
    screen.blit(text, [WIDTH // 4, HEIGHT // 
