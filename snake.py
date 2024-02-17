import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed = 10

# Food variables
food_pos = [random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
            random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE]
food_spawn = True

# Score variable
score = 0

# Function to display the score
def display_score(score):
    font = pygame.font.SysFont("arial", 25)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [0, 0])

# Main game function
def main():
    global change_to, s
